{-# LANGUAGE KindSignatures  #-}
{-# LANGUAGE TemplateHaskell #-}
module TSL.AST.AST (
                Theorem(..),
                solveableFunctions,
                cataTSL,
                ) where

import           Data.Maybe
import           Data.Morphism.Cata

-- Functions we can solve for
solveableFunctions :: [String]
solveableFunctions = ["log","ln","sqrt","cos","sin"]

-- A theorem is a list of theorems
data Theorem a = Empty
               | If (Theorem a) (Theorem a) (Maybe (Theorem a))
               | InvarExpr (Theorem a) (Maybe (Theorem a))
               | Cond (Theorem a) (Theorem a)
               | ExprList [Theorem a]
               | ExprF String (Theorem a)
               | RelExpr (Theorem a) (Theorem a)
               | Relation Relation
               | Expr [Theorem a]
               | Or (Theorem a) (Theorem a)
               | And (Theorem a) (Theorem a)
               | Mul (Theorem a) (Theorem a)
               | Div (Theorem a) (Theorem a)
               | Neg (Theorem a)
               | Term (Theorem a)
               | Pow (Theorem a) (Theorem a)
               | Value (Theorem a)
               | Number a
               | Function String [Theorem a]
               | Local String
               | Invar String
               | Paren (Theorem a)
               deriving (Show,Eq)

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

$(makeCata defaultOptions { cataName = "cataTSL" } ''Theorem)
