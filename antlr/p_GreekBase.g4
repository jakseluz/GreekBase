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

// if statement
ifStatement
: KW_IF condition
    (
        (KW_THEN statement*
        (KW_ELSE statement*)?
        KW_END KW_IF OP_SEMICOLON)

        |

        ('{' statement*
        (KW_ELSE statement*)?
        '}')
    )
    ;
// while loop 
loopStatement
    : KW_WHILE condition
    (
        (KW_LOOP statement* (KW_END KW_LOOP OP_SEMICOLON))

        |

        ('{' statement* '}')
    )
    ;


assignment
    : IDENTIFIER OP_ASSIGN expression OP_SEMICOLON
    ;

//procedure declaration
procedureDeclaration
    : KW_PROCEDURE IDENTIFIER KW_IS KW_BEGIN statement* KW_END KW_PROCEDURE OP_SEMICOLON
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
