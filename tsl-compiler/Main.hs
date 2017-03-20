{-# LANGUAGE OverloadedStrings #-}
module Main where

import           Data.Aeson                 (decode)
import qualified Data.ByteString.Lazy.Char8 as C

import           Debug.Trace

import           TSL.AST.Manipulation
import           TSL.Compiler.Compiler
import           TSL.Compiler.Types
import           TSL.Parser.Parser

main :: IO ()
main =
  do input <- decode . C.pack <$> getContents
     case input of
       Nothing                 -> error "Invalid input"
       (Just (TSLInput tls))   ->
            do theorems <- mapM genTheorem tls
               mapM_ (putStrLn . generateTheorem) theorems
  where
  genTheorem t@(TSLInputTheorem n code d i) =
       do ts <- generateAllIneq 
                    . concatMap replaceAllEqSign
                    . (\(lets, ts) -> map (replaceAllInvar lets) ts) 
                    . (\ts -> (extractLetStatements ts, ts)) 
                    . theoremParser 
                    . lexer $ trace code code
          return $ TSLTheorem (TSLInputTheorem (n ++ show i) code d i) $! ts

