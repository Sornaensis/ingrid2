module TSL.Compiler.Analysis (
                    exprAnalysis,
                    InvarBoundSwitch(..),
                    swap
                    ) where

import qualified Data.List      as L
import qualified Data.Set       as S

import           TSL.AST.AST
import           TSL.Compiler.Types


data InvarBoundSwitch = Flip Bool | NotFound | Complex | Maximize | Minimize deriving Eq

swap :: Bound -> InvarBoundSwitch -> Bound
swap Max (Flip True) = Min
swap Min (Flip True) = Max
swap Min Maximize    = Max
swap b   _           = b

flipbound :: InvarBoundSwitch -> InvarBoundSwitch
flipbound (Flip a) = Flip $ not a
flipbound NotFound = Flip True
flipbound a        = a

--- | Expression Analysis
invarAnalysis

theoremAnalysis :: Theorem a -> String -> InvarBoundSwitch -> InvarBoundSwitch
theoremAnalysis (Expr exps) inv f = let analysis = L.nub $ filter (/=NotFound) . concatMap (\x -> theoremAnalysis x inv f) $ exps
                               in if null analysis
                                   then NotFound
                                   else if length analysis > 1
                                         then Complex
                                         else head analysis
theoremAnalysis (Mul a b) inv f = theoremAnalysis a inv f ++ theoremAnalysis b inv f
theoremAnalysis (Div a b) inv f = theoremAnalysis a inv f ++ theoremAnalysis b inv (flipbound f)
theoremAnalysis (Neg a) inv f   = theoremAnalysis a inv (flipbound f)
theoremAnalysis (Term a) inv f  = theoremAnalysis a inv f
theoremAnalysis (Pow a b) inv f = theoremAnalysis a inv f ++ theoremAnalysis b inv f
theoremAnalysis (Value v) inv f = return $ theoremAnalysis v inv f
theoremAnalysis (Invar v)         s f   | s == v     = f
theoremAnalysis (Function fun exps) s f | fun `L.elem` specialFunctions
                                                  = let fxprs = map (`theoremAnalysis` s) exps
                                                    in if null fxprs
                                                        then NotFound
                                                        else
                                                            let f' = head fxprs in
                                                            case fun of
                                                              "max" -> if f' == Flip True then Minimize else Maximize
                                                              "min" -> if f' == Flip True then Maximize else Minimize
                                                              _     -> f'
                                      | otherwise = let fxprs = map (`theoremAnalysis` s f) exps
                                                   in if null fxprs
                                                       then NotFound
                                                       else if length fxprs > 1
                                                             then Complex
                                                             else head fxprs
                                      where
                                      specialFunctions = ["min","max"]
theoremAnalysis (Paren p)         s f              = theoremAnalysis p s f
theoremAnalysis _                 _ _              = NotFound
--- | End Expression Analysis

--- | Degree Analysis
