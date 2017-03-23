module TSL.Compiler.Compiler (
        generateTheorem,
        generateAllIneq,
        genTheorem
        ) where

import           Data.Set             (Set)
import qualified Data.Set             as S

import           TSL.AST.AST
import           TSL.AST.Manipulation
import           TSL.Compiler.Python
import           TSL.Compiler.Types
import           TSL.Parser.Parser

generateTheorem :: TSLTheorem -> String
generateTheorem = generatePythonClass

generateAllIneq :: [Fix Theorem] -> IO [Fix Theorem]
generateAllIneq = fmap concat . mapM generateSymPyIneq

genTheorem :: TSLInputTheorem -> IO TSLTheorem
genTheorem (TSLInputTheorem n code d i) =
     do ts <- generateAllIneq
                  . concatMap replaceAllEqSign
                  . (\(lets, ts) -> map (replaceAllInvar lets
                                       . replaceAllInvar lets) ts)
                  . (\ts -> (extractLetStatements ts, ts))
                  . theoremParser
                  . lexer $ code
        return $ TSLTheorem (TSLInputTheorem (n ++ show i) code d i) $! ts
