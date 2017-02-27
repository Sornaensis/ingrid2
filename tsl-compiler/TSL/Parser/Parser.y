{
{-# LANGUAGE ScopedTypeVariables #-}
module TSL.Parser.Parser ( 
             theoremParser, 
             lexer
             ) where
import Data.Char
import TSL.AST.AST
}

%name theoremParser
%tokentype { Token }
%error { parseError }

%token 
      if             { TokenIf }
      then           { TokenThen }
      else           { TokenElse }
      null           { TokenNull }
      and            { TokenAnd }
      or             { TokenOr }
      not            { TokenNot }
      odd            { TokenOdd }
      even           { TokenEven }
      number         { TokenNum $$ }
      defined        { TokenDefined }
      undefined      { TokenUndefined }
      isset          { TokenIsset }
      istrue         { TokenIstrue }
      isfalse        { TokenIsfalse }
      global         { TokenGlobalName $$ }
      local          { TokenLocalName $$ }
      '=='           { TokenEq }
      '>='           { TokenGte }
      '<='           { TokenLte }
      '>'            { TokenGt }
      '<'            { TokenLt }
      '!='           { TokenNeq }
      '+'            { TokenPlus }
      '-'            { TokenMinus }
      '*'            { TokenTimes }
      '^'            { TokenPow }
      '/'            { TokenDiv }
      '{'            { TokenOB }
      '}'            { TokenCB }
      '('            { TokenOP }
      ')'            { TokenCP }
      ';'            { TokenSemiColon }
      ','            { TokenComma }

%%

Theorem : Invarexpr ';' Theorem    { $1 : $3 }
         | Ifstmt ';' Theorem      { $1 : $3 }
         | null ';' Theorem        { [Empty] }
         | {- empty -}             { [] }

Invarexpr  : not Invar       { ExprF     "not"       $2 }
           | even Invar      { ExprF     "even"      $2 }
           | odd Invar       { ExprF     "odd"       $2 }
           | undefined Invar { ExprF     "undefined" $2 }
           | Invar Invarel   { InvarExpr $1          $2 }

Invarel : Relation Expr { Just $ RelExpr $1 (Expr $2) }
        |               { Nothing }

Invarexprlist : '{' Invarexprlist1 '}'      { ExprList (reverse $2) }

Invarexprlist1 : Invarexpr                      { [$1] }
               | Ifstmt                         { [$1] }
               | Invarexprlist1 ',' Invarexpr   { $3 : $1 } 
               | Invarexprlist1 ',' Ifstmt      { $3 : $1 } 

Ifstmt : if Cond then Invarexprlist Elsestmt { If $2 $4 $5 }

Elsestmt : else Elsestmt1 { Just $2 }
         |                { Nothing }

Elsestmt1 : Ifstmt           { $1 }
          | Invarexprlist    { If (ExprF "not" (Local "True")) $1 Nothing }

Cond : Condand    { $1 }
     | Cond or Condand { Or $1 $3 }

Condand : Cond1   { $1 }
        | Condand and Cond1 { And $1 $3 }

Cond1 : Invar CondRel    { Cond $1 $2 }
      | istrue Expr      { CondF "istrue" (Expr $2) }
      | isfalse Expr     { CondF "isfalse" (Expr $2) }
      | not Invar        { CondF "not" $2 }
      | even Invar       { CondF "even" $2 }
      | odd Invar        { CondF "odd" $2 }
      | isset Invar      { CondF "isset" $2 }
      | defined Invar    { CondF "defined" $2 }
      | undefined Invar  { CondF "undefined" $2 }
      | '(' Cond ')'     { $2 }

CondRel : Relation Expr  { Just $ RelExpr $1 (Expr $2) }
        |                { Nothing }
 
Relation : '=='   { Relation $ RelEq  }
         | '>='   { Relation $ RelGte }
         | '<='   { Relation $ RelLte }
         | '!='   { Relation $ RelNeq }
         | '>'    { Relation $ RelGt  }
         | '<'    { Relation $ RelLt  }

Invar : global  { Invar $1 }

Localvar : local   { Local $1 }

Func : global '(' Arglist ')'  { Function $1 $3 }

Arglist : Arglist1 { reverse $1 }

Arglist1 : Expr              { [Expr $1] }
        | Arglist1 ',' Expr  { Expr $3 : $1 }
        |                   { [] } 

Expr : Expr1 { reverse $1 }

Expr1 : Term           { [$1] }
     | '-' Term        { [Neg $2] }
     | Expr1 '+' Term  { $3 : $1 }
     | Expr1 '-' Term  { (Neg $3) : $1 }

Term : Factor          { Term $1 }
     | Term '*' Factor { Mul $1 (Term $3) }
     | Term '/' Factor { Div $1 (Term $3) }

Factor : Val             { Value $1 }
       | Factor '^' Val  { Pow $1 (Value $3) } 

Val : Func   { $1 }
    | Invar  { $1 }
    | Localvar { $1 }
    | number { Number $1 }
    | '(' Expr ')' { Paren (Expr $2) }

{

-- Simple Error Facility. This will be replaced with line/column error reporting
parseError :: [Token] -> a
parseError _ = error "Parse error"

-- Declarative Datatype for representing Tokens
data Token
      = TokenIf
      | TokenThen
      | TokenNull
      | TokenElse
      | TokenDefined
      | TokenUndefined
      | TokenIsset
      | TokenIstrue
      | TokenIsfalse
      | TokenNum Double
      | TokenGlobalName String
      | TokenLocalName String
      | TokenAnd
      | TokenOr
      | TokenAll
      | TokenNone
      | TokenOne
      | TokenNot
      | TokenOdd
      | TokenEven
      | TokenSemiColon
      | TokenComma
      | TokenEq
      | TokenGte
      | TokenLte
      | TokenLt
      | TokenGt
      | TokenNeq
      | TokenPlus
      | TokenMinus
      | TokenTimes
      | TokenDiv
      | TokenPow
      | TokenOB
      | TokenCB
      | TokenOP
      | TokenCP
 deriving Show

-- Lexer for creating a stream of tokens from the input
lexer :: String -> [Token]
lexer [] = []
lexer (c:cs) 
      | isSpace c               = lexer cs
      | isAlpha c || c == '_'   = lexVar (c:cs)
      | isDigit c               = lexNum (c:cs)
lexer ('=':'=':cs) = TokenEq : lexer cs
lexer ('>':'=':cs) = TokenGte : lexer cs
lexer ('<':'=':cs) = TokenLte : lexer cs
lexer ('!':'=':cs) = TokenNeq : lexer cs
lexer ('*':'*':cs) = TokenPow : lexer cs
lexer ('<':cs) = TokenLt : lexer cs
lexer ('>':cs) = TokenGt : lexer cs
lexer ('+':cs) = TokenPlus : lexer cs
lexer ('^':cs) = TokenPow : lexer cs
lexer ('-':cs) = TokenMinus : lexer cs
lexer ('*':cs) = TokenTimes : lexer cs
lexer ('/':cs) = TokenDiv : lexer cs
lexer ('{':cs) = TokenOB : lexer cs
lexer ('}':cs) = TokenCB : lexer cs
lexer ('(':cs) = TokenOP : lexer cs
lexer (')':cs) = TokenCP : lexer cs
lexer (',':cs) = TokenComma : lexer cs
lexer (';':cs) = TokenSemiColon : lexer cs

lexNum cs = TokenNum num : lexer rest
      where [(num,rest)] = reads cs

lexVar cs =
   case span (\c -> isAlpha c || isDigit c || c == '_') cs of
      ("undefined",rest) -> TokenUndefined : lexer rest
      ("defined",rest)   -> TokenDefined : lexer rest
      ("isfalse",rest)   -> TokenIsfalse : lexer rest
      ("istrue",rest)    -> TokenIstrue : lexer rest
      ("isset",rest)     -> TokenIsset : lexer rest
      ("then",rest)      -> TokenThen : lexer rest
      ("null",rest)      -> TokenNull : lexer rest
      ("else",rest)      -> TokenElse : lexer rest
      ("even",rest)      -> TokenEven : lexer rest
      ("and",rest)       -> TokenAnd : lexer rest
      ("not",rest)       -> TokenNot : lexer rest
      ("odd",rest)       -> TokenOdd : lexer rest
      ("if",rest)        -> TokenIf : lexer rest
      ("or",rest)        -> TokenOr : lexer rest
      ('_':var,rest)     -> TokenLocalName ('_':var) : lexer rest
      (var,rest)         -> TokenGlobalName var : lexer rest

}
