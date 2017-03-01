module TSL.Compiler.Analysis (
                    exprAnalysis,
                    InvarBoundSwitch(..),
                    swap
                    ) where

import qualified Data.List      as L
import qualified Data.Set       as S

import           TSL.AST.AST
import TSL.AST.Manipulation
import           TSL.Compiler.Types

data InvarBoundSwitch = Flip Int | NotFound | Maximize | Minimize deriving Eq

swap :: Bound -> InvarBoundSwitch -> Bound
swap Max (Flip True) = Min
swap Min (Flip True) = Max
swap Min Maximize    = Max
swap b   _           = b

flipbound :: InvarBoundSwitch -> InvarBoundSwitch
flipbound (Flip a) = Flip $ not a
flipbound NotFound = Flip True
flipbound a        = a

--- | Expression Analysis
invarAnalysis :: String -> Fix Theorem -> InvarBoundSwitch
invarAnalysis s = snd . cata (invarAnalysis' s) . replaceAllInvar [(s,Fx $ Local s)]

invarAnalysis' :: String -> Theorem (Fix Theorem, InvarBoundSwitch) -> (Fix Theorem, InvarBoundSwitch)

