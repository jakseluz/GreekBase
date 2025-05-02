parser grammar p_GreekBase;

options {
    tokenVocab = l_GreekBase;
}

// Top-level program rule
program: statement* EOF;

// Statement can be either an if-statement or an assignment or loop statement or procedure declaration
statement
    : ifStatement
    | loopStatement
    | assignment
    | procedureDeclaration
    ;
literal
    : LIT_INT
    | LIT_FLOAT
    | LIT_CHAR
    | LIT_STRING
    ;

// if statement
ifStatement
: KW_IF condition
    (
        (KW_THEN statement*
        (KW_ELSE statement*)?
        KW_END KW_IF OP_SEMICOLON)

        |

        ( KW_LCURL statement*
        (KW_ELSE statement*)?
        KW_RCURL)
    )
    ;
// while loop 
loopStatement
    : KW_WHILE condition
    (
        (KW_LOOP statement* (KW_END KW_LOOP OP_SEMICOLON))

        |

        (KW_LCURL statement* KW_RCURL)
    )
    ;


assignment
    : IDENTIFIER OP_ASSIGN expression OP_SEMICOLON
    ;
// ----procedure specific things----
//TODO: our procedure declaration doesn't have declarative part yet e.g. you have to declare temporary values in body of the procedure
//statements allowed in procedure block
procedureStatement
    :
    ifStatement
    | loopStatement
    | assignment
    ;
//formal parameter part is for defining in and out variables
formalParameterPart
    :
    OP_LPAREN parameterSpecification (OP_SEMICOLON parameterSpecification)* OP_RPAREN ;
//parameter specification is for definining which variables should have what mode and what type
parameterSpecification
    : IDENTIFIER (OP_COMMA IDENTIFIER)* OP_COLON modeSpecifier literal
    ;
//modes can be either in, out or in out
modeSpecifier
    : KW_IN
    | KW_OUT
    | KW_IN KW_OUT
    ;
//procedure declaration
procedureDeclaration
    : KW_PROCEDURE IDENTIFIER formalParameterPart? KW_IS KW_BEGIN
    procedureStatement*
    KW_END KW_PROCEDURE OP_SEMICOLON
    ;
// ---- function ----
// function declaration
functionDeclaration
    : KW_FUNCTION IDENTIFIER OP_LPAREN (IDENTIFIER (OP_COMMA IDENTIFIER)*)? OP_RPAREN
      OP_COLON IDENTIFIER
      KW_IS KW_BEGIN statement* KW_END KW_FUNCTION OP_SEMICOLON
    ;
condition
    : expression relop expression
    ;

expression
    : IDENTIFIER
    | LIT_INT
    | LIT_FLOAT
    | LIT_STRING
    ;

relop
    : OP_EQUAL
    | OP_NOT_EQUAL
    | OP_LESS
    | OP_LESS_EQ
    | OP_GREATER
    | OP_GREATER_EQ
    ;
