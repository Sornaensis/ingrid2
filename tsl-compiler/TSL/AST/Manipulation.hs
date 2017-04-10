{-# LANGUAGE DataKinds         #-}
{-# LANGUAGE FlexibleInstances #-}
module TSL.AST.Manipulation where

import qualified Data.List   as L

import           Data.Maybe  (fromMaybe)
import           Data.Monoid
import           TSL.AST.AST

import           Debug.Trace

-- | Begin helper functions
invarMappingList :: [String]
invarMappingList = map (:[]) (filter (/='I') $ ['A'..'Z'] ++ ['a'..'z'])

getAllInvars :: Fix Theorem -> [Fix Theorem]
getAllInvars = map (Fx . Invar) . getInvolves
--- | End helper functions
isFunction :: Fix Theorem -> Bool
isFunction (Fx (Function _ _)) = True
isFunction _                   = False

eqIFns :: Fix Theorem -> Fix Theorem -> Bool
eqIFns (Fx (Function a [Fx (Invar i)])) (Fx (Function b [Fx (Invar j)])) = a == b && i == j
eqIFns _ _ = False

isLetStatement :: Fix Theorem -> Bool
isLetStatement (Fx (Let _ _)) = True
isLetStatement _              = False

checkFunctions :: Fix Theorem -> Bool
checkFunctions = cata checkFunctions'

checkFunctions' :: Theorem Bool -> Bool
checkFunctions' (Let a b)       = a && b
checkFunctions' (InvarExpr a b) = a && fromMaybe True b
checkFunctions' (If a b c)      = a && b && fromMaybe True c
checkFunctions' (Cond a b)      = a && fromMaybe True b
checkFunctions' (RelExpr a b)   = a && b
checkFunctions' (ExprList as)   = and as
checkFunctions' (Expr as)       = and as
checkFunctions' (ExprF _ a)     = a
checkFunctions' (Or a b)        = a && b
checkFunctions' (And a b)       = a && b
checkFunctions' (Mul a b)       = a && b
checkFunctions' (Div a b)       = a && b
checkFunctions' (Pow a b)       = a && b
checkFunctions' (Paren a)       = a
checkFunctions' (Neg a)         = a
checkFunctions' (Function f as) | Just (min, max) <- lookup f arityOfFns
                                    = let len = length as
                                      in  len <= max && len >= min
                                | Nothing <- lookup f arityOfFns
                                    = False
checkFunctions' _               = True

-- checkNakedInvars :: Fix Theorem -> Bool
-- checkNakedInvars l = case cata checkNakedInvars' l of
--                         Naked -> True
--                         _     -> False

-- data NakedInvar = Naked | Expr | NoNaked deriving Eq

-- instance Monoid NakedInvar where
--     mempty = NoNaked
--     Naked `mappend` _     = Expr
--     _     `mappend` Naked = Expr

-- checkNakedInvars' :: Fix (NakedInvar) -> NakedInvar
-- checkNakedInvars' (Invar a) = Naked
-- checkNakedInvars' (InvarExpr a b) = a <> fromMaybe NoNaked b
-- checkNakedInvars' (If a b c) = a <> b <> fromMaybe NoNaked c
-- checkNakedInvars' (Cond a b) = a <> fromMaybe False b
-- checkNakedInvars' (RelExpr a b) = a <> b
-- checkNakedInvars' (ExprList as) = any as
-- checkNakedInvars' (Expr as) = any as
-- checkNakedInvars' (ExprF _ a) = a
-- checkNakedInvars' (Or a b) = a <> b
-- checkNakedInvars' (And a b) = a <> b
-- checkNakedInvars' (Mul a b) = a <> b
-- checkNakedInvars' (Div a b) = a <> b
-- checkNakedInvars' (Pow a b) = a <> b
-- checkNakedInvars' (Paren a) = a
-- checkNakedInvars' (Neg a) = a
-- checkNakedInvars' (Function s [Naked]) | s == "minb" || s == "maxb" = NoNaked
--                                        | s == "minb" || s == "maxb" = Naked
-- checkNakedInvars' (Function _ as)  = any as
-- checkNakedInvars' _         = NoNaked

getLocals :: Fix Theorem -> [String]
getLocals = L.nub . cata getLocals'

getLocals' :: Theorem [String] -> [String]
getLocals' (Local a) = return a
getLocals' (InvarExpr a b) = a ++ fromMaybe [] b
getLocals' (If a b c) = a ++ b ++ fromMaybe [] c
getLocals' (Cond a b) = a ++ fromMaybe [] b
getLocals' (RelExpr a b) = a ++ b
getLocals' (ExprList as) = concat as
getLocals' (Expr as) = concat as
getLocals' (ExprF _ a) = a
getLocals' (Or a b) = a ++ b
getLocals' (And a b) = a ++ b
getLocals' (Mul a b) = a ++ b
getLocals' (Div a b) = a ++ b
getLocals' (Pow a b) = a ++ b
getLocals' (Paren a) = a
getLocals' (Neg a) = a
getLocals' (Function _ as) = concat as
getLocals' _         = []

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
theoremToSrc' (Let a b)             = "let " ++ a ++ " = " ++ b
theoremToSrc' (Relation a)          = show a
theoremToSrc' (RelExpr a b)         = " " ++ a ++ " " ++ b
theoremToSrc' (Cond a b)            = a ++ fromMaybe [] b
theoremToSrc' (InvarExpr a b)       = a ++ fromMaybe [] b
theoremToSrc' (If a b c)            =
    case a of
        "not Local True" ->
           concat [" \n{\n",
                       init $ unlines (map ("    "++) (lines b)), "\n}",
                       maybe [] ("\nelse "++) c] --,
                       --";\n"]
        _            ->
           concat ["if ", a, " then \n{\n",
                       init $ unlines (map ("    "++) (lines b)), "\n}",
                       maybe [] ("\nelse "++) c] --,
                       --";\n"]
