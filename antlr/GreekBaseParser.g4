parser grammar GreekBaseParser;

options {
    tokenVocab = GreekBaseLexer;
}

// Top-level program rule
program: statement* EOF;

// Types
literal
    : LIT_INT
    | LIT_FLOAT
    | LIT_CHAR
    | LIT_STRING
    | LIT_BOOL
    ;

// Statement can be either a non-declarative statement or a procedure declaration
statement
    : nonDeclarativeStatement
    | procedureDeclaration
    | functionDeclaration
    | expressionStatement
    | returnStatement
    ;

//statements that explicitly do not allow making declarations of functions or procedures
nonDeclarativeStatement
    :
    ifStatement
    | loopStatement
    | assignment
    | printStatement
    | variableDeclaration
    ;

expressionStatement
    : expression OP_SEMICOLON;


// ----statements----

// if statement
ifStatement
: KW_IF condition
    (
        (KW_THEN thenBranch+=nonDeclarativeStatement*
        (KW_ELSE elseBranch+=nonDeclarativeStatement*)?
        KW_END KW_IF OP_SEMICOLON)

        |

        ( KW_LCURL thenBranch+=nonDeclarativeStatement*
        (KW_ELSE elseBranch+=nonDeclarativeStatement*)?
        KW_RCURL)
    )
    ;

// while loop 
loopStatement
    : KW_WHILE condition
    (
        (KW_LOOP nonDeclarativeStatement* (KW_END KW_LOOP OP_SEMICOLON))

        |

        (KW_LCURL nonDeclarativeStatement* KW_RCURL)
    )
    ;

// print statement
printStatement
    : KW_PRINT (IDENTIFIER | literal | functionCall) OP_SEMICOLON
    ;

assignment
    : IDENTIFIER OP_ASSIGN expression OP_SEMICOLON
    ;

variableDeclaration
    : IDENTIFIER OP_COLON varType (OP_ASSIGN (expression | condition))? OP_SEMICOLON;



returnStatement
    : KW_RETURN literal OP_SEMICOLON;

// ----procedure specific things----

//TODO (or not TODO, that is the question...): our procedure declaration doesn't have declarative part yet e.g. you have to declare temporary values in body of the procedure

//formal parameter part is for defining in and out variables
formalParameterPart
    : OP_LPAREN parameterSpecification (OP_SEMICOLON parameterSpecification)* OP_RPAREN ;

//parameter specification is for definining which variables should have what mode and what type
parameterSpecification
    : IDENTIFIER (OP_COMMA IDENTIFIER)* OP_COLON modeSpecifier literal;

//modes can be either in, out or in out
modeSpecifier
    : KW_IN
    | KW_OUT
    | KW_IN KW_OUT
    ;

//procedure declaration
procedureDeclaration
    : KW_PROCEDURE IDENTIFIER formalParameterPart? KW_IS KW_BEGIN
    nonDeclarativeStatement*
    KW_END KW_PROCEDURE OP_SEMICOLON
    ;


// ---- function ----

// function declaration
functionDeclaration
    : KW_FUNCTION IDENTIFIER OP_LPAREN (variableDeclaration (OP_COMMA variableDeclaration)*)? OP_RPAREN (KW_RETURN varType)?
    (
        (KW_IS KW_BEGIN statement* KW_END KW_FUNCTION OP_SEMICOLON)
        |
        (KW_LCURL statement* KW_RCURL)
    )
    ;

functionCall
    : call_name+=IDENTIFIER OP_LPAREN (params+=expression (OP_COMMA params+=expression)*)? OP_RPAREN;

/*
condition
    : left_expr=expression relop right_expr=expression
    | condition OP_OR condition
    | condition OP_AND condition
    | OP_NOT negated=condition
    ;
*/
condition : conditionOr;

conditionOr
    : conditionAnd (OP_OR conditionAnd)*
    ;

conditionAnd
    : conditionNot (OP_AND conditionNot)*
    ;

conditionNot
    : OP_NOT conditionNot
    | conditionAtom
    ;

conditionAtom
    : expression relop expression
    | OP_LPAREN condition OP_RPAREN
    ;


expression : addExpr;

addExpr
    : mulExpr ( (OP_ADD | OP_SUB) mulExpr )*
    ;

mulExpr
    : atom ( (OP_MUL | OP_DIV | OP_MOD) atom )*
    ;

atom
    : functionCall
    | IDENTIFIER
    | literal
    | OP_LPAREN expression OP_RPAREN
    ;

relop
    : OP_EQUAL
    | OP_NOT_EQUAL
    | OP_LESS
    | OP_LESS_EQ
    | OP_GREATER
    | OP_GREATER_EQ
    ;

varType
    : KW_INT
    | KW_FLOAT
    | KW_CHAR
    | KW_STRING
    | KW_BOOL
    ;