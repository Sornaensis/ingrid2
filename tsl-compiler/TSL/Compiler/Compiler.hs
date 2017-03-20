module TSL.Compiler.Compiler (
        generateTheorem,
        generateAllIneq
        ) where

import           Data.Set            (Set)
import qualified Data.Set            as S

import           TSL.AST.AST
import           TSL.Compiler.Python
import           TSL.Compiler.Types

generateTheorem :: TSLTheorem -> String
generateTheorem = generatePythonClass

generateAllIneq :: [Fix Theorem] -> IO [Fix Theorem]
generateAllIneq = fmap concat . mapM generateSymPyIneq

