{-# LANGUAGE OverloadedStrings #-}
module TSL.Compiler.Python (
                    generatePythonClass
                ,   generatePython
                ,   realizeAnalysis
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

realizeAnalysis :: Fix Theorem -> Fix Theorem
realizeAnalysis = cata realizeAnalysis'

-- | Body
generatePythonClass :: TSLTheorem -> String
generatePythonClass (TSLTheorem (TSLInputTheorem name text disp idnum) ts)  = 
       (("class " ++ name ++ "(Theorem):\n")++) . indent $
                "def __init__(self):\n"
             ++ "    super(" ++ name ++ ", self).__init__(" ++ L.intercalate ", " [show idnum, show . unlines . map show . theoremParser . lexer $ text, show disp] ++")\n"
             ++ "def involves(self, str_invar):\n"
             ++ "    return str_invar in " ++ show (L.nub $ concatMap getInvolves ts) ++ "\n"
             ++ "def run(self):\n"
             ++ "    get = self.get\n"
             ++ "    set = self.set\n"
             ++ "    maxb = self.maxb\n"
             ++ "    minb = self.minb\n"
             ++ "    evenInvar = self.evenInvar\n"
             ++ "    oddInvar = self.oddInvar\n"
             ++ "    congruent = self.congruent\n"
             ++ concatMap (indent . generatePython) ts 
             ++ "    return"

generatePython :: Fix Theorem -> String
generatePython = cata generatePython'  . cata realizeAnalysis2' . cata realizeAnalysis'

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
                       init $ unlines (map ("    "++) (lines b)),
                       maybe [] ("\n el"++) c]
        _            ->
           concat ["if ", a, ":\n",
                       init $ unlines (map ("    "++) (lines b)),
                       maybe [] ("\nel"++) c]
-- generatePython' (ExprF "even" a)      = s ++ " " ++ a
generatePython' (ExprF s a)       = s ++ (if null a then "" else " " ++ a)
generatePython' (ExprList as)           = L.intercalate "\n" . filter (not . null) $ as
generatePython' (Expr (t:ts))           = t ++ concatMap (\s ->
                                                  case s of
                                                    ('-':_) -> s
                                                    _       -> '+':s) ts
generatePython' (Or a b)                = a ++ " or " ++ b
generatePython' (And a b)               = a ++ " and " ++ b
generatePython' (Mul a b)               = a ++ "*" ++ b
generatePython' (Div a b)               = a ++ "/" ++ b
generatePython' (Pow a b)               = a ++ "**" ++ b
generatePython' (Neg a)                 = "-(" ++ a ++ ")"
generatePython' (Number a)              = show a
generatePython' (Function "setmin" es)  = "try:\n    set(" ++ L.intercalate ", " es ++ ", ind=\'Min\')\nexcept:\n    pass"
generatePython' (Function "setmax" es)  = "try:\n    set(" ++ L.intercalate ", " es ++ ", ind=\'Max\')\nexcept:\n    pass"
generatePython' (Function s es)         = s ++ "(" ++ L.intercalate ", " es ++ ")"
generatePython' (Local "True")          = "Local True"
generatePython' (Local s)               = show s
generatePython' (Invar s)               = show s
generatePython' (Paren e)               = "(" ++ e ++ ")"
generatePython' _                       = ""

