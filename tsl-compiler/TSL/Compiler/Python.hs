{-# LANGUAGE OverloadedStrings #-}
module TSL.Compiler.Python (
                    generatePython
                    -- generateSympyIneq,
                    -- generatePythonClass
                    ) where

{- All python generation and related functions go in here
 - -}

import qualified Control.Exception        as E
import qualified Data.Text                as T

import           Control.Monad            (liftM2, replicateM)
import           Control.Monad.Fix        (fix)
import qualified CPython                  as Py
import qualified CPython.Constants        as Py
import qualified CPython.Protocols.Object as Py
import qualified CPython.Types            as Py
import qualified CPython.Types.Dictionary as PyDict
import qualified CPython.Types.Exception  as Py
import qualified CPython.Types.Module     as Py
import qualified CPython.Types.Unicode    as Py
import           Data.Maybe               (fromMaybe)

import qualified Data.List                as L
import qualified Data.Set                 as S

import           Debug.Trace

import           TSL.AST.AST
import           TSL.AST.Manipulation
import           TSL.Compiler.Analysis
import           TSL.Compiler.Types
import           TSL.Parser.Parser

-- indent :: String -> String
-- indent = unlines . map ("    " ++) . lines

-- | Body
-- generatePythonClass :: TSLTheorem -> String
-- generatePythonClass (TSLTheorem (TSLInputTheorem name text disp idnum) ts)  =
--        (("class " ++ name ++ "(Theorem):"):) . concatMap indent $
--              [("def __init__(self):" :) $
--                 indent ["super(" ++ name ++ ", self).__init__(" ++ L.intercalate ", " [show idnum, show text, show disp] ++")"]
--              ,("def involves(self, str_invar):" :) $
--                 indent ["return str_invar in " ++ show (concatMap getInvolves ts)]
--              , ("def run(self, ingrid_obj):" : concatMap (indent . generatePython) ts) ++ ["\treturn"]]

generatePython :: Fix Theorem -> String
generatePython = cata generatePython'  . cata realizeAnalysis'

generatePython' :: Theorem String -> String
generatePython' (Relation a) = show a
generatePython' (RelExpr a b) = a ++ " " ++ b
generatePython' (Cond a b)                   = a ++ fromMaybe [] b
generatePython' (InvarExpr a (Just relexpr)) =
           "set(" ++ a ++  ", " ++ expr ++ ", ind=\'" ++ rel' ++ "\')"
           where
           rel = takeWhile (/= ' ') relexpr
           expr = drop (length rel + 1) relexpr
           rel' = case rel of
                    ">=" -> "Min"
                    "<=" -> "Max"
generatePython' (If a b c)            =
    case a of
        "not Local True" ->
           concat ["if True:\n",
                       unlines (map ("    "++) (lines b)), "\n",
                       maybe [] (" el"++) c]
        _            ->
           concat ["if ", a, ":\n",
                       unlines (map ("    "++) (lines b)), "\n",
                       maybe [] ("el"++) c]
-- generatePython' (ExprF "even" a)      = s ++ " " ++ a
generatePython' (ExprF s a)       = s ++ " " ++ a
generatePython' (ExprList as)         = L.intercalate ",\n" as
generatePython' (Expr (t:ts))         = t ++ concatMap (\s ->
                                                case s of
                                                  ('-':_) -> s
                                                  _       -> '+':s) ts
generatePython' (Or a b)              = a ++ " or " ++ b
generatePython' (And a b)             = a ++ " and " ++ b
generatePython' (Mul a b)             = a ++ "*" ++ b
generatePython' (Div a b)             = a ++ "/" ++ b
generatePython' (Pow a b)             = a ++ "**" ++ b
generatePython' (Neg a)               = "-(" ++ a ++ ")"
generatePython' (Number a)            = show a
generatePython' (Function s es)      = s ++ "(" ++ L.intercalate ", " es ++ ")"
generatePython' (Local s)            = "Local " ++ s
generatePython' (Invar s)            = show s
generatePython' (Paren e)            = "(" ++ e ++ ")"
generatePython' _                    = ""

