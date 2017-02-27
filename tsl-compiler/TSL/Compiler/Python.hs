{-# LANGUAGE OverloadedStrings #-}
module TSL.Compiler.Python (
                    generateSympyIneq,
                    generatePythonClass
                    ) where

{- All python generation and related functions go in here
 - -}

import qualified Control.Exception        as E
import qualified Data.Text                as T

import           Control.Monad            (liftM2, replicateM)
import           Control.Monad.Fix        (fix)
import qualified CPython                  as Py
import qualified CPython.Constants        as Py
import qualified CPython.Protocols.Object as Py
import qualified CPython.Types            as Py
import qualified CPython.Types.Dictionary as PyDict
import qualified CPython.Types.Exception  as Py
import qualified CPython.Types.Module     as Py
import qualified CPython.Types.Unicode    as Py

import qualified Data.List                as L
import qualified Data.Set                 as S

import           Debug.Trace

import           TSL.AST.AST
import           TSL.AST.Manipulation
import           TSL.Compiler.Analysis
import           TSL.Compiler.Types
import           TSL.Parser.Parser

indent :: [String] -> [String]
indent = map ("\t" ++)

assertNotUdts :: [(Bound, String)] -> String
assertNotUdts = L.intercalate " and " . map (\(_,i) -> i ++ " != \'undt\'") . filter (\(b,_) -> b == Max)

-- | Body
generatePythonClass :: TSLTheorem -> [String]
generatePythonClass (TSLTheorem (TSLInputTheorem name text disp idnum) ts)  =
       (("class " ++ name ++ "(Theorem):"):) . concatMap indent $
             [("def __init__(self):" :) $
                indent ["super(" ++ name ++ ", self).__init__(" ++ L.intercalate ", " [show idnum, show text, show disp] ++")"]
             ,("def involves(self, str_invar):" :) $
                indent ["return str_invar in " ++ show (L.nub . concatMap getInvolves $ ts)]
             , ("def run(self, ingrid_obj):" : concatMap (indent . generatePython) ts) ++ ["\treturn"]]

generatePython :: Theorem a -> [String]
generatePython NullBody = []
generatePython i        = generateCode i

generateCode :: Theorem a -> [String]
generateCode (InvarExpr (Invar v) Nothing) = return ("ingrid_obj.set(\'" ++ v ++ "\', True)")
generateCode (ExprF "not" (Invar v)) = return ("ingrid_obj.set(\'" ++ v ++ "\', False)")
generateCode (ExprF "undefined" (Invar v)) = 
    [ v ++ "_Min = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Min\')" 
    , "ingrid_obj.set(\'" ++ v ++ "\', \'undt\', ind=\'Min\')"
    ]
generateCode (ExprF "even" (Invar v)) =
    [ v ++ "_Max = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Max\')-1"
    , v ++ "_Min = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Min\')+1"
    , "if even(" ++ v ++ "_Max):"
    , "\tingrid_obj.set(\'" ++ v ++ "\', ind=\'Max\')"
    , "if even(" ++ v ++ "_Min):"
    , "\tingrid_obj.set(\'" ++ v ++ "\', ind=\'Min\')"]
generateCode (ExprF "odd" (Invar v)) =
    [ v ++ "_Max = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Max\')-1"
    , v ++ "_Min = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Min\')+1"
    , "if odd(" ++ v ++ "_Max):"
    , "\tingrid_obj.set(\'" ++ v ++ "\', ind=\'Max\')"
    , "if odd(" ++ v ++ "_Min):"
    , "\tingrid_obj.set(\'" ++ v ++ "\', ind=\'Min\')"]
generateCode (InvarExpr (Invar v) (Just (RelExpr r exp))) =
    case r of
        RelLte -> make Max
        RelGte -> make Min
        RelEq  -> generateCode (InvarExpr (Invar v) (Just (RelExpr RelLte exp)))
                    ++
                  generateCode (InvarExpr (Invar v) (Just (RelExpr RelGte exp)))
        _      -> [""]
    where
    make m =
      let invars = map (\i -> (swap m (exprAnalysis exp i), i)) . S.toList . getExprInvolves $ exp
      in
         if any (\(_,i) -> exprAnalysis exp i == Complex) invars
            then "result = []" : iterateBounds invars m
            else setBound invars m

    resultList m = [ "if len(result) > 0:","\tingrid_obj.set(\'" ++ v ++ "\', " ++ (if m == Max then "max" else "min") ++ "(result), ind=\'" ++ show m ++ "\')" ]

    result m = [ "try:"
               , "\tingrid_obj.set(\'" ++ v ++ "\', " ++ exprToSrc exp ++ ", ind=\'" ++ show m ++ "\')"
               , "except:"
               , "\tpass"]

    setTryBound invars =
            (invars >>=
                \(b, i) -> [i ++ " = ingrid_obj.get(\'" ++ i ++ "\', ind=\'" ++ show b ++ "\')"])
                            ++ if not . null $ assertNotUdts invars
                                then ("if " ++ assertNotUdts invars ++ ":") : indent ["try:","\tresult.append(" ++ exprToSrc exp ++ ")","except:","\tpass"]
                                else ["try:","\tresult.append(" ++ exprToSrc exp ++ ")","except:","\tpass"]
    setBound invars m =
            (invars >>=
                \(b, i) -> [i ++ " = ingrid_obj.get(\'" ++ i ++ "\', ind=\'" ++ show b ++ "\')"])
                            ++ if not . null $ assertNotUdts invars then ("if " ++ assertNotUdts invars ++ ":") : indent (result m) else result m
    iterateBounds ivars m = let  cplx_vars = filter (\(b,i) -> exprAnalysis exp i == Complex) ivars
                                 reg_vars  = filter (\(b,i) -> exprAnalysis exp i /= Complex) ivars
                                 cplx_perms = map (\x -> zipWith (\b (_,i) -> (b,i)) x cplx_vars ++ reg_vars) (replicateM (length cplx_vars) [Min,Max])
                            in concatMap setTryBound cplx_perms ++ resultList m
generateCode i@(If c (ExprList is) _)
    = let ([c,f,b]:ifs) = generateIfStmt' <$> flattenIfStmt i []
          initf         = [c, map ("if "++) f, b]
          conds         = concatMap (\[c,_,_] -> c) $ initf : ifs
      in  L.nub conds ++ (concat (tail initf) ++ concatMap (\[_,i,b] -> (("elif "++) <$> i) ++ b) ifs)
generateCode _ = []

generateIfStmt' :: Theorem a -> [[String]]
generateIfStmt' (If c (ExprList is) Nothing)
    = let cond = generateCond c in
       init cond : [last cond ++ ":"] : [indent (concatMap generatePython is)]

flattenIfStmt :: Theorem a -> [IfStmt] -> [IfStmt]
flattenIfStmt i@(If _ _   Nothing)  is = i : is
flattenIfStmt   (If c iex (Just i)) is = If c iex Nothing : flattenIfStmt i is

junction a b condis =
    let af = init $ generateCond a
        bf = init $ generateCond b
        ac = last $ generateCond a
        bc = last $ generateCond b
    in L.nub (af ++ bf) ++ [ "(" ++ ac ++ " " ++ condis ++ " " ++ bc ++ ")" ]

generateCond :: Theorem a -> [String]
generateCond (Or a b)  = junction a b "or"
generateCond (And a b) = junction a b "and"
generateCond (CondSpecF "isfalse" exp) =
    let setconds = foldr1 CondAnd . map (CondSpec "isset" . Invar) $ involves
        involves = S.toList $ getExprInvolves exp
    in generateCond setconds
generateCond (CondSpecF "istrue" exp) =
    let setconds = foldr1 CondAnd . map (CondSpec "isset" . Invar) $ involves
        involves = S.toList $ getExprInvolves exp
    in generateCond setconds
generateCond (CondSpec "undefined" (Invar v)) =
    [ v ++ "_Min = ingrid_obj.get(\'" ++ v ++ "\', ind = \'Min\')",
     "(" ++ v ++ "_Min == \'undt\')"]
generateCond (CondSpec "defined" (Invar v)) =
    [ v ++ "_Max = ingrid_obj.get(\'" ++ v ++ "\', ind = \'Max\')",
     "(" ++ v ++ "_Max != \'undt\')"]
generateCond (CondSpec "isset" (Invar v)) =
    [v ++ "_Min = ingrid_obj.get(\'" ++ v ++ "\', ind = \'Min\')",
     v ++ "_Max = ingrid_obj.get(\'" ++ v ++ "\', ind = \'Max\')",
     "(" ++ v ++ "_Min" ++ " == " ++ v ++ "_Max)"]
generateCond (CondSpec "not" (Local "True")) =
    ["", "(True)"]
generateCond (CondSpec "even" (Invar v)) =
    [v ++ "_Min = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Min\')",
     v ++ "_Max = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Max\')",
     "(even(" ++ v ++ "_Min) and even(" ++ v ++ "_Max))"]
generateCond (CondSpec "odd" (Invar v)) =
    [v ++ "_Min = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Min\')",
     v ++ "_Max = ingrid_obj.get(\'" ++ v ++ "\', ind=\'Max\')",
     "(odd(" ++ v ++ "_Min) and odd(" ++ v ++ "_Max))"]
generateCond (CondSpec "not" (Invar v)) =
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
     let invars    = (m2, v, v ++ "_" ++ show m2) : (map (\i ->
                                                    let m' = (swap m $ exprAnalysis exp i)
                                                    in (m', i, i ++ "_" ++ show m')) . S.toList . getExprInvolves $ exp)
         v'        =  v ++ "_" ++ show m2
         invars'   = map (\(a,b,c) -> (a,c)) invars
         invarmap  = map (\(a,b,c) -> (Invar b, Invar c)) invars
     in (invars >>=
         \(b, i, name) -> [name ++ " = ingrid_obj.get(\'" ++ i ++ "\', ind=\'" ++ show b ++ "\')"])
        ++ [v' ++ " = ingrid_obj.get(\'" ++ v ++ "\', ind=\'" ++ show m2 ++ "\')",
            if not . null $ assertNotUdts invars'
                then "(" ++ assertNotUdts invars' ++ " and (" ++ v' ++ show r ++ exprToSrc (replaceExprInvar invarmap exp) ++ "))"
                else "(" ++ v' ++ show r ++ exprToSrc (replaceExprInvar invarmap exp) ++ ")"]

generateSympyIneq :: [Theorem a] -> IO [Theorem a]
generateSympyIneq =
    fmap concat . mapM (\t ->
          case t of
           e@(InvarExpr _ _)  -> genIExprIneq e
           i@(IfStmt _ _ _) -> return . IfStmt <$> genIfStmtIneq i
           t'         -> return [t']
        )

genIfStmtIneq :: Theorem a -> IO (Theorem a)
genIfStmtIneq (If c (ExprList iexpl) Nothing) =
    fmap (\il -> If c (ExprList il) Nothing) . generateSympyIneq $ iexpl
genIfStmtIneq (If c (ExprList iexpl) (Just i)) =
    let elsestmt = genIfStmtIneq i
        ifstmt   = If c (ExprList iexpl) Nothing
    in liftM2 nestif elsestmt (genIfStmtIneq ifstmt)
    where
    nestif :: IfStmt -> IfStmt -> IfStmt
    nestif e (If c iex _) = If c iex (Just e)

-- genInvarExprIneq :: Theorem a -> IO [Theorem a]
-- genInvarExprIneq = fmap (map extractInvarExprIO) . genIExprIneq
--         where
--         extractInvarExprIO :: Theorem -> InvarExpr
--         extractInvarExprIO (IExpr i) = i

genIExprIneq :: Theorem a -> IO [Theorem a]
genIExprIneq e@(InvarExpr _ (Just (RelExpr _ _))) =
        let  (InvarExpr (Invar v) (Just (RelExpr rel exp))) = func_map
             (func_map, func_remap)                            = replAllFuncs e invarMappingList
             rationalFlag                                      = not $ containsFunc exp
             inequality                                        = exprToSrc exp
             lhs                                               = v
             relation                                          = show rel
             invars                                            = v : S.toList (getInvolves exp)
        in fmap (map (replaceAllInvar func_remap) . theoremParser . lexer . (\i -> trace i i) . concat) . sequence $
               invars
                >>= \inv -> return $
                   do Py.initialize
                      equation <- Py.toUnicode . T.pack $ inequality
                      variables <- Py.toList =<< map Py.toObject <$> mapM (Py.toUnicode . T.pack) invars
                      lhs <- Py.toUnicode . T.pack $ lhs
                      rel <- Py.toUnicode . T.pack $ relation
                      target  <- Py.toUnicode . T.pack $ inv
                      ms <- Py.importModule "mystic.symbolic"
                      solver <- Py.getAttribute ms =<< Py.toUnicode "solve_ingrid"
                      rationalval <- if rationalFlag then Py.true else Py.false
                      pyout <- Py.callArgs solver [Py.toObject lhs, Py.toObject rel, Py.toObject equation, Py.toObject variables, Py.toObject target, Py.toObject rationalval]
                      rewrite <- Py.cast pyout :: IO (Maybe Py.Unicode)
                      case rewrite of
                       (Just eqn) -> (++";") . T.unpack <$> Py.fromUnicode eqn
                       _          -> return ""
genIExprIneq e = return [IExpr e]
