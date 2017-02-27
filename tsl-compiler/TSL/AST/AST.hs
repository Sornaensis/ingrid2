module TSL.AST.AST (
                Theorem(..), 
                IfStmt(..),
                Cond(..), 
                CondRel(..),
                InvarExprList(..), 
                InvarExpr(..),
                InvarRelExpr(..), 
                Relation(..), 
                Expr(..), 
                Term(..), 
                Factor(..), 
                Value(..),
                solveableFunctions
                ) where

-- Functions we can solve for
solveableFunctions :: [String]
solveableFunctions = ["log","ln","sqrt","cos","sin"]

-- A theorem is a list of theorems
data Theorem = IExpr InvarExpr
             | IfStmt IfStmt
             | NullBody
    deriving (Show)

-- If statements may be nested
data IfStmt = If Cond InvarExprList (Maybe IfStmt) 
    deriving (Show)

data Cond = CondOr Cond Cond
          | CondAnd Cond Cond
          | CondSpec String Value
          | CondSpecF String Expr
          | Cond Value (Maybe CondRel)
    deriving (Show)

data CondRel = CondRel Relation Expr
    deriving (Show)

data InvarExprList = InvarExprList [Theorem]
    deriving (Show)

data InvarExpr = InvarOr InvarExpr InvarExpr
               | InvarAnd InvarExpr InvarExpr
               | InvarExpr Value (Maybe InvarRelExpr)
               | InvarExprNot Value 
               | InvarExprEven Value 
               | InvarExprOdd Value 
               | InvarExprUndefined Value
    deriving (Show)

data InvarRelExpr = InvarRelExpr Relation Expr
    deriving (Show)

data Relation = RelEq
              | RelGte
              | RelLte
              | RelNeq
              | RelGt
              | RelLt

instance Show Relation where
    show RelEq = "=="
    show RelGte = ">="
    show RelLte = "<="
    show RelLt  = "<"
    show RelGt  = ">"
    show RelNeq = "!="

-- A list of terms to be summed
data Expr = Expr [Term]
    deriving (Show)

data Term = Mul Term Term
          | Div Term Term
          | Neg Term
          | Term Factor
    deriving (Show)

data Factor = Pow Factor Factor
            | Value Value
    deriving (Show)

data Value = Number Double
           | Function String [Expr] 
           | Local String
           | Invar String
           | Paren Expr
    deriving (Show)

instance Eq Value where
    (Number a) == Number b = a == b
    Invar a == Invar b = a == b
    _ == _ = False 



