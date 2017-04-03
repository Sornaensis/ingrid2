{-# LANGUAGE CPP                        #-}
{-# LANGUAGE EmptyDataDecls             #-}
{-# LANGUAGE FlexibleContexts           #-}
{-# LANGUAGE GADTs                      #-}
{-# LANGUAGE GeneralizedNewtypeDeriving #-}
{-# LANGUAGE MultiParamTypeClasses      #-}
{-# LANGUAGE OverloadedStrings          #-}
{-# LANGUAGE QuasiQuotes                #-}
{-# LANGUAGE TemplateHaskell            #-}
{-# LANGUAGE TypeFamilies               #-}
import           Control.Exception          (SomeException)
import           Control.Exception          (SomeException, handle)
import           Control.Exception.Lifted   (handle)
import           Control.Monad.IO.Class     (liftIO)
import           Control.Monad.IO.Class     (liftIO)
import           Data.Aeson                 (Value, decode, encode, object,
                                             (.=))
import           Data.Aeson
import           Data.Aeson.Parser          (json)
import           Data.ByteString            (ByteString)
import qualified Data.ByteString.Lazy.Char8 as C
import           Data.Conduit               (($$))
import           Data.Conduit.Attoparsec    (sinkParser)
import           Data.String.Conversions
import           Data.Text                  (Text)
import qualified Data.Text                  as T
import           Data.Text.Encoding         (encodeUtf8)
import           Network.HTTP.Types         (status200, status400)
import           Network.Wai                (Application, Response, responseLBS)
import           Network.Wai.Conduit        (sourceRequestBody)
import           Network.Wai.Handler.Warp   (run)
import           System.IO                  (hFlush, hGetContents, hPutStrLn)
import           System.Process
import           Yesod


import           TSL.Compiler.Compiler
import           TSL.Compiler.Types

data App = App

mkYesod "App" [parseRoutes|
/rpc/init RPCInitR GET
/rpc RPCRunR POST
|]

instance Yesod App where
    makeSessionBackend _ = do
        backend <- defaultClientSessionBackend 600 "keyfile.aes"
        return $ Just backend

instance RenderMessage App FormMessage where
    renderMessage _ _ = defaultFormMessage

main :: IO ()
main = warp 4000 App

getRPCInitR :: Handler Value
getRPCInitR = do
    init <- decode <$> liftIO $ readFile "init.json"
    returnJson $ fromMaybe (object []) init

postRPCRunR :: Handler Value
postRPCRunR = do
    json <- requireJsonBody :: Handler Value
    returnJson . liftIO $ modValue json
    where
    -- Application-specific logic would go here.
    modValue :: Value -> IO Value
    modValue val = do (Just stdin, Just stdout, _, ingrid) <- createProcess (proc "python2" ["ingrid.py"])
                                                           { std_in = CreatePipe, std_out = CreatePipe }
                      hPutStrLn stdin . C.unpack . encode $ val
                      hFlush stdin
                      _ <- waitForProcess ingrid
                      reply <- decode . C.pack <$> hGetContents stdout
                      return $ case reply of
                                (Just resp) -> resp
                                _           -> val
