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
exprAnalysis :: Expr -> String -> InvarBoundSwitch
exprAnalysis (Expr exps) inv = let analysis = L.nub $ filter (/=NotFound) . concatMap (\x -> termAnalysis x inv (Flip False)) $ exps
                               in if null analysis
                                   then NotFound
                                   else if length analysis > 1
                                         then Complex
                                         else head analysis

termAnalysis :: Term -> String -> InvarBoundSwitch -> [InvarBoundSwitch]
termAnalysis (Mul a b) inv f = termAnalysis a inv f ++ termAnalysis b inv f
termAnalysis (Div a b) inv f = termAnalysis a inv f ++ termAnalysis b inv (flipbound f)
termAnalysis (Neg a) inv f   = termAnalysis a inv (flipbound f)
termAnalysis (Term a) inv f  = factorAnalysis a inv f

factorAnalysis :: Factor -> String -> InvarBoundSwitch -> [InvarBoundSwitch]
factorAnalysis (Pow a b) inv f = factorAnalysis a inv f ++ factorAnalysis b inv f
factorAnalysis (Value v) inv f = return $ valueAnalysis v inv f

valueAnalysis :: Value -> String -> InvarBoundSwitch -> InvarBoundSwitch
valueAnalysis (Invar v)         s f   | s == v     = f
valueAnalysis (Function fun exps) s f | fun `L.elem` specialFunctions
                                                  = let fxprs = map (`exprAnalysis` s) exps
                                                    in if null fxprs
                                                        then NotFound
                                                        else
                                                            let f' = head fxprs in
                                                            case fun of
                                                              "max" -> if f' == Flip True then Minimize else Maximize
                                                              "min" -> if f' == Flip True then Maximize else Minimize
                                                              _     -> f'
                                      | otherwise = let fxprs = map (`exprAnalysis` s) exps
                                                   in if null fxprs
                                                       then NotFound
                                                       else if length fxprs > 1
                                                             then Complex
                                                             else if f == Flip True
                                                                   then flipbound $ head fxprs
                                                                   else head fxprs
                                      where
                                      specialFunctions = ["min","max"]
valueAnalysis (Paren p)         s f              = let an = exprAnalysis p s
                                                   in if f == Flip True
                                                       then flipbound an
                                                       else if f == Complex && an /= NotFound
                                                             then Complex
                                                             else an
valueAnalysis _                 _ _              = NotFound
--- | End Expression Analysis

--- | Degree Analysis
