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
import           Control.Monad              (join)
import           Control.Monad.IO.Class     (liftIO)
import           Data.Aeson
import           Data.Aeson.Parser          (json)
import           Data.ByteString            (ByteString)
import qualified Data.ByteString.Lazy.Char8 as C
import           Data.Conduit               (($$))
import           Data.Conduit.Attoparsec    (sinkParser)
import qualified Data.HashMap.Lazy          as HML
import qualified Data.List                  as L
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
import           System.IO.Temp
import           System.Posix.Files
import           System.Process
import           Yesod


import           TSL.AST.Manipulation
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
    json        <- requireJsonBody :: Handler Value
    case json of
        (Object o) -> do
           (path, hdl) <- liftIO $ openTempFile "/home/sornaensis/ingrid" "ingrid_runner.py"
           ingridpy    <- liftIO $ readFile "/home/sornaensis/ingrid/ingrid.py"
           liftIO $ hPutStrLn hdl ingridpy
           let thms = concat . zipWith mkAddenda [1200..] . fromMaybe [] $ (join $ decode' . encode <$> HML.lookup "Addenda" o)
           let thmtxt = unlines . map genTheoremPure $ thms
           let userthms = "def UserTheorems():\n    return ["++L.intercalate "," (map getAddenda thms)++"]\n\nMain()\n"
           liftIO $ writeFile "/home/sornaensis/ingrid/ingrid2.py" $ unlines [ingridpy,thmtxt,userthms]
           liftIO $ hPutStrLn hdl thmtxt
           liftIO $ hPutStrLn hdl userthms
           json'  <- liftIO $ modValue json path
           returnJson json'
        _          -> returnJson json
    where
    getString (String s) = Just $ cs s
    getString _          = Nothing
    mkAddenda i (Object obj) = fromMaybe [] $ do
        text <- getString =<< HML.lookup ("output" :: Text) =<< (join $ decode' . encode <$> HML.lookup "IR" obj)
        name <- getString =<< HML.lookup "Name" obj
        return [TSLInputTheorem "Theorem" text name i]
    mkAddenda _ _          = []
    getAddenda (TSLInputTheorem n _ _ i) = n ++ show i ++ "()"
    modValue :: Value -> FilePath -> IO Value
    modValue val fn = do
        (Just stdin, Just stdout, Just stderr, ingrid) <- createProcess (proc "python2" [fn])
                                             { std_in = CreatePipe, std_out = CreatePipe, std_err = CreatePipe }
        putStrLn . C.unpack . encode $ val
        hPutStrLn stdin . C.unpack . encode $ val
        hFlush stdin
        _ <- waitForProcess ingrid
        print =<< hGetContents stderr
        reply <- decode . C.pack <$> hGetContents stdout
        removeLink fn
        return $ case reply of
                  (Just resp) -> resp
                  _           -> val

postRPCIRR :: Handler Value
postRPCIRR = do
    json <- requireJsonBody :: Handler Value
    case decode . cs . encode $ json of
        Just (String tls) ->
            do theorems <- liftIO $ E.handle ((\_ -> return []) :: SomeException -> IO [TSLTheorem]) (mapM genTheorem
                    [(TSLInputTheorem "" (cs tls) "" 0)])
               if null theorems
                  then returnJson $ object ["success" .= False, "output" .= ("Compiler error" :: Text)]
                  else do
                    let res = T.pack . unlines . map (unlines . filter (not . null) . map (show . realizeAnalysis) . theorem) $ theorems
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
                    let res = T.pack . unlines . map (unlines . filter (not . null) . map (show . realizeAnalysis) . theorem) $ theorems
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
