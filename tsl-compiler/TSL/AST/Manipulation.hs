{-# LANGUAGE DataKinds #-}
module TSL.AST.Manipulation where

import qualified Data.List   as L

import           TSL.AST.AST

-- | Begin helper functions
invarMappingList :: [Theorem a]
invarMappingList = map (Invar . return) (filter (/='I') $ ['A'..'Z'] ++ ['a'..'z'])

getAllInvars :: Theorem a -> [Theorem a]
getAllInvars = map Invar . getInvolves
--- | End helper functions

-- | Begin getInvolves as strings
getInvolves :: Theorem a -> [String]
getInvolves = L.nub . cataTSL [[]]
                      (\a b c -> a ++ b ++ maybe [[]] getInvolves c)
                      (\a b -> a ++ maybe [[]] getInvolves b)
                      (++)
                      (concatMap getInvolves)
                      (\_ b -> b)
                      (++)
                      (const [[]])
                      (concatMap getInvolves)
                      (++)
                      (++)
                      (++)
                      (++)
                      id
                      id
                      (++)
                      id
                      (const [[]])
                      (\_ b -> concatMap getInvolves b)
                      (const [[]])
                      (:[])
                      id
---  | End getInvolves

theoremToSrc :: Show a => Theorem a -> String
theoremToSrc (Expr ts)             = foldl (\s t -> 
                                    case t of
                                       (Neg _) -> s ++ theoremToSrc t
                                       _       -> s ++ (if null s then "" else "+") ++ theoremToSrc t) "" ts
theoremToSrc (Mul a b)             = theoremToSrc a ++ "*" ++ theoremToSrc b
theoremToSrc (Div a b)             = theoremToSrc a ++ "/" ++ theoremToSrc b
theoremToSrc (Pow a b)             = theoremToSrc a ++ "**" ++ theoremToSrc b
theoremToSrc (Neg a)               = "-(" ++ theoremToSrc a ++ ")"
theoremToSrc (Value a)             = theoremToSrc a
theoremToSrc (Number a)            = show a
theoremToSrc (Function "sqrt" es) = "(" ++ (L.intercalate ", " . map theoremToSrc $ es) ++ ")**(1.0/2.0)"
theoremToSrc (Function s es)      = s ++ "(" ++ (L.intercalate ", " . map theoremToSrc $ es) ++ ")"
theoremToSrc (Local s)            = s
theoremToSrc (Invar s)            = s
theoremToSrc (Paren e)            = theoremToSrc e
theoremToSrc _                    = ""

containsInvar :: Theorem a -> Bool
containsInvar = cataTSL False
                        (\a b c -> a || b || maybe False containsInvar c)
                        (\a b -> a || maybe False containsInvar b)
                        (||)
                        (any containsInvar)
                        (\_ b -> b)
                        (||)
                        (const False)
                        (any containsInvar)
                        (||)
                        (||)
                        (||)
                        (||)
                        id
                        id
                        (||)
                        id
                        (const False)
                        (\_ b -> any containsInvar b)
                        (const False)
                        (const True)
                        id

containsFunc :: Theorem a -> Bool
containsFunc = cataTSL False
                         (\a b c -> a || b || maybe False containsInvar c)
                         (\a b -> a || maybe False containsInvar b)
                         (||)
                         (any containsInvar)
                         (\_ b -> b)
                         (||)
                         (const False)
                         (any containsInvar)
                         (||)
                         (||)
                         (||)
                         (||)
                         id
                         id
                         (||)
                         id
                         (const False)
                         (\_ _ -> True)
                         (const False)
                         (const False)
                         id

-- -- | Begin replace Invars
replaceAllInvar :: Eq a => [(Theorem a, Theorem a)] -> Theorem a -> Theorem a
replaceAllInvar _  Empty          = Empty
replaceAllInvar m (InvarExpr i (Just (RelExpr r exp))) =
  InvarExpr (case lookup i m of
              (Just new) -> new
              _          -> i) (Just $ RelExpr r (replaceAllInvar m exp))
replaceAllInvar m (Expr xs)       = Expr $ map (replaceAllInvar m) xs
replaceAllInvar m (Div a b)       = Div (replaceAllInvar m a) (replaceAllInvar m b)
replaceAllInvar m (Mul a b)       = Mul (replaceAllInvar m a) (replaceAllInvar m b)
replaceAllInvar m (Term f)        = Term $ replaceAllInvar m f
replaceAllInvar m (Neg a)         = Neg $ replaceAllInvar m a
replaceAllInvar m (Pow a b)       = Pow (replaceAllInvar m a) (replaceAllInvar m b)
replaceAllInvar m (Value v)       = Value $ replaceAllInvar m v
replaceAllInvar m i@(Invar _)     = case lookup i m of
                                        Just v -> v
                                        _      -> i
replaceAllInvar m (Function f es) = Function f $ map (replaceAllInvar m) es
replaceAllInvar m (Paren e)       = Paren . replaceAllInvar m $ e
replaceAllInvar _ v               = v
--- | End replace

-- -- | Begin replace Functions
replAllFuncs :: Theorem a -> [Theorem a] -> (Theorem a, [(Theorem a, Theorem a)])
replAllFuncs (InvarExpr i (Just (RelExpr r exp))) vals =
    let (exp', vals') = replAllFuncs exp vals
    in  (InvarExpr i (Just (RelExpr r exp')), vals')
replAllFuncs (Expr es) vals = snd $ foldr (\y (v, (Expr es, out)) ->
                                    let (t, vs) = replAllFuncs y v
                                    in (drop (length vs) v, (Expr (es++[t]), out++vs))) (vals, (Expr [], [])) es
replAllFuncs (Div a b) vals =
    let (ta, avs) = replAllFuncs a vals
        (tb, bvs) = replAllFuncs b (drop (length avs) vals)
    in (Div ta tb, avs ++ bvs)
replAllFuncs (Mul a b) vals =
    let (ta, avs) = replAllFuncs a vals
        (tb, bvs) = replAllFuncs b (drop (length avs) vals)
    in (Mul ta tb, avs ++ bvs)
replAllFuncs (Neg a) vals =
    let (t, v) = replAllFuncs a vals
    in  (Neg t, v)
replAllFuncs (Term a) vals =
    let (f, vs) = replAllFuncs a vals
    in  (Term f, vs)
replAllFuncs (Pow a b)                vals  =
    let (fa, avs) = replAllFuncs a vals 
        (fb, bvs) = replAllFuncs b (drop (length avs) vals)
    in (Pow fa fb, avs ++ bvs)
replAllFuncs fv@(Value f@(Function fun _)) (v:_) | fun `L.elem` solveableFunctions
                                                                  = (fv, [])
                                                 | otherwise = (Value v, [(v, f)])
replAllFuncs (Value (Paren expr))     vals  =
    let (p', vs') = replAllFuncs expr vals 
    in (Value $ Paren p', vs')
replAllFuncs (Value n@(Number _))     (v:_) = (Value n, [])
replAllFuncs v                        _     = (v, [])
-- --- | End replace Functions

