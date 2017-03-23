{-# LANGUAGE OverloadedStrings #-}
module Main where

import           Data.Aeson                 (decode)
import qualified Data.ByteString.Lazy.Char8 as C

import           Debug.Trace

import           TSL.Compiler.Compiler
import           TSL.Compiler.Types

main :: IO ()
main =
  do input <- decode . C.pack <$> getContents
     case input of
       Nothing                 -> error "Invalid input"
       (Just (TSLInput tls))   ->
            do theorems <- mapM genTheorem tls
               mapM_ (putStrLn . generateTheorem) theorems

