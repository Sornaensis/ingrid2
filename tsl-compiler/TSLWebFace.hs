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
import qualified Control.Exception          as E
import           Control.Exception.Lifted   (handle)
import           Control.Monad.IO.Class     (liftIO)
import           Data.Aeson
import           Data.Aeson.Parser          (json)
import           Data.ByteString            (ByteString)
import qualified Data.ByteString.Lazy.Char8 as C
import           Data.Conduit               (($$))
import           Data.Conduit.Attoparsec    (sinkParser)
import           Data.Maybe                 (fromMaybe)
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
import           TSL.Compiler.Python
import           TSL.Compiler.Types

data App = App

mkYesod "App" [parseRoutes|
/rpc/init RPCInitR GET
/rpc/ir RPCIRR POST
/rpc RPCRunR POST
/tsl CompileTSLR GET POST
/tsl/ir PreCompileTSLR GET POST
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
    init <- liftIO $ decode' <$> C.readFile "init.json"
    returnJson $ 
     case init of
       Just v ->  v
       Nothing -> object []

postRPCRunR :: Handler Value
postRPCRunR = do
    json <- requireJsonBody :: Handler Value
    json' <- liftIO $ modValue json
    returnJson json'
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

postRPCIRR :: Handler Value
postRPCIRR = do
    json <- requireJsonBody :: Handler Value
    case decode . cs $ json of
        Just (String tls) ->
            do theorems <- liftIO $ E.handle ((\_ -> return []) :: SomeException -> IO [TSLTheorem]) (mapM genTheorem tls)
               if null theorems
                  then returnJson $ object ["success" .= False, "output" .= ("Compiler error" :: Text)]
                  else do
                    let res = T.pack . unlines . map realizeAnalysis $ theorems
                    returnJson $ object ["success" .= True, "output" .= res]
        _  -> returnJson $ object ["success" .= False, "output" .= ("Compiler error" :: Text)]

postPreCompileTSLR :: Handler Html
postPreCompileTSLR = do
    json <- runInputPost $ ireq textField "theoremjson"
    case decode . cs $ json of
        Just (TSLInput tls) ->
            do theorems <- liftIO $ E.handle ((\_ -> return []) :: SomeException -> IO [TSLTheorem]) (mapM genTheorem tls)
               liftIO $ print . length $ theorems
               if null theorems
                  then badResult json "Compiler Error"
                  else do
                    let res = T.pack . unlines . map (concatMap (show . realizeAnalysis) . theorem) $ theorems
                    defaultLayout
                     [whamlet|
                       <div>
                           <div style="width:40%;float:left;">
                                   <form method=post>
                                       <textarea rows="40" cols="80" name=theoremjson>
                                                 #{json}
                                       <input type=submit>
                           <div style="width:60%;float:left">
                                       <textarea rows="40" cols="80" name=theoremjson>
                                         #{res}
                     |]
        _  -> badResult json "Input Error"

    where
    badResult :: Text -> Text -> Handler Html
    badResult json msg =
     defaultLayout
      [whamlet|
        <div>
            <div style="width:40%;float:left;">
                    <form method=post>
                        <textarea rows="40" cols="80" name=theoremjson>
                                  #{json}
                        <input type=submit>
            <div style="width:60%;float:left">
                        <pre>#{msg}
      |]

getPreCompileTSLR :: Handler Html
getPreCompileTSLR =
    defaultLayout
        [whamlet|
          <div>
              <div style="width:40%;float:left;">
                      <form method=post>
                          <textarea rows="40" cols="80" name=theoremjson>
                                Theorem Json Here
                          <input type=submit>
              <div style="width:60%;float:left">
                              <pre>Enter Theorem JSON and Submit!
        |]


postCompileTSLR :: Handler Html
postCompileTSLR = do
    json <- runInputPost $ ireq textField "theoremjson"
    case decode . cs $ json of
        Just (TSLInput tls) ->
            do theorems <- liftIO $ E.handle ((\_ -> return []) :: SomeException -> IO [TSLTheorem]) (mapM genTheorem tls)
               liftIO $ print . length $ theorems
               if null theorems
                  then badResult json "Compiler Error"
                  else do
                    let res = T.pack . concatMap generateTheorem $ theorems
                    defaultLayout
                     [whamlet|
                       <div>
                           <div style="width:40%;float:left;">
                                   <form method=post>
                                       <textarea rows="40" cols="80" name=theoremjson>
                                                 #{json}
                                       <input type=submit>
                           <div style="width:60%;float:left">
                                       <textarea rows="40" cols="80" name=theoremjson>
                                         #{res}
                     |]
        _  -> badResult json "Input Error"

    where
    badResult :: Text -> Text -> Handler Html
    badResult json msg =
     defaultLayout
      [whamlet|
        <div>
            <div style="width:40%;float:left;">
                    <form method=post>
                        <textarea rows="40" cols="80" name=theoremjson>
                                  #{json}
                        <input type=submit>
            <div style="width:60%;float:left">
                        <pre>#{msg}
      |]

getCompileTSLR :: Handler Html
getCompileTSLR =
    defaultLayout
        [whamlet|
          <div>
              <div style="width:40%;float:left;">
                      <form method=post>
                          <textarea rows="40" cols="80" name=theoremjson>
                                Theorem Json Here
                          <input type=submit>
              <div style="width:60%;float:left">
                              <pre>Enter Theorem JSON and Submit!
        |]
