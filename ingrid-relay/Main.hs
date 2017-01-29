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
