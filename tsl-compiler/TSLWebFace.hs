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


postCompileTSLR :: Handler ()
postCompileTSLR = do
    json <- runInputPost $ ireq textField "theoremjson"
    setSession "FormValue" json
    case decode . cs $ json of
        Just (TSLInput tls) ->
            do theorems <- liftIO $ handle ((\_ -> return []) :: SomeException -> IO [TSLTheorem]) (mapM genTheorem tls)
               if null theorems
                  then setSession "CompilerResult" "Compiler Error"
                  else setSession "CompilerResult" (T.pack . concatMap generateTheorem $ theorems)
        _  -> setSession "CompilerResult" "Input Error"
    redirect CompileTSLR

getCompileTSLR :: Handler Html
getCompileTSLR = do
    res <- lookupSession "CompilerResult"
    textval <- lookupSession "FormValue"
    defaultLayout
        [whamlet|
          <div>
              <div style="width:40%;float:left;">
                      <form method=post>
                          <textarea rows="12" cols="50" name=theoremjson>
                            $case textval 
                                $of Nothing
                                    Theorem Json Here
                                $of Just val'
                                    #{val'}
                          <input type=submit>
              <div style="width:60%;float:left">
                      $case res
                          $of Nothing
                              <pre>Enter Theorem JSON and Submit!
                          $of Just res'
                              <pre>#{res'}
        |]

instance Yesod App where
    makeSessionBackend _ = do
        backend <- defaultClientSessionBackend 600 "keyfile.aes"
        return $ Just backend

instance RenderMessage App FormMessage where
    renderMessage _ _ = defaultFormMessage

main :: IO ()
main = warp 6001 App
