module TSL.Compiler.Compiler (
        generateTheorem,
        generateAllIneq,
        genTheoremPure,
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

genTheoremPure :: TSLInputTheorem -> String
genTheoremPure (TSLInputTheorem n code d i) =
        let ir_past =
                  concatMap replaceAllEqSign
                  . (\(lets, ts) -> map ( replaceAllInvar lets
                                       .  replaceAllInvar lets) ts)
                  . (\ts -> (extractLetStatements ts, filter (not . isLetStatement) ts))
                  . (\t -> if all checkFunctions t then t else error "Invalid Function Passed")
                  . theoremParser
                  . lexer $ trace code code
        in generateTheorem $ 
            TSLTheorem (TSLInputTheorem (n ++ show i) code d i) $! ts

genTheorem :: TSLInputTheorem -> IO TSLTheorem
genTheorem (TSLInputTheorem n code d i) =
     do ts <- generateAllIneq
                  . concatMap replaceAllEqSign
                  . (\(lets, ts) -> map ( replaceAllInvar lets
                                       .  replaceAllInvar lets) ts)
                  . (\ts -> (extractLetStatements ts, filter (not . isLetStatement) ts))
                  . (\t -> if all checkFunctions t then t else error "Invalid Function Passed")
                  . theoremParser
                  . lexer $ trace code code
        return $ TSLTheorem (TSLInputTheorem (n ++ show i) code d i) $! trace (unlines . map (show . realizeAnalysis) $ ts) ts
