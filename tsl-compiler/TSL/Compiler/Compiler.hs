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

import           Debug.Trace

generateTheorem :: TSLTheorem -> String
generateTheorem = generatePythonClass

generateAllIneq :: [Fix Theorem] -> IO [Fix Theorem]
generateAllIneq = fmap concat . mapM generateSymPyIneq

genTheorem' :: String -> IO (TSLTheorem)
genTheorem' = genTheorem . theoremParser . lexer

genTheorem :: TSLInputTheorem -> IO TSLTheorem
genTheorem (TSLInputTheorem n code d i) =
     do ts <- generateAllIneq
                  . concatMap replaceAllEqSign
                  . (\(lets, ts) -> map ( replaceAllInvar lets
                                       .  replaceAllInvar lets) ts)
                  . (\ts -> (extractLetStatements ts, filter (not . isLetStatement) ts))
                  . theoremParser
                  . lexer $ trace code code
        return $ TSLTheorem (TSLInputTheorem (n ++ show i) code d i) $! trace (unlines . map (show . realizeAnalysis) $ ts) ts
