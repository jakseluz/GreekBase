parser grammar GreekBase;

options {
    tokenVocab = l_GreekBase;
}

// Top-level program rule
program: statement* EOF;

// Statement can be either an if-statement or an assignment
statement: ifStatement | assignment;

// if with optional elsif and else
ifStatement
    : 'if' condition 'then' statement*
      ('elsif' condition 'then' statement*)*
      ('else' statement*)?
      'end' 'if' ';'
    ;


assignment
    : ID ':=' expr ';'
    ;

condition
    : expr relop expr
    ;

expr
    : ID
    | INT
    ;

relop
    : '>'
    | '<'
    | '>='
    | '<='
    | '='
    | "/="
    ;
