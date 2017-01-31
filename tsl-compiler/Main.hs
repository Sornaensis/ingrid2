{-# LANGUAGE OverloadedStrings #-}
module Main where

import Parser
import CodeGen
import Data.Aeson (decode)
import qualified Data.ByteString.Lazy.Char8 as C 

import Prelude hiding ((<$>))

main :: IO ()
main = 
  do input <- decode . C.pack <$> getContents  
     case input of
       Nothing                 -> error "Invalid input"
       (Just (TSLInput tls))   -> 
            do theorems <- mapM genTheorem tls
               mapM_ (putStrLn . unlines . generatePythonClass) $ theorems
  where
  genTheorem t@(TSLInputTheorem n code d i) = 
       do ts <- generateIneq . theoremParser . lexer $ code
          return $ TSLTheorem (TSLInputTheorem (n ++ show i) code d i) $! ts
            
