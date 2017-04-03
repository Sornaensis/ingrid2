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
/tsl CompileTSLR GET POST
|]


postCompileTSLR :: Handler Html
postCompileTSLR = do
    json <- runInputPost $ ireq textField "theoremjson"
    case decode . cs $ json of
        Just (TSLInput tls) ->
            do theorems <- liftIO $ handle ((\_ -> return []) :: SomeException -> IO [TSLTheorem]) (mapM genTheorem tls)
               liftIO $ print . length $ theorems
               if null theorems
                  then badResult json "Compiler Error"
                  else do
                    let res = T.pack . concatMap realizeAnalysis $ theorems
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

instance Yesod App where
    makeSessionBackend _ = do
        backend <- defaultClientSessionBackend 600 "keyfile.aes"
        return $ Just backend

instance RenderMessage App FormMessage where
    renderMessage _ _ = defaultFormMessage

main :: IO ()
main = warp 6001 App
