module TSL.Compiler.Analysis (
                    InvarBoundSwitch(..),
                    invarAnalysis
                    ) where

import qualified Data.List            as L
import qualified Data.Set             as S

import           Data.Maybe
import           TSL.AST.AST
import           TSL.AST.Manipulation
import           TSL.Compiler.Types

-- data Sign = Positive | Negative deriving Eq

data InvarBoundSwitch = Coeff Double | InvAn Bool Double | Complex | NotFound deriving (Show, Eq)

-- swap :: Bound -> InvarBoundSwitch -> Bound
-- swap Max (Flip True) = Min
-- swap Min (Flip True) = Max
-- swap Min Maximize    = Max
-- swap b   _           = b

isCoeff :: InvarBoundSwitch -> Bool
isCoeff (Coeff _) = True
isCoeff _         = False

chooseBound :: InvarBoundSwitch -> InvarBoundSwitch -> InvarBoundSwitch
chooseBound (InvAn af ad) (InvAn bf bd) | abs ad == abs bd && af && abs ad > 1  = InvAn af ad
                                        | abs ad == abs bd && bf && abs ad > 1  = InvAn bf bd
                                        | abs ad == abs bd && af && abs ad <= 1 = InvAn bf bd
                                        | abs ad == abs bd && bf && abs ad <= 1 = InvAn af ad
                                        | abs ad > abs bd                       = InvAn af ad
                                        | otherwise                             = InvAn bf bd
chooseBound Complex       _             = Complex
chooseBound _             Complex       = Complex
chooseBound _             a@InvAn{}     = a
chooseBound a@InvAn{}     _             = a
chooseBound NotFound      a             = a
chooseBound a             NotFound      = a
chooseBound _             _             = NotFound

flipInvBound :: InvarBoundSwitch -> InvarBoundSwitch
flipInvBound (InvAn af ad) = InvAn (not af) ad
flipInvBound a             = a

addBound :: InvarBoundSwitch -> InvarBoundSwitch -> InvarBoundSwitch
addBound (InvAn af ad) (InvAn bf bd) |  af == bf  = InvAn af $ ad+bd
                                     |  otherwise = chooseBound (InvAn af ad) (InvAn bf bd)
addBound a@InvAn{}     _             = a
addBound _             a@InvAn{}     = a
addBound NotFound      a             = a
addBound a             _             = a

mulBound :: InvarBoundSwitch -> InvarBoundSwitch -> InvarBoundSwitch
mulBound Complex       _             = Complex
mulBound _             Complex       = Complex
mulBound InvAn{}       InvAn{}       = Complex
mulBound (InvAn af ad) (Coeff c)     = InvAn af $ ad*c
mulBound (Coeff c)     (InvAn af ad) = InvAn af $ ad*c
mulBound InvAn{}       NotFound      = Complex
mulBound _             a@InvAn{}     = a
mulBound NotFound      a             = a
mulBound a             _             = a

--- | Expression Analysis
invarAnalysis :: String -> Fix Theorem -> InvarBoundSwitch
invarAnalysis s = cata (invarAnalysis' s)

invarAnalysis' :: String -> Theorem InvarBoundSwitch -> InvarBoundSwitch
--- If we only match numbers
invarAnalysis' s (Mul (Coeff a) (Coeff b)) = Coeff $ a*b
invarAnalysis' s (Div (Coeff a) (Coeff b)) = Coeff $ a/b
invarAnalysis' s (Neg (Coeff a))           = Coeff $ -1*a
invarAnalysis' s (Pow (Coeff a) (Coeff b)) = Coeff $ a**b
---
invarAnalysis' s (If a b c)                 = foldr1 chooseBound [a, b, fromMaybe NotFound c]
invarAnalysis' s (InvarExpr a b)            = foldr1 chooseBound [a,    fromMaybe NotFound b]
invarAnalysis' s (RelExpr a b)              = chooseBound a b
invarAnalysis' s (ExprList [])              = NotFound
invarAnalysis' s (ExprList as)              = foldr1 chooseBound as
invarAnalysis' s (Expr [])                  = NotFound
invarAnalysis' s (Expr as)                  | all isCoeff as = foldr1 (\(Coeff a) (Coeff b) -> Coeff $ a+b)  as
                                            | otherwise      = foldr chooseBound NotFound . filter (not . isCoeff) $ as
invarAnalysis' s (Mul a b)                  = addBound a b
invarAnalysis' s (Div a b)                  = chooseBound a (flipInvBound b)
invarAnalysis' s (Neg a)                    = flipInvBound a
invarAnalysis' s (Pow a b)                  = mulBound a b
invarAnalysis' s (Function "sqrt" as@(_:_)) = foldr1 chooseBound . map (mulBound $ Coeff 0.5) $ as
invarAnalysis' s (Function _ [])            = NotFound
invarAnalysis' s (Function _ as)            = foldr1 chooseBound as
invarAnalysis' s (Paren a)                  = a
invarAnalysis' s (Number n)                 = Coeff n
invarAnalysis' s (Invar i)                  | s == i = InvAn False 1
invarAnalysis' _ _                          = NotFound


