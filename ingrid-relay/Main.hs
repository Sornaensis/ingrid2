{-# LANGUAGE OverloadedStrings #-}
import           Control.Exception        (SomeException)
import           Control.Exception.Lifted (handle)
import           Control.Monad.IO.Class   (liftIO)
import           Data.Aeson               (Value, encode, decode, object, (.=))
import           Data.Aeson.Parser        (json)
import           Data.ByteString          (ByteString)
import           Data.Conduit             (($$))
import           Data.Conduit.Attoparsec  (sinkParser)
import           Network.HTTP.Types       (status200, status400)
import           Network.Wai              (Application, Response, responseLBS)
import           Network.Wai.Conduit      (sourceRequestBody)
import           Network.Wai.Handler.Warp (run)
import           System.Process
import           System.IO (hPutStrLn, hGetContents, hFlush)
import qualified Data.ByteString.Lazy.Char8 as C 

infixl 4 <$>
(<$>) = fmap

main :: IO ()
main = run 4000 app

app :: Application
app req sendResponse = handle (sendResponse . invalidJson) $ do
    value <- sourceRequestBody req $$ sinkParser json
    newValue <- liftIO $ modValue value
    sendResponse $ responseLBS
        status200
        [("Content-Type", "application/json"), ("Access-Control-Allow-Origin", "*")]
        $ encode newValue

invalidJson :: SomeException -> Response
invalidJson ex = responseLBS
    status400
    [("Content-Type", "application/json")]
    $ encode $ object
        [ "message" .= show ex
        ]

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
import           Control.Exception       (SomeException, handle)
import           Control.Monad.IO.Class  (liftIO)
import           Data.Aeson
import           Data.String.Conversions
import           Data.Text               (Text)
import qualified Data.Text               as T
import           Data.Text.Encoding      (encodeUtf8)
import           Yesod


import           TSL.Compiler.Compiler
import           TSL.Compiler.Types

data App = App

mkYesod "App" [parseRoutes|
/rpc/init RPCInitR GET 
|]

instance Yesod App where
    makeSessionBackend _ = do
        backend <- defaultClientSessionBackend 600 "keyfile.aes"
        return $ Just backend

instance RenderMessage App FormMessage where
    renderMessage _ _ = defaultFormMessage

main :: IO ()
main = warp 6001 App

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
