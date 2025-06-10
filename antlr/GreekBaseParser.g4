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
    : KW_PRINT expression OP_SEMICOLON
    ;

assignment
    : IDENTIFIER OP_ASSIGN expression OP_SEMICOLON
    ;

variableDeclaration
    : IDENTIFIER OP_COLON varType (OP_ASSIGN expression)? OP_SEMICOLON;


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
    : KW_FUNCTION IDENTIFIER OP_LPAREN (IDENTIFIER OP_COLON literal (OP_COMMA IDENTIFIER OP_COLON literal)*)? OP_RPAREN KW_RETURN literal
      (KW_IS KW_BEGIN statement* KW_END KW_FUNCTION OP_SEMICOLON)
      |
      (KW_LCURL statement* KW_RCURL)
    ;

functionCall
    : IDENTIFIER OP_LPAREN (IDENTIFIER (OP_COMMA IDENTIFIER)*)? OP_RPAREN OP_SEMICOLON;

condition
    : expression relop expression
    | condition OP_OR condition
    | condition OP_AND condition
    ;


expression
    : expression OP_MUL expression     # mulExpr
    | expression OP_DIV expression     # divExpr
    | expression OP_MOD expression     # modExpr
    | expression OP_ADD expression     # addExpr
    | expression OP_SUB expression     # subExpr
    | OP_LPAREN expression OP_RPAREN   # parensExpr
    | IDENTIFIER                       # idExpr
    | literal                          # typeExpression
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