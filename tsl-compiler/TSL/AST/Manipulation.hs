{-# LANGUAGE DataKinds #-}
module TSL.AST.Manipulation where

import qualified Data.List   as L

import           TSL.AST.AST
import Data.Maybe (fromMaybe)

-- | Begin helper functions
invarMappingList :: [String]
invarMappingList = map (:[]) (filter (/='I') $ ['A'..'Z'] ++ ['a'..'z'])

getAllInvars :: Fix Theorem -> [Fix Theorem]
getAllInvars = map (Fx . Invar) . getInvolves
--- | End helper functions

getInvolves :: Fix Theorem -> [String]
getInvolves = L.nub . cata getInvolves'

getInvolves' :: Theorem [String] -> [String]
getInvolves' (Invar a) = return a
getInvolves' (InvarExpr a b) = a ++ fromMaybe [] b
getInvolves' (If a b c) = a ++ b ++ fromMaybe [] c
getInvolves' (Cond a b) = a ++ fromMaybe [] b
getInvolves' (RelExpr a b) = a ++ b
getInvolves' (ExprList as) = concat as
getInvolves' (Expr as) = concat as
getInvolves' (ExprF _ a) = a
getInvolves' (Or a b) = a ++ b
getInvolves' (And a b) = a ++ b
getInvolves' (Mul a b) = a ++ b
getInvolves' (Div a b) = a ++ b
getInvolves' (Pow a b) = a ++ b
getInvolves' (Paren a) = a 
getInvolves' (Neg a) = a 
getInvolves' (Function _ as) = concat as
getInvolves' _         = []

theoremToSrc :: Fix Theorem -> String
theoremToSrc = cata theoremToSrc' 

theoremToSrc' :: Theorem String -> String
theoremToSrc' (Relation a)          = show a
theoremToSrc' (RelExpr a b)         = a ++ b
theoremToSrc' (Cond a b)            = a ++ fromMaybe [] b
theoremToSrc' (InvarExpr a b)       = a ++ fromMaybe [] b ++ ";\n"
theoremToSrc' (If a b c)            =
        concat ["if ", a, " then \n{\n", 
                    unlines (map ("    "++) (lines b)), "\n}",
                    maybe [] (" else "++) c, 
                    ";\n"]
theoremToSrc' (ExprList as)         = L.intercalate ",\n" . map (("    "++) . filter (/=';')) $ as
theoremToSrc' (Expr (t:ts))         = t ++ concatMap (\s -> 
                                                case s of 
                                                  ('-':_) -> s
                                                  _       -> '+':s) ts
theoremToSrc' (Mul a b)             = a ++ "*" ++ b
theoremToSrc' (Div a b)             = a ++ "/" ++ b
theoremToSrc' (Pow a b)             = a ++ "**" ++ b
theoremToSrc' (Neg a)               = "-(" ++ a ++ ")"
theoremToSrc' (Number a)            = show a
theoremToSrc' (Function "sqrt" es) = "(" ++ L.intercalate ", " es ++ ")**(1.0/2.0)"
theoremToSrc' (Function s es)      = s ++ "(" ++ L.intercalate ", " es ++ ")"
theoremToSrc' (Local s)            = s
theoremToSrc' (Invar s)            = s
theoremToSrc' (Paren e)            = e
theoremToSrc' _                    = ""

extractLetStatements :: [Fix Theorem] -> [(String, Fix Theorem)]
extractLetStatements = foldr (\x ys ->
                                case x of
                                    (Fx (Let (Fx (Invar s)) e)) -> (s,e):ys
                                    _                           -> ys) [] 

containsFunc :: Fix Theorem -> Bool
containsFunc = cata containsFunc'

containsFunc' :: Theorem Bool -> Bool
containsFunc' (If a b c) = a || b || fromMaybe False c
containsFunc' (InvarExpr a b) = a || fromMaybe False b
containsFunc' (Cond a b)      =  a || fromMaybe False b
containsFunc' (ExprList as)   = or as
containsFunc' (ExprF _ a)     = a
containsFunc' (RelExpr a b)   = a || b
containsFunc' (Expr as)       = or as
containsFunc' (Or a b)        = a || b
containsFunc' (And a b)       = a || b
containsFunc' (Mul a b)       = a || b
containsFunc' (Neg a)         = a
containsFunc' (Pow a b)       = a || b
containsFunc' (Function _ _)  = True
containsFunc' (Paren a)       = a
containsFunc' _               = False

