{-# LANGUAGE DeriveGeneric, OverloadedStrings #-}
module CodeGen ((<$>), generatePythonClass, generateIneq, TSLInput(..), TSLInputTheorem(..), TSLTheorem(..)) where

import qualified Data.Set as S
import Data.Set (Set)
import Parser

import Debug.Trace

import qualified Data.List as L
import Control.Monad (liftM2, replicateM)
import Control.Monad.Fix (fix)

import System.Process (createProcess, CreateProcess(..), StdStream(CreatePipe), proc, waitForProcess)
import System.Exit
import System.IO (hPutStrLn, hGetLine, hFlush)
import Data.Aeson (FromJSON(..), ToJSON(..))
import GHC.Generics

import Prelude hiding ((<$>))

infixl 4 <$>
f <$> m = fmap f m

data TSLInput = TSLInput { theorems :: [TSLInputTheorem] } deriving Generic
data TSLInputTheorem = TSLInputTheorem 
                        { name, text, disp :: String,
                               idnum :: Int } deriving Generic -- Use 'Int' to prevent BigNum usage

data TSLTheorem = TSLTheorem { info :: TSLInputTheorem, theorem :: [Theorem] }

instance FromJSON TSLInput
instance FromJSON TSLInputTheorem

instance ToJSON TSLInput
instance ToJSON TSLInputTheorem 

{-

 --> Always check for undt with maximum value for RHS invariants
 
-}

getInvolves :: Theorem -> [String]
getInvolves (IExpr i)  = S.toList $ getInvarExprInvolves i
getInvolves (IfStmt i) = S.toList $ getIfStmtInvolves i

getInvarExprInvolves :: InvarExpr -> Set String
getInvarExprInvolves (InvarOr a b)          = S.union (getInvarExprInvolves a) (getInvarExprInvolves b)
getInvarExprInvolves (InvarAnd a b)         = S.union (getInvarExprInvolves a) (getInvarExprInvolves b)
getInvarExprInvolves (InvarExpr a Nothing)  = getValueInvolves a 
getInvarExprInvolves (InvarExpr a (Just b)) = S.union (getValueInvolves a) (getInvarRelExprInvolves b)
getInvarExprInvolves (InvarExprNot a)       = getValueInvolves a
getInvarExprInvolves (InvarExprEven a)       = getValueInvolves a
getInvarExprInvolves (InvarExprOdd a)       = getValueInvolves a

getValueInvolves :: Value -> Set String
getValueInvolves (Invar i) = S.singleton i
getValueInvolves (Paren exp) = getExprInvolves exp
getValueInvolves (Function _ exps) = S.unions . map getExprInvolves $ exps
getValueInvolves _         = S.empty

getInvarRelExprInvolves :: InvarRelExpr -> Set String
getInvarRelExprInvolves (InvarRelExpr _ ex) = getExprInvolves ex

getExprInvolves :: Expr -> Set String
getExprInvolves (Expr t) = foldr (S.union . getTermInvolves) S.empty t

getTermInvolves :: Term -> Set String
getTermInvolves (Mul a b)  = S.union (getTermInvolves a) (getTermInvolves b)
getTermInvolves (Div a b)  = S.union (getTermInvolves a) (getTermInvolves b)
getTermInvolves (Neg a)    = getTermInvolves a
getTermInvolves (Term fac) = getFactorInvolves fac

getFactorInvolves :: Factor -> Set String 
getFactorInvolves (Pow a b) = S.union (getFactorInvolves a) (getFactorInvolves b)
getFactorInvolves (Value v) = getValueInvolves v

getIfStmtInvolves :: IfStmt -> Set String
getIfStmtInvolves (If c iexpl (Just i)) = S.union (getCondInvolves c) (S.union (getInvarExprListInvolves iexpl) (getIfStmtInvolves i))
getIfStmtInvolves (If c iexpl Nothing) = S.union (getCondInvolves c) (getInvarExprListInvolves iexpl)

getInvarExprListInvolves :: InvarExprList -> Set String
getInvarExprListInvolves (InvarExprList l) = foldr (S.union . getInvarExprInvolves) S.empty l

getCondInvolves :: Cond -> Set String
getCondInvolves (CondOr a b)        = S.union (getCondInvolves a) (getCondInvolves b)
getCondInvolves (CondAnd a b)       = S.union (getCondInvolves a) (getCondInvolves b)
getCondInvolves (CondOdd v)         = getValueInvolves v
getCondInvolves (CondEven v)         = getValueInvolves v
getCondInvolves (CondNot v)         = getValueInvolves v
getCondInvolves (Cond ex (Just cr)) = S.union (getValueInvolves ex) (getCondRelInvolves cr)
getCondInvolves (Cond ex Nothing)   = getValueInvolves ex

getCondRelInvolves :: CondRel -> Set String
getCondRelInvolves (CondRel _ e) = getExprInvolves e

-- CODE GENERATION BELOW --

data Bound = Max | Min deriving (Show, Eq)

indent :: [String] -> [String]
indent = map ("\t" ++)

assertNotUdts :: [(Bound, String)] -> String
assertNotUdts = L.intercalate " and " . map (\(_,i) -> i ++ " != \'undt\'") . filter (\(b,_) -> b == Max) 

-- | Expression -> Source

exprToSrc :: Expr -> String
exprToSrc (Expr ts) = L.intercalate "+" $ map termToSrc ts

termToSrc :: Term -> String
termToSrc (Mul a b) = termToSrc a ++ "*" ++ termToSrc b
termToSrc (Div a b) = termToSrc a ++ "/" ++ termToSrc b
termToSrc (Neg a)   = "-" ++ termToSrc a 
termToSrc (Term a)  = factorToSrc a 

factorToSrc :: Factor -> String
factorToSrc (Pow a b) = factorToSrc a ++ "**" ++ factorToSrc b
factorToSrc (Value v) = valueToSrc v

valueToSrc :: Value -> String
valueToSrc (Number n)      = show n
valueToSrc (Function "sqrt" es) = "(" ++ (L.intercalate ", " . map exprToSrc $ es) ++ ")**(1/2)"
valueToSrc (Function s es) = s ++ "(" ++ (L.intercalate ", " . map exprToSrc $ es) ++ ")"
valueToSrc (Local s)       = s
valueToSrc (Invar s)       = s
valueToSrc (Paren e)       = "(" ++ exprToSrc e ++ ")"

-- | Body
generatePythonClass :: TSLTheorem -> [String]
generatePythonClass (TSLTheorem (TSLInputTheorem name text disp idnum) ts)  = 
       (("class " ++ name ++ "(Theorem):"):) . concatMap indent $
             [("def __init__(self):" :) $ 
                indent ["super(" ++ name ++ ", self).__init__(" ++ L.intercalate ", " [show idnum, show text, show disp] ++")"]
             ,("def involves(self, str_invar):" :) $ 
                indent ["return str_invar in " ++ show (L.nub . concatMap getInvolves $ ts)]
             , "def run(self, ingrid_obj):" : concatMap (indent . generatePython) ts]

generatePython :: Theorem -> [String]
generatePython (IExpr i) =  generateIExpr i 
generatePython (IfStmt i) = generateIfStmt i 

generateIExpr :: InvarExpr -> [String]
generateIExpr (InvarOr a b) = undefined
generateIExpr (InvarAnd a b) = 
    generateIExpr a ++ generateIExpr b
generateIExpr (InvarExpr (Invar v) Nothing) = 
    return ("ingrid_obj.set(\'" ++ v ++ "\', True)")
generateIExpr (InvarExprNot (Invar v)) = 
    return ("ingrid_obj.set(\'" ++ v ++ "\', False)")
generateIExpr (InvarExprEven (Invar v)) = 
    [ v ++ "_Max = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Max\')-1"
    , v ++ "_Min = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Min\')+1" 
    , "if even(" ++ v ++ "_Max):"
    , "\tingrid_obj.set(\'" ++ v ++ "\', ind=\'Max\')"
    , "if even(" ++ v ++ "_Min):"
    , "\tingrid_obj.set(\'" ++ v ++ "\', ind=\'Min\')"]
generateIExpr (InvarExprOdd (Invar v)) = 
    [ v ++ "_Max = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Max\')-1"
    , v ++ "_Min = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Min\')+1" 
    , "if odd(" ++ v ++ "_Max):"
    , "\tingrid_obj.set(\'" ++ v ++ "\', ind=\'Max\')"
    , "if odd(" ++ v ++ "_Min):"
    , "\tingrid_obj.set(\'" ++ v ++ "\', ind=\'Min\')"]
generateIExpr (InvarExpr (Function _ _) (Just (InvarRelExpr r exp))) = 
    []
generateIExpr (InvarExpr (Invar v) (Just (InvarRelExpr r exp))) = 
    case r of 
        RelLte -> make Max
        RelGte -> make Min
        RelEq  -> generateIExpr (InvarExpr (Invar v) (Just (InvarRelExpr RelLte exp))) 
                    ++
                  generateIExpr (InvarExpr (Invar v) (Just (InvarRelExpr RelGte exp)))
        _      -> ["return"]
    where 
    make m =        
      let invars = map (\i -> (swap m (exprAnalysis exp i), i)) . S.toList . getExprInvolves $ exp  
      in 
         if any (\(_,i) -> exprAnalysis exp i == Complex) invars 
            then iterateBounds invars m
            else setBound invars m
         
    result m = [ "try:"
               , "\tingrid_obj.set(\'" ++ v ++ "\', " ++ exprToSrc exp ++ ", ind=\'" ++ show m ++ "\')"
               , "except:"
               , "\tpass"]

    setBound invars m = 
            (invars >>= 
                \(b, i) -> [i ++ " = ingrid_obj.get(\'" ++ i ++ "\', ind=\'" ++ show b ++ "\')"])
                            ++ if not . null $ assertNotUdts invars then ("if " ++ assertNotUdts invars ++ ":") : indent (result m) else result m
    iterateBounds ivars m = let  cplx_vars = filter (\(b,i) -> exprAnalysis exp i == Complex) ivars
                                 reg_vars  = filter (\(b,i) -> exprAnalysis exp i /= Complex) ivars 
                                 cplx_perms = map (\x -> zipWith (\b (_,i) -> (b,i)) x cplx_vars ++ reg_vars) (replicateM (length cplx_vars) [Min,Max])
                            in concatMap (`setBound` m) cplx_perms
generateIExpr _ = []

swap :: Bound -> InvarBoundSwitch -> Bound
swap Max (Flip True) = Min
swap Min (Flip True) = Max
swap b   _           = b

flipbound :: InvarBoundSwitch -> InvarBoundSwitch
flipbound (Flip a) = Flip $ not a
flipbound NotFound = Flip True
flipbound a        = a

data InvarBoundSwitch = Flip Bool | NotFound | Complex deriving Eq

exprAnalysis :: Expr -> String -> InvarBoundSwitch
exprAnalysis (Expr exps) inv = let analysis = L.nub $ filter (/=NotFound) . concatMap (\x -> termAnalysis x inv (Flip False)) $ exps
                               in if null analysis 
                                   then NotFound
                                   else if length analysis > 1
                                         then Complex
                                         else head analysis

termAnalysis :: Term -> String -> InvarBoundSwitch -> [InvarBoundSwitch]
termAnalysis (Mul a b) inv f = termAnalysis a inv f ++ termAnalysis b inv f
termAnalysis (Div a b) inv f = termAnalysis a inv f ++ termAnalysis b inv (flipbound f)
termAnalysis (Neg a) inv f   = termAnalysis a inv (flipbound f) 
termAnalysis (Term a) inv f  = factorAnalysis a inv f

factorAnalysis :: Factor -> String -> InvarBoundSwitch -> [InvarBoundSwitch]
factorAnalysis (Pow a b) inv _ = factorAnalysis a inv Complex ++ factorAnalysis b inv Complex 
factorAnalysis (Value v) inv f = return $ valueAnalysis v inv f

valueAnalysis :: Value -> String -> InvarBoundSwitch -> InvarBoundSwitch
valueAnalysis (Invar v)         s f | s == v     = f
valueAnalysis (Function _ exps) s f              = let fxprs = L.nub $ map (`exprAnalysis` s) exps 
                                                   in if null fxprs 
                                                       then NotFound
                                                       else if length fxprs > 1
                                                             then Complex
                                                             else head fxprs
valueAnalysis (Paren p)         s f              = let an = exprAnalysis p s
                                                   in if f == Flip True 
                                                       then flipbound an 
                                                       else if f == Complex && an /= NotFound 
                                                             then Complex
                                                             else an
valueAnalysis _                 _ _              = NotFound

generateIfStmt' :: IfStmt -> [[String]]
generateIfStmt' (If c (InvarExprList is) Nothing) 
    = let cond = generateCond c in
       init cond : [last cond ++ ":"] : [indent (concatMap generateIExpr is)]

generateIfStmt :: IfStmt -> [String]
generateIfStmt i@(If c (InvarExprList is) _)
    = let ([c,f,b]:ifs) = generateIfStmt' <$> flattenIfStmt i []
          initf         = [c, map ("if "++) f, b]
          conds         = concatMap (\[c,_,_] -> c) $ initf : ifs
      in  L.nub conds ++ (concat (tail initf) ++ concatMap (\[_,i,b] -> (("elif "++) <$> i) ++ b) ifs)


flattenIfStmt :: IfStmt -> [IfStmt] -> [IfStmt]
flattenIfStmt i@(If _ _   Nothing)  is = i : is 
flattenIfStmt   (If c iex (Just i)) is = If c iex Nothing : flattenIfStmt i is 

junction a b condis = 
    let af = init $ generateCond a
        bf = init $ generateCond b
        ac = last $ generateCond a
        bc = last $ generateCond b
    in L.nub (af ++ bf) ++ [ ac ++ " " ++ condis ++ " " ++ bc ]

generateCond :: Cond -> [String]
generateCond (CondOr a b)  = junction a b "or"
generateCond (CondAnd a b) = junction a b "and" 
generateCond (CondNot (Local "True")) =
    ["", "(True)"]
generateCond (CondEven (Invar v)) =
    [v ++ "_Min = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Min\')",
     v ++ "_Max = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Max\')",
     "(even(" ++ v ++ "_Min) and even(" ++ v ++ "_Max))"]
generateCond (CondOdd (Invar v)) =
    [v ++ "_Min = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Min\')",
     v ++ "_Max = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Max\')",
     "(odd(" ++ v ++ "_Min) and odd(" ++ v ++ "_Max))"]
generateCond (CondNot (Invar v)) = 
    [v ++ " = ingrid_obj.get(\'" ++ v ++ "\')",
     "(" ++ v ++ " == False)"]
generateCond (Cond (Invar v) Nothing) = 
    [v ++ " = ingrid_obj.get(\'" ++ v ++ "\')",
     "(" ++ v ++ " == True)"]
generateCond (Cond (Invar v) (Just (CondRel r exp))) = 
    case r of 
        RelLte -> make Min Max
        RelGte -> make Max Min
        RelGt  -> make Max Min
        RelLt  -> make Min Max
        RelEq  -> if containsInvar exp 
                    then generateCond $ CondAnd (Cond (Invar v) (Just (CondRel RelLte exp))) 
                                                (Cond (Invar v) (Just (CondRel RelGte exp)))
                    else makeEq 
    where 
    makeEq = let v_max = v ++ "_Max"
                 v_min = v ++ "_Min"
             in [v_min ++ " = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Min\')",
                 v_max ++ " = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Max\')",
                  "(" ++ v_max ++ "==" ++ v_min ++ " and (" ++ v_min ++ show r ++ exprToSrc exp ++ "))"]
    make m m2 = 
     let invars    = (m2, v, v ++ "_" ++ show m2) : (map (\i -> (m, i, i ++ "_" ++ show m)) . S.toList . getExprInvolves $ exp)
         v'        =  v ++ "_" ++ show m2
         invars'   = map (\(a,b,c) -> (a,c)) invars
         invarmap  = map (\(a,b,c) -> (Invar b, Invar c)) invars
     in (invars >>= 
         \(b, i, name) -> [name ++ " = ingrid_obj.get(\'" ++ i ++ "\', ind=\'" ++ show b ++ "\')"]) 
        ++ [v' ++ " = ingrid_obj.get(\'" ++ v ++ "\', ind=\'" ++ show m2 ++ "\')",
            if not . null $ assertNotUdts invars' 
                then "(" ++ assertNotUdts invars' ++ " and (" ++ v' ++ show r ++ exprToSrc (replaceExprInvar invarmap exp) ++ "))"
                else "(" ++ v' ++ show r ++ exprToSrc (replaceExprInvar invarmap exp) ++ ")"]

invarMappingList :: [Value]
invarMappingList = map (Invar . return) (['A'..'Z'] ++ ['a'..'z'])

getAllIExprInvars :: InvarExpr -> [Value]
getAllIExprInvars = map Invar . S.toList . getInvarExprInvolves

replAllIExprFuncs :: InvarExpr -> [Value] -> (InvarExpr, [(Value, Value)])
replAllIExprFuncs (InvarExpr i (Just (InvarRelExpr r exp))) vals = 
    let (exp', vals') = replAllExprFuncs exp vals True
    in  (InvarExpr i (Just (InvarRelExpr r exp')), vals')

replAllExprFuncs :: Expr -> [Value] -> Bool -> (Expr, [(Value, Value)])
replAllExprFuncs (Expr es) vals p = snd $ foldr (\y (v, (Expr es, out)) -> 
                                    let (t, vs) = replTermFuncs y v p
                                    in (drop (length vs) v, (Expr (es++[t]), out++vs))) (vals, (Expr [], [])) es 

replTermFuncs :: Term -> [Value] -> Bool -> (Term, [(Value, Value)])
replTermFuncs (Div a b) vals p = 
    let (ta, avs) = replTermFuncs a vals p
        (tb, bvs) = replTermFuncs b (drop (length avs) vals) p
    in (Div ta tb, avs ++ bvs)
replTermFuncs (Mul a b) vals p = 
    let (ta, avs) = replTermFuncs a vals p
        (tb, bvs) = replTermFuncs b (drop (length avs) vals) p
    in (Mul ta tb, avs ++ bvs)
replTermFuncs (Neg a) vals p = 
    let (t, v) = replTermFuncs a vals p
    in  (Neg t, v)
replTermFuncs (Term a) vals p = 
    let (f, vs) = replFactorFuncs a vals p
    in  (Term f, vs)

replFactorFuncs :: Factor -> [Value] -> Bool -> (Factor, [(Value, Value)])
replFactorFuncs (Pow a b)                vals  p = 
    let (fa, avs) = replFactorFuncs a vals True
        (fb, bvs) = replFactorFuncs b (drop (length avs) vals) False
    in (Pow fa fb, avs ++ bvs)
replFactorFuncs (Value f@(Function _ _)) (v:_) _ = (Value v, [(v, f)])
replFactorFuncs (Value (Paren expr))     vals  p = 
    let (p', vs') = replAllExprFuncs expr vals p
    in (Value $ Paren p', vs')
replFactorFuncs (Value n@(Number _))     (v:_) p = 
    if p then (Value v, [(v, n)]) else (Value n, [])
replFactorFuncs v                        _     _ = (v, [])


replaceAllInvar :: [(Value, Value)] -> Theorem -> Theorem
replaceAllInvar m (IExpr i) = IExpr $ replaceIExprInvar m i

replaceIExprInvar :: [(Value, Value)] -> InvarExpr -> InvarExpr
replaceIExprInvar m (InvarExpr i (Just (InvarRelExpr r exp))) = 
  InvarExpr (case lookup i m of 
              (Just new) -> new
              _          -> i) (Just $ InvarRelExpr r (replaceExprInvar m exp))

replaceExprInvar :: [(Value, Value)] -> Expr -> Expr
replaceExprInvar m (Expr xs) = Expr $ map (replaceTermInvar m) xs
              
replaceTermInvar :: [(Value, Value)] -> Term -> Term
replaceTermInvar m (Div a b) = Div (replaceTermInvar m a) (replaceTermInvar m b)
replaceTermInvar m (Mul a b) = Mul (replaceTermInvar m a) (replaceTermInvar m b)
replaceTermInvar m (Term f)  = Term $ replaceFactorInvar m f
replaceTermInvar m (Neg a)   = Neg $ replaceTermInvar m a

replaceFactorInvar :: [(Value, Value)] -> Factor -> Factor
replaceFactorInvar m (Pow a b) = Pow (replaceFactorInvar m a) (replaceFactorInvar m b)
replaceFactorInvar m (Value v) = Value $ replaceValueInvar m v

replaceValueInvar :: [(Value, Value)] -> Value -> Value
replaceValueInvar m i@(Invar _)     = case lookup i m of
                                        Just v -> v
                                        _      -> i
replaceValueInvar m (Function f es) = Function f $ map (replaceExprInvar m) es
replaceValueInvar m (Paren e)       = Paren . replaceExprInvar m $ e
replaceValueInvar _ v               = v
                                           
generateIneq :: [Theorem] -> IO [Theorem]
generateIneq = 
    fmap concat . mapM (\t ->
          case t of
           (IExpr e)  -> genIExprIneq e
           (IfStmt i) -> return . IfStmt <$> genIfStmtIneq i
        )

genIfStmtIneq :: IfStmt -> IO IfStmt
genIfStmtIneq (If c (InvarExprList iexpl) Nothing) = 
    fmap ((\il -> If c (InvarExprList il) Nothing) . concat) . mapM genInvarExprIneq $ iexpl
genIfStmtIneq (If c (InvarExprList iexpl) (Just i)) = 
    let elsestmt = genIfStmtIneq i
        ifstmt   = If c (InvarExprList iexpl) Nothing
    in liftM2 nestif elsestmt (genIfStmtIneq ifstmt)
    where
    nestif :: IfStmt -> IfStmt -> IfStmt
    nestif e (If c iex _) = If c iex (Just e)

genInvarExprIneq :: InvarExpr -> IO [InvarExpr]
genInvarExprIneq = fmap (map extractInvarExprIO) . genIExprIneq
        where
        extractInvarExprIO :: Theorem -> InvarExpr
        extractInvarExprIO (IExpr i) = i

genIExprIneq :: InvarExpr -> IO [Theorem]
genIExprIneq e@(InvarExpr _ (Just (InvarRelExpr _ _))) =
        let  (InvarExpr (Invar v) (Just (InvarRelExpr rel exp))) = replaceIExprInvar invar_map func_map
             (func_map, func_remap)                            = replAllIExprFuncs e invarMappingList
             invar_maplist                                     = drop (length func_remap) invarMappingList
             invar_map                                         = zip (getAllIExprInvars e) invar_maplist 
             invar_remap                                       = map (\(a,b) -> (b,a)) invar_map
             inequality                                        = v ++ show rel ++ exprToSrc exp
             invars                                            = v : S.toList (getExprInvolves exp)
        in fmap (map (replaceAllInvar func_remap . replaceAllInvar invar_remap) . theoremParser . lexer . concat) . sequence $ 
               invars
                >>= \inv -> return $
                               fix (\loop c ->
                               do (Just stdin, Just stdout, _, solver) <- createProcess (proc "python2" ["solver.py"]) 
                                                                           { std_in = CreatePipe, std_out = CreatePipe }
                                  hPutStrLn stdin $ "{\"invariants\":" ++ show invars ++ 
                                                    ", \"target_invariant\":" ++ show inv ++ 
                                                    ", \"inequality\":" ++ show inequality ++ "}"
                                  hFlush stdin
                                  ec <- waitForProcess solver
                                  case ec of
                                   (ExitFailure _) -> if c < 10 then loop (c+1) else hGetLine stdout
                                   _               -> hGetLine stdout) 0
genIExprIneq e = return [IExpr e]
               
containsInvar :: Expr -> Bool
containsInvar (Expr es) = any termHasInvar es
    where 
    termHasInvar (Div a b)       = termHasInvar a || termHasInvar b 
    termHasInvar (Mul a b)       = termHasInvar a || termHasInvar b
    termHasInvar (Term f)        = factorHasInvar f 
    termHasInvar (Neg a)         = termHasInvar a
    factorHasInvar (Pow a b)     = factorHasInvar a || factorHasInvar b
    factorHasInvar (Value v)     = valueHasInvar v
    valueHasInvar (Invar _)      = True
    valueHasInvar (Function _ e) = any containsInvar e
    valueHasInvar (Paren e)      = containsInvar e
    valueHasInvar _              = False

containsFunc :: Expr -> Bool
containsFunc (Expr es) = any termHasFunc es
    where 
    termHasFunc (Div a b)       = termHasFunc a || termHasFunc b 
    termHasFunc (Mul a b)       = termHasFunc a || termHasFunc b
    termHasFunc (Term f)        = factorHasFunc f 
    termHasFunc (Neg a)         = termHasFunc a
    factorHasFunc (Pow a b)     = factorHasFunc a || factorHasFunc b
    factorHasFunc (Value v)     = valueHasFunc v
    valueHasFunc (Function _ _) = True
    valueHasFunc (Paren e)      = containsFunc e
    valueHasFunc _              = False
