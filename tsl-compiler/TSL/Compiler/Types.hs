{-# LANGUAGE DeriveGeneric     #-}
{-# LANGUAGE OverloadedStrings #-}
module TSL.Compiler.Types (
                TSLInput(..),
                TSLInputTheorem(..),
                TSLTheorem(..),
                Bound(..)
                ) where

import           Data.Aeson   (FromJSON (..), ToJSON (..))
import           GHC.Generics

import           TSL.AST.AST

data TSLInput = TSLInput { theorems :: [TSLInputTheorem] } deriving Generic
data TSLInputTheorem = TSLInputTheorem
                        { name, text, disp :: String,
                               idnum       :: Int } deriving Generic -- Use 'Int' to prevent BigNum usage

data TSLTheorem a = TSLTheorem { info :: TSLInputTheorem, theorem :: [Theorem a] }

instance FromJSON TSLInput
instance FromJSON TSLInputTheorem

instance ToJSON TSLInput
instance ToJSON TSLInputTheorem

-- CODE GENERATION BELOW --

data Bound = Max | Min deriving (Show, Eq)
