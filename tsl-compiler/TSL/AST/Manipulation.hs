module TSL.AST.Manipulation where

import qualified Data.List as L
import           Data.Set  (Set)
import qualified Data.Set  as S

import           TSL.AST.AST

-- | Begin helper functions
invarMappingList :: [Value]
invarMappingList = map (Invar . return) (filter (/='I') $ ['A'..'Z'] ++ ['a'..'z'])

getAllIExprInvars :: InvarExpr -> [Value]
getAllIExprInvars = map Invar . S.toList . getInvarExprInvolves
--- | End helper functions

-- | Begin getInvolves
getInvolves :: Theorem -> [String]
getInvolves (IExpr i)  = S.toList $ getInvarExprInvolves i
getInvolves (IfStmt i) = S.toList $ getIfStmtInvolves i
getInvolves NullBody   = []

getInvarExprInvolves :: InvarExpr -> Set String
getInvarExprInvolves (InvarOr a b)          = S.union (getInvarExprInvolves a) (getInvarExprInvolves b)
getInvarExprInvolves (InvarAnd a b)         = S.union (getInvarExprInvolves a) (getInvarExprInvolves b)
getInvarExprInvolves (InvarExpr a Nothing)  = getValueInvolves a
getInvarExprInvolves (InvarExpr a (Just b)) = S.union (getValueInvolves a) (getInvarRelExprInvolves b)
getInvarExprInvolves (InvarExprNot a)       = getValueInvolves a
getInvarExprInvolves (InvarExprEven a)      = getValueInvolves a
getInvarExprInvolves (InvarExprOdd a)       = getValueInvolves a
getInvarExprInvolves (InvarExprUndefined a) = getValueInvolves a

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
getInvarExprListInvolves (InvarExprList l) = foldr (flip (\r -> S.union r . S.fromList . getInvolves)) S.empty l

getCondInvolves :: Cond -> Set String
getCondInvolves (CondOr a b)        = S.union (getCondInvolves a) (getCondInvolves b)
getCondInvolves (CondAnd a b)       = S.union (getCondInvolves a) (getCondInvolves b)
getCondInvolves (CondSpec _ v)      = getValueInvolves v
getCondInvolves (CondSpecF _ e)      = getExprInvolves e
getCondInvolves (Cond ex (Just cr)) = S.union (getValueInvolves ex) (getCondRelInvolves cr)
getCondInvolves (Cond ex Nothing)   = getValueInvolves ex

getCondRelInvolves :: CondRel -> Set String
getCondRelInvolves (CondRel _ e) = getExprInvolves e
---  | End getInvolves

-- | Begin exprToSrc
exprToSrc :: Expr -> String
exprToSrc (Expr ts) = foldl (\s t -> case t of
                                     (Neg _) -> s ++ termToSrc t
                                     _       -> s ++ (if null s then "" else "+") ++ termToSrc t) "" ts

termToSrc :: Term -> String
termToSrc (Mul a b) = termToSrc a ++ "*" ++ termToSrc b
termToSrc (Div a b) = termToSrc a ++ "/" ++ termToSrc b
termToSrc (Neg a)   = "-(" ++ termToSrc a ++ ")"
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
--- | End exprToSrc

-- | Begin contains
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
--- | End contains

-- | Begin replace Invars
replaceAllInvar :: [(Value, Value)] -> Theorem -> Theorem
replaceAllInvar _  NullBody = NullBody
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
--- | End replace

-- | Begin replace Functions
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
replFactorFuncs fv@(Value f@(Function fun _)) (v:_) _ | fun `L.elem` solveableFunctions
                                                                  = (fv, [])
                                                      | otherwise = (Value v, [(v, f)])
replFactorFuncs (Value (Paren expr))     vals  p =
    let (p', vs') = replAllExprFuncs expr vals p
    in (Value $ Paren p', vs')
replFactorFuncs (Value n@(Number _))     (v:_) p =
    {- if p then (Value v, [(v, n)]) else -} (Value n, [])
replFactorFuncs v                        _     _ = (v, [])
--- | End replace Functions