realizeAnalysis2' :: Theorem (Fix Theorem) -> Fix Theorem
realizeAnalysis2' v
   | ExprF "nosolve" ivexpr <- v = cata realizeAnalysis2' . cata realizeAnalysis' $ ivexpr
   | Function "setmax" [i, e] <- v =
        let ivs = map (\f -> Fx $ Cond f    
                                       (Just . Fx $ RelExpr (Fx $ Relation RelNeq)
                                                            (Fx $ ExprF "\'undt\'" (Fx Empty)))) .
                      L.nubBy eqIFns . filter isFunction $ getInvarFunctions e
        in  if null ivs 
              then Fx $ Function "setmax" [i, e]
              else
               if length ivs == 1
                 then Fx $ If (head ivs) (Fx $ Function "setmax" [i, e]) Nothing
                 else Fx $ If (foldr1 (\x y -> Fx $ And x y) ivs) (Fx $ Function "setmax" [i, e]) Nothing
   | Function "setmin" [i, e] <- v =
        let ivs = map (\f -> Fx $ Cond f    
                                       (Just . Fx $ RelExpr (Fx $ Relation RelNeq)
                                                            (Fx $ ExprF "\'undt\'" (Fx Empty)))) .
                      L.nubBy eqIFns . filter isFunction $ getInvarFunctions e
        in  if null ivs 
              then Fx $ Function "setmin" [i, e]
              else
               if length ivs == 1
                 then Fx $ If (head ivs) (Fx $ Function "setmin" [i, e]) Nothing
                 else Fx $ If (foldr1 (\x y -> Fx $ And x y) ivs) (Fx $ Function "setmin" [i, e]) Nothing
   | (Cond (Fx (ExprF s e)) Nothing) <- v =
        case s of
            "not" -> Fx $ 
                Cond (Fx $ Function "get" [e]) (Just . Fx $ RelExpr (Fx $ Relation RelEq) (Fx $ ExprF "False" (Fx Empty))) 
            "even" ->  Fx $ Function "evenInvar" [e]
            "odd" -> Fx $ Function "oddInvar" [e]
            "istrue" -> Fx $ InvarExpr e Nothing
            "isset" -> Fx $ 
                And (Fx $ Cond (Fx $ Function "maxb" [e]) (Just . Fx $ RelExpr (Fx $ Relation RelNeq) (Fx $ ExprF "\'undt\'" (Fx Empty))))
                 (Fx $ Cond (Fx $ Function "minb" [e]) (Just . Fx $ RelExpr (Fx $ Relation RelEq) (Fx $ Function "maxb" [e])))
            "exists" -> Fx $ 
                Cond (Fx $ Function "maxb" [e]) (Just . Fx $ RelExpr (Fx $ Relation RelNeq) (Fx $ ExprF "\'undt\'" (Fx Empty))) 
            "defined" -> Fx $ 
                Cond (Fx $ Function "minb" [e]) (Just . Fx $ RelExpr (Fx $ Relation RelNeq) (Fx $ ExprF "\'undt\'" (Fx Empty))) 
            "undefined" -> Fx $ 
                Cond (Fx $ Function "minb" [e]) (Just . Fx $ RelExpr (Fx $ Relation RelEq) (Fx $ ExprF "\'undt\'" (Fx Empty)))
   | (Cond a (Just (Fx (RelExpr (Fx (Relation RelNeq)) expr)))) <- v =
        cata realizeAnalysis2' . cata realizeAnalysis' . Fx . Paren . Fx $ Or (Fx $ Paren (Fx (Cond a (Just (Fx (RelExpr (Fx (Relation RelGt)) expr))))))
                                         (Fx $ Paren (Fx (Cond a (Just (Fx (RelExpr (Fx (Relation RelLt)) expr))))))
   | (Cond a (Just (Fx (RelExpr (Fx (Relation RelEq)) expr)))) <- v =
        cata realizeAnalysis2' . cata realizeAnalysis' . Fx . Paren . Fx $ And (Fx (Cond a (Just (Fx (RelExpr (Fx (Relation RelGte)) expr)))))
                                         (Fx (Cond a (Just (Fx (RelExpr (Fx (Relation RelLte)) expr)))))
   | (Cond a@(Fx (Function _ _)) (Just (Fx (RelExpr rel expr)))) <- v =
        let bound = flipBound $ getBound rel
            invars = getInvolves expr
            inv_mappings = zip invars (map (`invarAnalysis` expr) invars)
            inv_replce = map (swapBound bound) inv_mappings
            inv_check  = map (\(_,f) -> Fx $ Cond f 
                                            (Just . Fx $ 
                                                RelExpr (Fx $ Relation RelNeq) 
                                                        (Fx $ ExprF "\'undt\'" (Fx Empty)))) (("",a):inv_replce)
        in  if null inv_check 
              then Fx $ Cond a (Just . Fx $ RelExpr rel expr)
              else 
                if length inv_check == 1
                    then Fx. Paren . Fx $ And (head inv_check) (Fx $ Cond a (Just . Fx $ RelExpr rel expr))
                    else Fx . Paren . Fx $ And (foldr1 (\x y -> Fx $ And x y) inv_check) (Fx $ Cond a (Just . Fx $ RelExpr rel expr))
   | (Cond a@(Fx (Invar _)) (Just (Fx (RelExpr rel expr)))) <- v =
        let bound = flipBound $ getBound rel
            invars = getInvolves expr
            inv_mappings = zip invars (map (`invarAnalysis` expr) invars)
            inv_replce = map (swapBound bound) inv_mappings
            inv_check  = map (\(_,f) -> Fx $ Cond f 
                                            (Just . Fx $ 
                                                RelExpr (Fx $ Relation RelNeq) 
                                                        (Fx $ ExprF "\'undt\'" (Fx Empty)))) (("",a'):inv_replce)
            a' = case bound of
                    Max -> Fx $ Function "minb" [a]
                    Min -> Fx $ Function "maxb" [a] 
        in  if null inv_check 
              then Fx $ Cond a' (Just . Fx $ RelExpr rel expr)
              else 
                if length inv_check == 1
                    then Fx. Paren . Fx $ And (head inv_check) (Fx $ Cond a' (Just . Fx $ RelExpr rel expr))
                    else Fx . Paren . Fx $ And (foldr1 (\x y -> Fx $ And x y) inv_check) (Fx $ Cond a' (Just . Fx $ RelExpr rel expr))
   | (InvarExpr (Fx (ExprF s e)) Nothing) <- v =
        case s of
            "undefined" -> Fx $ InvarExpr (Fx $ Function "set" [e, 
                                                                Fx $ ExprF "\'undt\'" (Fx Empty),
                                                                Fx $ ExprF "ind=\'Min\'" (Fx Empty)]) Nothing
            "not" -> Fx $ InvarExpr (Fx $ Function "set" [e, 
                                                          Fx $ ExprF "False" (Fx Empty)]) Nothing
            s@"even" -> evenOrOdd (s+"Invar") e
            s@"odd"  -> evenOrOdd (s+"Invar") e
   | (InvarExpr (Fx (Local l)) (Just (Fx (ExprF _ expr)))) <- v =
        Fx $ ExprF (l ++ " =") expr
   | (InvarExpr a (Just (Fx (RelExpr rel expr)))) <- v =
        let bound = getBound rel
            invars = getInvolves expr
            inv_mappings = zip invars (map (`invarAnalysis` expr) invars)
            inv_replce = map (swapBound bound) inv_mappings
            inv_check  = map (\(_,f) -> Fx $ Cond f 
                                            (Just . Fx $ 
                                                RelExpr (Fx $ Relation RelNeq) 
                                                        (Fx $ ExprF "\'undt\'" (Fx Empty)))) (inv_replce)
        in if null inv_check
             then Fx $ InvarExpr a (Just . Fx $ RelExpr rel expr)
             else 
                if length inv_check == 1 
                    then Fx $ If (head inv_check)
                                 (Fx $ InvarExpr a (Just . Fx $ RelExpr rel expr))
                                 Nothing
                    else Fx $ If (foldr1 (\x y -> Fx $ And x y) inv_check)
                          (Fx $ InvarExpr a (Just . Fx $ RelExpr rel expr))
                          Nothing
   | (Cond a Nothing) <- v =
        Fx $ Cond (Fx $ Function "get" [a]) (Just . Fx $ RelExpr (Fx $ Relation RelEq) (Fx $ ExprF "True" (Fx Empty)))
   | (InvarExpr a Nothing) <- v =
        Fx $ InvarExpr (Fx $ Function "set" [a, Fx $ ExprF "True" (Fx Empty)]) Nothing
   | otherwise = Fx v
   where
        swapBound Max (i, InvAn True _ _) = (i, Fx $ Function "minb" [Fx $ Invar i])
        swapBound Min (i, InvAn True _ _) = (i, Fx $ Function "maxb" [Fx $ Invar i])
        swapBound Min (i, _)            = (i, Fx $ Function "minb" [Fx $ Invar i])
        swapBound Max (i, _)            = (i, Fx $ Function "maxb" [Fx $ Invar i])
        evenOrOdd s e = Fx $ ExprList [
                            Fx $ If (Fx $ Cond (Fx $ Function "minb" [e])
                                               (Just . Fx $ RelExpr (Fx $ Relation RelNeq) 
                                                                     (Fx $ ExprF "\'undt\'" (Fx Empty))))
                                    (Fx $ If (Fx $ Function s [Fx $ Expr [Fx $ Function "minb" [e]
                                                                             , Fx $ Number 1]])
                                             (Fx $ InvarExpr (Fx $ Function "set" [e 
                                                                        ,    Fx $ Expr [Fx $ Function "minb" [e] 
                                                                                   ,    Fx $ Number 1]
                                                                        , Fx $ ExprF "ind=\'Min\'" (Fx Empty)])
                                                             Nothing)
                                             Nothing)
                                    Nothing,
                            Fx $ If (Fx $ Cond (Fx $ Function "maxb" [e])
                                               (Just . Fx $ RelExpr (Fx $ Relation RelNeq) 
                                                                     (Fx $ ExprF "\'undt\'" (Fx Empty))))
                                    (Fx $ If (Fx $ Function s [Fx $ Expr [Fx $ Function "maxb" [e]
                                                                             , Fx $ Neg $ Fx $ Number 1]])
                                             (Fx $ InvarExpr (Fx $ Function "set" [e 
                                                                        ,    Fx $ Expr [Fx $ Function "minb" [e] 
                                                                                   ,    Fx $ Neg $ Fx $ Number 1]
                                                                        , Fx $ ExprF "ind=\'Max\'" (Fx Empty)])
                                                             Nothing)
                                             Nothing)
                                    Nothing ]

realizeAnalysis' :: Theorem (Fix Theorem) -> Fix Theorem
realizeAnalysis' v
   | (Cond a (Just (Fx (RelExpr (Fx (Relation RelNeq)) expr)))) <- v =
        cata realizeAnalysis' . Fx . Paren . Fx $ Or (Fx $ Paren (Fx (Cond a (Just (Fx (RelExpr (Fx (Relation RelGt)) expr))))))
                                         (Fx $ Paren (Fx (Cond a (Just (Fx (RelExpr (Fx (Relation RelLt)) expr))))))
   | (Cond a (Just (Fx (RelExpr (Fx (Relation RelEq)) expr)))) <- v =
        cata realizeAnalysis' . Fx . Paren . Fx $ And (Fx (Cond a (Just (Fx (RelExpr (Fx (Relation RelGte)) expr)))))
                                         (Fx (Cond a (Just (Fx (RelExpr (Fx (Relation RelLte)) expr)))))
   | (Cond a@(Fx (Invar _)) (Just (Fx (RelExpr rel expr)))) <- v =
        let bound = flipBound $ getBound rel
            invars = getInvolves expr
            inv_mappings = zip invars (map (`invarAnalysis` expr) invars)
            inv_replce = map (swapBound bound) inv_mappings
            a' = case bound of
                    Max -> Fx $ Function "minb" [a]
                    Min -> Fx $ Function "maxb" [a] 
        in  Fx $ Cond a' (Just . Fx $ RelExpr rel $ replaceAllInvar inv_replce expr)
   | (InvarExpr a@(Fx (Invar _)) (Just (Fx (RelExpr rel expr)))) <- v =
        let bound = getBound rel
            invars = getInvolves expr
            inv_mappings = zip invars (map (`invarAnalysis` expr) invars)
            inv_replce = map (swapBound bound) inv_mappings
        in Fx $ InvarExpr a (Just . Fx $ RelExpr rel $ replaceAllInvar inv_replce expr)
   | otherwise = Fx v
   where
        swapBound Max (i, InvAn True _ _)  = (i, Fx $ Function "minb" [Fx $ Invar i])
        swapBound Min (i, InvAn True _ _)  = (i, Fx $ Function "maxb" [Fx $ Invar i])
        swapBound Max (i, InvAn False _ _) = (i, Fx $ Function "maxb" [Fx $ Invar i])
        swapBound Min (i, InvAn False _ _) = (i, Fx $ Function "minb" [Fx $ Invar i])
        swapBound Max (i, _)               = (i, Fx $ Invar i)
        swapBound Min (i, _)               = (i, Fx $ Invar i)
        evenOrOdd s e = Fx $ ExprList [
                            Fx $ If (Fx $ Cond (Fx $ Function "minb" [e])
                                               (Just . Fx $ RelExpr (Fx $ Relation RelNeq) 
                                                                     (Fx $ ExprF "\'undt\'" (Fx Empty))))
                                    (Fx $ If (Fx $ Function s [Fx $ Expr [Fx $ Function "minb" [e]
                                                                             , Fx $ Number 1]])
                                             (Fx $ InvarExpr (Fx $ Function "set" [e 
                                                                        ,    Fx $ Expr [Fx $ Function "minb" [e] 
                                                                                   ,    Fx $ Number 1]
                                                                        , Fx $ ExprF "ind=\'Min\'" (Fx Empty)])
                                                             Nothing)
                                             Nothing)
                                    Nothing,
                            Fx $ If (Fx $ Cond (Fx $ Function "maxb" [e])
                                               (Just . Fx $ RelExpr (Fx $ Relation RelNeq) 
                                                                     (Fx $ ExprF "\'undt\'" (Fx Empty))))
                                    (Fx $ If (Fx $ Function s [Fx $ Expr [Fx $ Function "maxb" [e]
                                                                             , Fx $ Neg $ Fx $ Number 1]])
                                             (Fx $ InvarExpr (Fx $ Function "set" [e 
                                                                        ,    Fx $ Expr [Fx $ Function "minb" [e] 
                                                                                   ,    Fx $ Neg $ Fx $ Number 1]
                                                                        , Fx $ ExprF "ind=\'Max\'" (Fx Empty)])
                                                             Nothing)
                                             Nothing)
                                    Nothing ]

swapBound Max (InvAn True _ _) = Min
swapBound Min (InvAn True _ _) = Max
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
generateSymPyIneq e@(Fx (InvarExpr i (Just relexp))) =
        case relexp of 
            (Fx (RelExpr r (Fx (Adden orig ann)))) ->
              let  (Fx (InvarExpr (Fx (Invar v)) (Just (Fx (RelExpr rel exp)))))    = func_map
                   (func_map, func_remap)                            = replaceAllFuncs (Fx $ InvarExpr i (Just (Fx $ RelExpr r orig)))
                   rationalFlag                                      = not $ containsFunc exp
                   inequality                                        = theoremToSrc exp
                   lhs                                               = v
                   relation                                          = theoremToSrc rel
                   bound                                             = getBound rel
                   invar_analyses                                    = map (alterAnalysis ann) . map (\i -> (i, getIneq . flipBound . swapBound bound . invarAnalysis i $ exp)) $ invars
                   invar_doanalysis                                  = concatMap (alterAnalysis2 ann) $ invars
                   invars                                            = getInvolves orig
              in fmap (map (adjustInequality invar_analyses) . ((replaceAllInvar invar_doanalysis . Fx $ InvarExpr i (Just (Fx $ RelExpr r orig))):) . map (replaceAllInvar func_remap) . theoremParser . lexer . concat) . sequence $
                     invars >>= \inv -> return $
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
            (Fx (RelExpr _ orig)) -> 
              let  (Fx (InvarExpr (Fx (Invar v)) (Just (Fx (RelExpr rel exp)))))    = func_map
                   (func_map, func_remap)                            = replaceAllFuncs e 
                   rationalFlag                                      = not $ containsFunc exp
                   inequality                                        = theoremToSrc exp
                   lhs                                               = v
                   relation                                          = theoremToSrc rel
                   bound                                             = getBound rel
                   invar_analyses                                    = map (\i -> (i, getIneq . flipBound . swapBound bound . invarAnalysis i $ exp)) invars
                   invars                                            = getInvolves orig
              in fmap (map (adjustInequality invar_analyses) . (e:) . map (replaceAllInvar func_remap) . theoremParser . lexer . concat) . sequence $
                     invars >>= \inv -> return $
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
            _  -> return [e]
        where
        alterAnalysis2 [] _ = []
        alterAnalysis2 (Fx (Function s [Fx (Invar j)]):anns) i  
                        | "useMinFor" == s && i == j = [(i, Fx $ Function "minb" [Fx $ Invar i])]
                        | "useMaxFor" == s && i == j = [(i, Fx $ Function "maxb" [Fx $ Invar i])]
                        | otherwise                  = alterAnalysis2 anns i
        alterAnalysis [] a = a
        alterAnalysis (Fx (Function s [Fx (Invar j)]):anns) (i, an)  
                        | "useMinFor" == s && i == j = (i, getIneq Max)
                        | "useMaxFor" == s && i == j = (i, getIneq Min)
                        | otherwise                  = alterAnalysis anns (i, an)
        adjustInequality imap ineq@(Fx (InvarExpr (Fx (Invar v)) (Just (Fx (RelExpr rel exp))))) =
                   maybe ineq (\r -> Fx $ InvarExpr (Fx $ Invar v) (Just . Fx $ RelExpr r exp)) (lookup v imap) 
        adjustInequality _    ineq                                                               = ineq
            
generateSymPyIneq e = return [e]
