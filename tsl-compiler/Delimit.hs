{-# LANGUAGE TemplateHaskell #-}
module Delimit where

import           Control.Lens
import           Control.Monad.IO.Class         (liftIO)
import           Control.Monad.Trans.State.Lazy

import           Data.Aeson
import           Data.Map                       (Map)
import qualified Data.Map                       as M
import           Data.Text                      (Text)
import qualified Data.Text                      as T

data IngridValue = Bool BoolBound
                 | Int (NumBound Int)
                 | Real (NumBound Float)

data BoolBound   = BoolBound IngridBool
data NumBound  a = NumBound  { _min, _max :: IngridNum a  }

data IngridBool = Undt | IngridBool Bool

instance Read IngridBool where
    readsPrec _ ('u':'n':'d':'t':rest) = [(Undt, rest)]
    readsPrec _ b                      = let b' = reads b :: [(Bool, String)]
                                         in  case b' of
                                                [(b'',r)] -> [(IngridBool b'',r)]
                                                _       -> []

instance Show IngridBool where
    show Undt           = "undt"
    show (IngridBool b) = show b

data IngridNum a = IngridNum a | Infinity deriving Eq

instance Read a => Read (IngridNum a) where
    readsPrec _ ('u':'n':'d':'t':rest) = [(Infinity, rest)]
    readsPrec _ b                      = let b' = reads b
                                         in  case b' of
                                                [(b'',r)] -> [(IngridNum b'',r)]
                                                _       -> []

instance Show a => Show (IngridNum a) where
    show Infinity = "undt"
    show (IngridNum a) = show a

instance Ord a => Ord (IngridNum a) where
    IngridNum a <= IngridNum b  = a <= b
    Infinity    <= IngridNum _  = False
    IngridNum _ <= Infinity     = True
    Infinity    <= Infinity     = False

-- Data type for invariants
data Invariant = Invariant { _name    :: Text
                           , _value   :: IngridValue
                           , _trace   :: [IngridTrace]
                           , _changed :: Bool
                           }
-- Data Type for trace messages
data IngridTrace = IngridTrace {
                    _message     :: Text
                    , _theoremid :: Int
                    }

-- Data type for error messages
data IngridError = IngridError {
                  _errmsg, _errtype :: Text
                , _errored          :: Bool
                }

data Theorem = Theorem {
                  _involves :: [Text]
                , _theorem  :: Ingrid ()
                }

-- Data type for the entire ingrid world
data IngridWorld = IngridWorld {
                   _invariants :: Map Text Invariant
                 , _theorems   :: [Theorem]
                 , _error      :: IngridError
                 , _stack      :: [Text]
                 }

type Ingrid = StateT IngridWorld IO

doIO :: IO a -> Ingrid a
doIO = liftIO

makeLenses ''NumBound
makeLenses ''Invariant
makeLenses ''IngridError
makeLenses ''IngridWorld
makeLenses ''Theorem

main :: IO ()
main = putStrLn "Hello World"
