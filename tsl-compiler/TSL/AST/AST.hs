{-# LANGUAGE TemplateHaskell #-}
{-# LANGUAGE KindSignatures #-}
module TSL.AST.AST (
                Theorem(..), 
                solveableFunctions,
                tslCata
                ) where

import Data.Morphism.Cata

-- Functions we can solve for
solveableFunctions :: [String]
solveableFunctions = ["log","ln","sqrt","cos","sin"]

-- A theorem is a list of theorems
data Theorem a = IExpr (Theorem a)
               | IfStmt (Theorem a)
               | NullBody
               | If (Theorem a) (Theorem a) (Maybe (Theorem a)) 
               | CondOr (Theorem a) (Theorem a)
               | CondAnd (Theorem a) (Theorem a)
               | CondSpec String (Theorem a)
               | CondSpecF String (Theorem a)
               | Cond (Theorem a) (Maybe (Theorem a))
               | CondRel (Theorem a) (Theorem a)
               | InvarExprList [Theorem a]
               | InvarOr (Theorem a) (Theorem a)
               | InvarAnd (Theorem a) (Theorem a)
               | InvarExpr (Theorem a) (Maybe (Theorem a))
               | InvarExprNot (Theorem a) 
               | InvarExprEven (Theorem a) 
               | InvarExprOdd (Theorem a) 
               | InvarExprUndefined (Theorem a)
               | InvarRelExpr (Theorem a) (Theorem a)
               | RelEq
               | RelGte
               | RelLte
               | RelNeq
               | RelGt
               | RelLt
               | Expr [Theorem a]
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

$(makeCata defaultOptions { cataName = "tslCata" } ''Theorem)
