{-# LANGUAGE DeriveFunctor #-}
module TSL.AST.AST (
                Theorem(..),
                Relation(..),
                Fix(..),
                solveableFunctions,
                cata
                ) where

import           Data.Maybe
import           Data.Morphism.Cata

-- Functions we can solve for
solveableFunctions :: [String]
solveableFunctions = ["log","ln","sqrt","cos","sin"]

-- A theorem is a list of theorems
data Theorem a = Empty
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

newtype Fix f = Fx (f (Fix f))
unFix :: Fix f -> f (Fix f)
unFix (Fx x) = x

cata :: Functor f => (f a -> a) -> Fix f -> a
cata alg = alg . fmap (cata alg) . unFix

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
