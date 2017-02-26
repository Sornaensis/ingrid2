{-# LANGUAGE DeriveGeneric, OverloadedStrings #-}
module Compiler.Types (
                TSLInput(..), 
                TSLInputTheorem(..), 
                TSLTheorem(..),
                Bound(..)
                ) where

import Data.Aeson (FromJSON(..), ToJSON(..))
import GHC.Generics

import AST.AST

data TSLInput = TSLInput { theorems :: [TSLInputTheorem] } deriving Generic
data TSLInputTheorem = TSLInputTheorem 
                        { name, text, disp :: String,
                               idnum :: Int } deriving Generic -- Use 'Int' to prevent BigNum usage

data TSLTheorem = TSLTheorem { info :: TSLInputTheorem, theorem :: [Theorem] }

instance FromJSON TSLInput
instance FromJSON TSLInputTheorem

instance ToJSON TSLInput
instance ToJSON TSLInputTheorem 

-- CODE GENERATION BELOW --

data Bound = Max | Min deriving (Show, Eq)
