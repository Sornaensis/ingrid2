{-# LANGUAGE OverloadedStrings #-}
module TSL.Compiler.Python (
                    generatePythonClass
                ,   generateSymPyIneq
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

indent :: String -> String
indent = unlines . map ("    " ++) . lines

-- | Body
generatePythonClass :: TSLTheorem -> String
generatePythonClass (TSLTheorem (TSLInputTheorem name text disp idnum) ts)  = 
       (("class " ++ name ++ "(Theorem):\n")++) . indent $
                "def __init__(self):\n"
             ++ "    super(" ++ name ++ ", self).__init__(" ++ L.intercalate ", " [show idnum, show . concatMap show . theoremParser . lexer $ text, show disp] ++")\n"
             ++ "def involves(self, str_invar):\n"
             ++ "    return str_invar in " ++ show (L.nub $ concatMap getInvolves ts) ++ "\n"
             ++ "def run(self):\n"
             ++ concatMap (indent . generatePython) ts 
             ++ "    return"

generatePython :: Fix Theorem -> String
generatePython = cata generatePython'  . cata realizeAnalysis'

generatePython' :: Theorem String -> String
generatePython' (Relation a) = show a
generatePython' (RelExpr a b) = " " ++ a ++ " " ++ b
generatePython' (Cond a b)                   = a ++ fromMaybe [] b
generatePython' (InvarExpr a Nothing) = a
generatePython' (InvarExpr a (Just relexpr)) =
           "try:\n    set(" ++ a ++  ", " ++ expr ++ ", ind=\'" ++ rel' ++ "\')\nexcept:\n    pass"
           where
           rel = takeWhile (/= ' ') . dropWhile (==' ') $ relexpr
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
generatePython' (ExprList as)         = L.intercalate "\n" as
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
   | (Cond (Fx (ExprF s e)) Nothing) <- v =
        case s of
            "not" -> Fx $ 
                Cond (Fx $ Function "get" [e]) (Just . Fx $ RelExpr (Fx $ Relation RelEq) (Fx $ ExprF "False" (Fx Empty))) 
            "even" ->  Fx $ Function "evenInvar" [e]
            "odd" -> Fx $ Function "oddInvar" [e]
            "istrue" -> Fx $ InvarExpr e Nothing
            "isset" -> Fx $ 
                And (Fx $ Cond (Fx $ Function "max" [e]) (Just . Fx $ RelExpr (Fx $ Relation RelNeq) (Fx $ ExprF "\'undt\'" (Fx Empty))))
                 (Fx $ Cond (Fx $ Function "min" [e]) (Just . Fx $ RelExpr (Fx $ Relation RelEq) (Fx $ Function "max" [e])))
            "exists" -> Fx $ 
                Cond (Fx $ Function "max" [e]) (Just . Fx $ RelExpr (Fx $ Relation RelNeq) (Fx $ ExprF "\'undt\'" (Fx Empty))) 
            "defined" -> Fx $ 
                Cond (Fx $ Function "min" [e]) (Just . Fx $ RelExpr (Fx $ Relation RelNeq) (Fx $ ExprF "\'undt\'" (Fx Empty))) 
            "undefined" -> Fx $ 
                Cond (Fx $ Function "min" [e]) (Just . Fx $ RelExpr (Fx $ Relation RelEq) (Fx $ ExprF "\'undt\'" (Fx Empty)))
   | (Cond a (Just (Fx (RelExpr (Fx (Relation RelEq)) expr)))) <- v =
        cata realizeAnalysis' $ Fx $ And (Fx (Cond a (Just (Fx (RelExpr (Fx (Relation RelGte)) expr)))))
                                         (Fx (Cond a (Just (Fx (RelExpr (Fx (Relation RelLte)) expr)))))
   | (Cond a (Just (Fx (RelExpr rel expr)))) <- v =
        let bound = getBound rel
            invars = getInvolves expr
            inv_mappings = zip invars (map (`invarAnalysis` expr) invars)
            inv_replce = map (swapBound bound) inv_mappings
            a' = case bound of
                    Max -> Fx $ Function "min" [a]
                    Min -> Fx $ Function "max" [a] 
        in  Fx $ Cond a' (Just . Fx $ RelExpr rel $ replaceAllInvar inv_replce expr)
   | (InvarExpr (Fx (ExprF s e)) Nothing) <- v =
        case s of
            "undefined" -> Fx $ InvarExpr (Fx $ Function "set" [e, 
                                                                Fx $ ExprF "\'undt\'" (Fx Empty),
                                                                Fx $ ExprF "ind=\'Min\'" (Fx Empty)]) Nothing
            "not" -> Fx $ InvarExpr (Fx $ Function "set" [e, 
                                                          Fx $ ExprF "False" (Fx Empty)]) Nothing
            s@"even" -> evenOrOdd s e
            s@"odd"  -> evenOrOdd s e
   | (InvarExpr a (Just (Fx (RelExpr rel expr)))) <- v =
        let bound = getBound rel
            invars = getInvolves expr
            inv_mappings = zip invars (map (`invarAnalysis` expr) invars)
            inv_replce = map (swapBound bound) inv_mappings
        in  Fx $ InvarExpr a (Just . Fx $ RelExpr rel $ replaceAllInvar inv_replce expr)
   | (Cond a Nothing) <- v =
        Fx $ Cond (Fx $ Function "get" [a]) (Just . Fx $ RelExpr (Fx $ Relation RelEq) (Fx $ ExprF "True" (Fx Empty)))
   | (InvarExpr a Nothing) <- v =
        Fx $ InvarExpr (Fx $ Function "set" [a, Fx $ ExprF "True" (Fx Empty)]) Nothing
   | otherwise = Fx v
   where
        swapBound Max (i, InvAn True _) = (i, Fx $ Function "min" [Fx $ Invar i])
        swapBound Min (i, InvAn True _) = (i, Fx $ Function "max" [Fx $ Invar i])
        swapBound Min (i, _)            = (i, Fx $ Function "min" [Fx $ Invar i])
        swapBound Max (i, _)            = (i, Fx $ Function "max" [Fx $ Invar i])
        evenOrOdd s e = Fx $ ExprList [
                            Fx $ If (Fx $ Cond (Fx $ Function "min" [e])
                                               (Just . Fx $ RelExpr (Fx $ Relation RelNeq) 
                                                                     (Fx $ ExprF "\'undt\'" (Fx Empty))))
                                    (Fx $ If (Fx $ Function s [Fx $ Expr [Fx $ Function "min" [e]
                                                                             , Fx $ Number 1]])
                                             (Fx $ InvarExpr (Fx $ Function "set" [e 
                                                                        ,    Fx $ Expr [Fx $ Function "min" [e] 
                                                                                   ,    Fx $ Number 1]
                                                                        , Fx $ ExprF "ind=\'Min\'" (Fx Empty)])
                                                             Nothing)
                                             Nothing)
                                    Nothing,
                            Fx $ If (Fx $ Cond (Fx $ Function "max" [e])
                                               (Just . Fx $ RelExpr (Fx $ Relation RelNeq) 
                                                                     (Fx $ ExprF "\'undt\'" (Fx Empty))))
                                    (Fx $ If (Fx $ Function s [Fx $ Expr [Fx $ Function "max" [e]
                                                                             , Fx $ Neg $ Fx $ Number 1]])
                                             (Fx $ InvarExpr (Fx $ Function "set" [e 
                                                                        ,    Fx $ Expr [Fx $ Function "min" [e] 
                                                                                   ,    Fx $ Neg $ Fx $ Number 1]
                                                                        , Fx $ ExprF "ind=\'Max\'" (Fx Empty)])
                                                             Nothing)
                                             Nothing)
                                    Nothing ]

swapBound Max (InvAn True _) = Min
swapBound Min (InvAn True _) = Max
swapBound Max _              = Max
swapBound Min _              = Min

flipBound Min = Max
flipBound Max = Min

getBound rel = case rel of
            (Fx (Relation RelGte)) -> Min
            (Fx (Relation RelLte)) -> Max
            (Fx (Relation RelGt))  -> Min
            (Fx (Relation RelLt))  -> Max

getIneq rel = case rel of
            Min -> Fx (Relation RelGte)
            Max -> Fx (Relation RelLte)

generateSymPyIneq :: Fix Theorem -> IO [Fix Theorem]
generateSymPyIneq (Fx (If c (Fx (ExprList elist)) elif)) = do
        elist' <- mapM generateSymPyIneq elist
        elif'  <- sequence $ (head <$>) . generateSymPyIneq <$> elif
        return [Fx $ If c (Fx $ ExprList (concat elist')) elif']
generateSymPyIneq e@(Fx (InvarExpr _ (Just (Fx (RelExpr _ _))))) =
        let  (Fx (InvarExpr (Fx (Invar v)) (Just (Fx (RelExpr rel exp)))))    = func_map
             (func_map, func_remap)                            = replaceAllFuncs e 
             rationalFlag                                      = not $ containsFunc exp
             inequality                                        = theoremToSrc exp
             lhs                                               = v
             relation                                          = theoremToSrc rel
             bound                                             = getBound rel
             invar_analyses                                    = map (\i -> (i, getIneq . flipBound . swapBound bound . invarAnalysis i $ exp)) invars
             invars                                            = getInvolves e
        in fmap (map (adjustInequality invar_analyses) . (e:) . map (replaceAllInvar func_remap) . theoremParser . lexer . concat) . sequence $
               invars
                >>= \inv -> return $
                   do Py.initialize
                      equation    <- Py.toUnicode . T.pack $ inequality
                      variables   <- Py.toList =<< map Py.toObject <$> mapM (Py.toUnicode . T.pack) (v:invars)
                      lhs         <- Py.toUnicode . T.pack $ lhs
                      rel         <- Py.toUnicode . T.pack $ relation
                      target      <- Py.toUnicode . T.pack $ inv
                      ms          <- Py.importModule "mystic.symbolic"
                      solver      <- Py.getAttribute ms =<< Py.toUnicode "solve_ingrid"
                      rationalval <- if rationalFlag then Py.true else Py.false
                      pyout       <- Py.callArgs solver [   Py.toObject lhs
                                                    , Py.toObject rel
                                                    , Py.toObject equation
                                                    , Py.toObject variables
                                                    , Py.toObject target
                                                    , Py.toObject rationalval]
                      rewrite     <- Py.cast pyout :: IO (Maybe Py.Unicode)
                      case rewrite of
                       (Just eqn) -> (++";") . T.unpack <$> Py.fromUnicode eqn
                       _          -> return ""
        where
        adjustInequality imap ineq@(Fx (InvarExpr (Fx (Invar v)) (Just (Fx (RelExpr rel exp))))) =
                   maybe ineq (\r -> Fx $ InvarExpr (Fx $ Invar v) (Just . Fx $ RelExpr r exp)) (lookup v imap) 
        adjustInequality _    ineq                                                               = ineq
            
generateSymPyIneq e = return [e]
