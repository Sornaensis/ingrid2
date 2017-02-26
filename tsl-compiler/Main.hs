{-# LANGUAGE OverloadedStrings #-}
module Main where

import           Data.Aeson                 (decode)
import qualified Data.ByteString.Lazy.Char8 as C

import           Debug.Trace

import           Compiler.Compiler
import           Compiler.Types
import           Parser.Parser

main :: IO ()
main =
  do input <- decode . C.pack <$> getContents
     case input of
       Nothing                 -> error "Invalid input"
       (Just (TSLInput tls))   ->
            do theorems <- mapM genTheorem tls
               mapM_ (putStrLn . unlines . generateTheorem) $ theorems
  where
  genTheorem t@(TSLInputTheorem n code d i) =
       do ts <- generateAllIneq . theoremParser . lexer $ trace code code
          return $ TSLTheorem (TSLInputTheorem (n ++ show i) code d i) $! ts