theoremToSrc' (ExprF s a)           = s ++ (if null a then "" else " " ++ a)
theoremToSrc' (ExprList as)         = L.intercalate ",\n" . filter (not . null) $ as
theoremToSrc' (Expr (t:ts))         = t ++ concatMap (\s ->
                                                case s of
                                                  ('-':_) -> s
                                                  _       -> '+':s) ts
theoremToSrc' (Or a b)              = a ++ " or " ++ b
theoremToSrc' (And a b)             = a ++ " and " ++ b
theoremToSrc' (Mul a b)             = a ++ "*" ++ b
theoremToSrc' (Div a b)             = a ++ "/" ++ b
theoremToSrc' (Pow a b)             = a ++ "**" ++ b
theoremToSrc' (Neg a)               = "-(" ++ a ++ ")"
theoremToSrc' (Number a)            = show a
-- theoremToSrc' (Function "sqrt" es) = "(" ++ L.intercalate ", " es ++ ")**(1.0/2.0)"
theoremToSrc' (Function s es)      = s ++ "(" ++ L.intercalate ", " es ++ ")"
theoremToSrc' (Local "True")       = "Local True"
theoremToSrc' (Local s)            = s
theoremToSrc' (Invar s)            = s
theoremToSrc' (Paren e)            = "(" ++ e ++ ")"
theoremToSrc' (Adden a bs)         = a ++ ":" ++ L.intercalate ":" bs
theoremToSrc' _                    = ""

instance Show (Fix Theorem) where
    show (Fx Empty) = ""
    show t          = (++";") . theoremToSrc $ t

extractLetStatements :: [Fix Theorem] -> [(String, Fix Theorem)]
extractLetStatements = foldr (\x ys ->
                                case x of
                                    (Fx (Let (Fx (Invar s)) e)) -> (s,e):ys
                                    _                           -> ys) []

getInvarFunctions :: Fix Theorem -> [Fix Theorem]
getInvarFunctions = cata getInvarFunctions'

getInvarFunctions' :: Theorem [Fix Theorem] -> [Fix Theorem]
getInvarFunctions' (Function "maxb" [[Fx (Invar i)]]) = [Fx $ Function "maxb" [Fx $ Invar i]]
getInvarFunctions' (Function "minb" [[Fx (Invar i)]]) = [Fx $ Function "minb" [Fx $ Invar i]]
getInvarFunctions' (Function _ as) = concat as
getInvarFunctions' (Let a b)  = a ++ b
getInvarFunctions' (If a b c) = a ++ b ++ fromMaybe [] c
getInvarFunctions' (InvarExpr a b) = a ++ fromMaybe [] b
getInvarFunctions' (Cond a b)      =  a ++ fromMaybe [] b
getInvarFunctions' (ExprList as)   = concat as
getInvarFunctions' (ExprF _ a)     = a
getInvarFunctions' (RelExpr a b)   = a ++ b
getInvarFunctions' (Expr as)       = concat as
getInvarFunctions' (Or a b)        = a ++ b
getInvarFunctions' (And a b)       = a ++ b
getInvarFunctions' (Mul a b)       = a ++ b
getInvarFunctions' (Div a b)       = a ++ b
getInvarFunctions' (Neg a)         = a
getInvarFunctions' (Pow a b)       = a ++ b
getInvarFunctions' (Paren a)       = a
getInvarFunctions' (Invar i)       = [Fx $ Invar i]
getInvarFunctions' _               = []

containsFunc :: Fix Theorem -> Bool
containsFunc = cata containsFunc'

containsFunc' :: Theorem Bool -> Bool
containsFunc' (Let a b)  = a || b
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
containsFunc' (Div a b)       = a || b
containsFunc' (Neg a)         = a
containsFunc' (Pow a b)       = a || b
containsFunc' (Function f _)  | f == "ln" ||
                                f == "log" ||
                                f == "exp" =  True
                              | otherwise  = False
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
containsInvar' (Div a b)       = a || b
containsInvar' (Neg a)         = a
containsInvar' (Pow a b)       = a || b
containsInvar' (Function _ _)  = True
containsInvar' (Paren a)       = a
containsInvar' _               = False

