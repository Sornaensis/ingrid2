{-# LANGUAGE DeriveFunctor     #-}
module TSL.AST.AST (
                Theorem(..),
                Relation(..),
                Fix(..),
                solveableFunctions,
                validFunctions,
                arityOfFns,
                cata
                ) where

-- Functions we can solve for
solveableFunctions :: [String]
solveableFunctions = ["log","ln","sqrt","cos","sin"]

-- Functions that are a part of our language
validFunctions :: [String]
validFunctions = solveableFunctions ++ 
    ["setmin","setmax","maximum","minimum","congruent","pi"]

        -- Check argument count
        --     func    min    max
arityOfFns :: [(String, (Int, Int))] 
arityOfFns = [
        ("log",       (1, 2))
    ,   ("ln",        (1, 1))
    ,   ("sqrt",      (1, 1))
    ,   ("cos",       (1, 1))
    ,   ("sin",       (1, 1))
    ,   ("maxb",       (1, 1))
    ,   ("minb",       (1, 1))
    ,   ("maximum",   (2, 2))
    ,   ("minimum",   (2, 2))
    ,   ("congruent", (2, 2))
    ,   ("pi",        (0, 0))
    ,   ("setmin",    (1, 1))
    ,   ("setmax",    (1, 1))
    ]

-- A theorem is a list of theorems
data Theorem a = Empty
               | Let a a
               | If a a (Maybe a)
               | InvarExpr a (Maybe a)
               | Cond a (Maybe a)
               | ExprList [a]
               | ExprF String a
               | RelExpr a a
               | Relation Relation
               | Expr [a]
               | Or a a
               | And a a
               | Mul a a
               | Div a a
               | Neg a
               | Pow a a
               | Number Double
               | Function String [a]
               | Local String
               | Invar String
               | Paren a
               deriving (Functor, Show, Eq)

data Relation = RelEq
              | RelGte
              | RelLte
              | RelNeq
              | RelGt
              | RelLt
              deriving Eq

instance Show Relation where
        show RelEq  = "=="
        show RelGte = ">="
        show RelLte = "<="
        show RelNeq = "!="
        show RelGt  = ">"
        show RelLt  = "<"

newtype Fix f = Fx (f (Fix f))
unFix :: Fix f -> f (Fix f)
unFix (Fx x) = x


cata :: Functor f => (f a -> a) -> Fix f -> a
cata alg = alg . fmap (cata alg) . unFix

type MAlgebra m f a = f (m a) -> m a

mcata :: Functor f => MAlgebra m f a -> Fix f -> m a
mcata alg = alg . fmap (mcata alg) . unFix
