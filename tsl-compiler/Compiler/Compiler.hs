module Compiler.Compiler (
        generateTheorem, 
        generateAllIneq
        ) where

import qualified Data.Set as S
import Data.Set (Set)
import AST.AST
import Compiler.Types

import Compiler.Python

generateTheorem :: TSLTheorem -> [String]
generateTheorem = generatePythonClass

generateAllIneq :: [Theorem] -> IO [Theorem]
generateAllIneq = generateSympyIneq
                                           