replaceAllEqSign :: Fix Theorem -> [Fix Theorem]
replaceAllEqSign (Fx (If c (Fx (ExprList as)) elif)) =
        return . Fx $ If c (Fx $ ExprList (concatMap replaceAllEqSign as)) (head . replaceAllEqSign <$> elif)
replaceAllEqSign (Fx (InvarExpr i (Just (Fx (RelExpr (Fx (Relation RelEq)) exp))))) =
        [Fx $ InvarExpr i (Just (Fx (RelExpr (Fx (Relation RelGte)) exp))),
         Fx $ InvarExpr i (Just (Fx (RelExpr (Fx (Relation RelLte)) exp)))]
replaceAllEqSign e = [e]

replaceAllInvar :: [(String, Fix Theorem)] -> Fix Theorem -> Fix Theorem
replaceAllInvar m = cata (replaceAllInvar' m)

replaceAllInvar' :: [(String, Fix Theorem)] -> Theorem (Fix Theorem) -> Fix Theorem
replaceAllInvar' m (Invar i)       = case lookup i m of
                                        Just v -> replaceAllInvar (filter ((/=i) . fst) m) v
                                        _      -> Fx $ Invar i
replaceAllInvar' m v               = Fx v

replaceAllFuncs :: Fix Theorem -> (Fix Theorem, [(String, Fix Theorem)])
replaceAllFuncs f =
    let (exp, expmap)       = cata replaceAllFuncs' f
        (expmap', finalmap) = unzip $ zipWith  (\(a,b) s -> ((a,Fx $ Invar s),(s,b))) expmap invarMappingList
    in (replaceAllInvar expmap' exp, finalmap)


replaceAllFuncs' :: Theorem (Fix Theorem, [(String, Fix Theorem)]) -> (Fix Theorem, [(String, Fix Theorem)])
replaceAllFuncs' (Let (a,a') (b,b'))        = (Fx $ Let a b, a'++b')
replaceAllFuncs' (If (a,a') (b,b') mc)      = case mc of
                                                Just (c,c') -> (Fx $ If a b (Just c), a'++b'++c')
                                                _           -> (Fx $ If a b Nothing, a'++b')
replaceAllFuncs' (InvarExpr (a,a') mb)      = case mb of
                                                Just (b,b') -> (Fx $ InvarExpr a (Just b), a'++b')
                                                _           -> (Fx $ InvarExpr a Nothing, a')
replaceAllFuncs' (Cond (a,a') mb)           = case mb of
                                                Just (b,b') -> (Fx $ Cond a (Just b), a'++b')
                                                _           -> (Fx $ Cond a Nothing, a')
replaceAllFuncs' (ExprF s (a,a'))           = (Fx $ ExprF s a, a')
replaceAllFuncs' (RelExpr (r,r') (p,p'))        = (Fx $ RelExpr r p, r'++p')
replaceAllFuncs' (ExprList es)                       = let (es'',v) = foldr (\(e,t) (es',ts') -> (e:es', t++ts')) ([],[]) es
                                               in (Fx $ ExprList es'', v)
replaceAllFuncs' (Expr es)                       = let (es'',v) = foldr (\(e,t) (es',ts') -> (e:es', t++ts')) ([],[]) es
                                               in (Fx $ Expr es'', v)
replaceAllFuncs' (Or (a,a') (b,b'))             = (Fx $ Or a b, a'++b')
replaceAllFuncs' (And (a,a') (b,b'))             = (Fx $ And a b, a'++b')
replaceAllFuncs' (Div (a,a') (b,b'))             = (Fx $ Div a b, a'++b')
replaceAllFuncs' (Mul (a,a') (b,b'))             = (Fx $ Mul a b, a'++b')
replaceAllFuncs' (Neg (a,a'))                    = (Fx $ Neg a, a')
replaceAllFuncs' (Pow (a,a') (b,b'))             = (Fx $ Pow a b, a'++b')
replaceAllFuncs' (Function fun es) | fun `L.elem` solveableFunctions
                                             = let (es'',v) = foldr (\(e,t) (es',ts') -> (e:es', t++ts')) ([],[]) es
                                               in (Fx $ Function fun es'', v)
                                 | otherwise = let (es'',v) = foldr (\(e,t) (es',ts') -> (e:es', t++ts')) ([],[]) es
                                                   val      = Fx $ Function fun es''
                                               in (Fx $ Invar (theoremToSrc val), (theoremToSrc val, replaceAllInvar v val):v)
replaceAllFuncs' (Paren (a,a'))             = (Fx $ Paren a, a')
replaceAllFuncs' (Local s)                  = (Fx $ Local s, [])
replaceAllFuncs' (Invar a)                  = (Fx $ Invar a, [])
replaceAllFuncs' (Relation a)               = (Fx $ Relation a, [])
replaceAllFuncs' (Number a)                 = (Fx $ Number a, [])
replaceAllFuncs' Empty                      = (Fx Empty, [])