containsInvar :: Fix Theorem -> Bool
containsInvar = cata containsInvar' 

containsInvar' :: Theorem Bool -> Bool
containsInvar' (If a b c) = a || b || fromMaybe False c
containsInvar' (InvarExpr a b) = a || fromMaybe False b
containsInvar' (Cond a b)      =  a || fromMaybe False b
containsInvar' (ExprList as)   = or as
containsInvar' (ExprF _ a)     = a
containsInvar' (RelExpr a b)   = a || b
containsInvar' (Expr as)       = or as
containsInvar' (Or a b)        = a || b
containsInvar' (And a b)       = a || b
containsInvar' (Mul a b)       = a || b
containsInvar' (Neg a)         = a
containsInvar' (Pow a b)       = a || b
containsInvar' (Function _ _)  = True
containsInvar' (Paren a)       = a
containsInvar' _               = False

replaceAllInvar :: [(String, Fix Theorem)] -> Fix Theorem -> Fix Theorem
replaceAllInvar m = cata (replaceAllInvar' m)

replaceAllInvar' :: [(String, Fix Theorem)] -> Theorem (Fix Theorem) -> Fix Theorem 
replaceAllInvar' m (Invar i)       = case lookup i m of
                                        Just v -> v
                                        _      -> Fx $ Invar i
replaceAllInvar' m v               = Fx v

replaceAllFuncs :: Fix Theorem -> (Fix Theorem, [(String, Fix Theorem)])
replaceAllFuncs f = 
    let (exp, expmap)       = cata replaceAllFuncs' f
        (expmap', finalmap) = unzip $ zipWith  (\(a,b) s -> ((a,Fx $ Invar s),(s,b))) expmap invarMappingList 
    in (replaceAllInvar expmap' exp, finalmap)


replaceAllFuncs' :: Theorem (Fix Theorem, [(String, Fix Theorem)]) -> (Fix Theorem, [(String, Fix Theorem)])
replaceAllFuncs' (InvarExpr (a,a') mb)       = case mb of
                                            Just (b,b') -> (Fx $ InvarExpr a (Just b), a'++b') 
                                            _           -> (Fx $ InvarExpr a Nothing, a')
replaceAllFuncs' (RelExpr (r,r') (p,p'))        = (Fx $ RelExpr r p, r'++p')
replaceAllFuncs' (Expr es)                       = let (es'',v) = foldr (\(e,t) (es',ts') -> (e:es', t++ts')) ([],[]) es
                                               in (Fx $ Expr es'', v)
replaceAllFuncs' (Div (a,a') (b,b'))             = (Fx $ Div a b, a'++b')
replaceAllFuncs' (Mul (a,a') (b,b'))             = (Fx $ Mul a b, a'++b')
replaceAllFuncs' (Neg (a,a'))                    = (Fx $ Neg a, a')
replaceAllFuncs' (Pow (a,a') (b,b'))             = (Fx $ Pow a b, a'++b')
replaceAllFuncs' (Function fun es) | fun `L.elem` solveableFunctions
                                             = let (es'',v) = foldr (\(e,t) (es',ts') -> (e:es', t++ts')) ([],[]) es
                                               in (Fx $ Function fun es'', v)
                                 | otherwise = let (es'',v) = foldr (\(e,t) (es',ts') -> (e:es', t++ts')) ([],[]) es
                                                   val      = Fx $ Function fun es''
                                               in (Fx $ Invar (theoremToSrc val), (theoremToSrc val, val):v)
replaceAllFuncs' (Paren (a,a'))             = (Fx $ Paren a, a')
replaceAllFuncs' (Invar a)                  = (Fx $ Invar a, [])
replaceAllFuncs' (Relation a)               = (Fx $ Relation a, [])
replaceAllFuncs' (Number a)                 = (Fx $ Number a, [])