realizeAnalysis' :: Theorem (Fix Theorem) -> Fix Theorem
realizeAnalysis' v
   | (Cond a (Just (Fx (RelExpr rel expr)))) <- v =
        let bound = getBound rel
            invars = getInvolves expr
            inv_mappings = zip invars (map (`invarAnalysis` expr) invars)
            inv_replce = map (swapBound bound) inv_mappings
        in  Fx $ Cond a (Just . Fx $ RelExpr rel $ replaceAllInvar inv_replce expr)
   | (InvarExpr a (Just (Fx (RelExpr rel expr)))) <- v =
        let bound = getBound rel
            invars = getInvolves expr
            inv_mappings = zip invars (map (`invarAnalysis` expr) invars)
            inv_replce = map (swapBound bound) inv_mappings
        in  Fx $ InvarExpr a (Just . Fx $ RelExpr rel $ replaceAllInvar inv_replce expr)
   | otherwise = Fx v
        where
        swapBound Max (i, InvAn True _) = (i, Fx $ Function "min" [Fx $ Invar i])
        swapBound Min (i, InvAn True _) = (i, Fx $ Function "max" [Fx $ Invar i])
        swapBound Min (i, _)            = (i, Fx $ Function "min" [Fx $ Invar i])
        swapBound Max (i, _)            = (i, Fx $ Function "max" [Fx $ Invar i])
        getBound rel = case rel of
                 (Fx (Relation RelGte)) -> Max
                 (Fx (Relation RelLte)) -> Min
                 (Fx (Relation RelGt))  -> Max
                 (Fx (Relation RelLt))  -> Min




-- generateSympyIneq :: [Fix Theorem] -> IO [Fix Theorem]
-- generateSympyIneq =
--     fmap concat . mapM (\t ->
--           case t of
--            e@(InvarExpr _ _)  -> genIExprIneq e
--            i@(If _ _ _) -> return . IfStmt <$> genIfStmtIneq i
--            t'         -> return [t']
--         )

-- genIfStmtIneq :: Fix Theorem -> IO (Fix Theorem)
-- genIfStmtIneq (If c (ExprList iexpl) Nothing) =
--     fmap (\il -> If c (ExprList il) Nothing) . generateSympyIneq $ iexpl
-- genIfStmtIneq (If c (ExprList iexpl) (Just i)) =
--     let elsestmt = genIfStmtIneq i
--         ifstmt   = If c (ExprList iexpl) Nothing
--     in liftM2 nestif elsestmt (genIfStmtIneq ifstmt)
--     where
--     nestif :: IfStmt -> IfStmt -> IfStmt
--     nestif e (If c iex _) = If c iex (Just e)

-- -- genInvarExprIneq :: Theorem a -> IO [Theorem a]
-- -- genInvarExprIneq = fmap (map extractInvarExprIO) . genIExprIneq
-- --         where
-- --         extractInvarExprIO :: Theorem -> InvarExpr
-- --         extractInvarExprIO (IExpr i) = i

-- genIExprIneq :: Theorem a -> IO [Theorem a]
-- genIExprIneq e@(InvarExpr _ (Just (RelExpr _ _))) =
--         let  (InvarExpr (Invar v) (Just (RelExpr rel exp))) = func_map
--              (func_map, func_remap)                            = replAllFuncs e invarMappingList
--              rationalFlag                                      = not $ containsFunc exp
--              inequality                                        = exprToSrc exp
--              lhs                                               = v
--              relation                                          = show rel
--              invars                                            = v : S.toList (getInvolves exp)
--         in fmap (map (replaceAllInvar func_remap) . theoremParser . lexer . (\i -> trace i i) . concat) . sequence $
--                invars
--                 >>= \inv -> return $
--                    do Py.initialize
--                       equation <- Py.toUnicode . T.pack $ inequality
--                       variables <- Py.toList =<< map Py.toObject <$> mapM (Py.toUnicode . T.pack) invars
--                       lhs <- Py.toUnicode . T.pack $ lhs
--                       rel <- Py.toUnicode . T.pack $ relation
--                       target  <- Py.toUnicode . T.pack $ inv
--                       ms <- Py.importModule "mystic.symbolic"
--                       solver <- Py.getAttribute ms =<< Py.toUnicode "solve_ingrid"
--                       rationalval <- if rationalFlag then Py.true else Py.false
--                       pyout <- Py.callArgs solver [Py.toObject lhs, Py.toObject rel, Py.toObject equation, Py.toObject variables, Py.toObject target, Py.toObject rationalval]
--                       rewrite <- Py.cast pyout :: IO (Maybe Py.Unicode)
--                       case rewrite of
--                        (Just eqn) -> (++";") . T.unpack <$> Py.fromUnicode eqn
--                        _          -> return ""
-- genIExprIneq e = return [IExpr e]
