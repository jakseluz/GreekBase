lexer grammar l_GreekBase;
// Keywords
KW_BEGIN      : 'begin';
KW_END        : 'end';
KW_IF         : 'if';
KW_THEN       : 'then';
KW_ELSE       : 'else';
KW_LOOP       : 'loop';
KW_WHILE      : 'while';
KW_FOR        : 'for';
KW_IN         : 'in';
KW_OUT        : 'out';
KW_RETURN     : 'return';
KW_PROCEDURE  : 'procedure';
KW_FUNCTION   : 'function';
KW_IS         : 'is';
KW_TYPE       : 'type';
KW_ARRAY      : 'array';
KW_OF         : 'of';
KW_CONST      : 'const';
KW_USE        : 'use';
KW_WITH       : 'with';
KW_NEW        : 'new';
KW_LCURL : '{';
KW_RCURL : '}';

// Symbols and operators
OP_ASSIGN     : ':=';
OP_EQUAL      : '=';
OP_NOT_EQUAL  : '/=';
OP_LESS       : '<';
OP_LESS_EQ    : '<=';
OP_GREATER    : '>';
OP_GREATER_EQ : '>=';
OP_PLUS       : '+';
OP_MINUS      : '-';
OP_MUL        : '*';
OP_DIV        : '/';
OP_MOD        : 'mod';
OP_AND        : 'and';
OP_OR         : 'or';
OP_NOT        : 'not';
OP_DOT        : '.';
OP_COLON      : ':';
OP_SEMICOLON  : ';';
OP_COMMA      : ',';
OP_ARROW      : '=>';
OP_LPAREN     : '(';
OP_RPAREN     : ')';
OP_LBRACKET   : '[';
OP_RBRACKET   : ']';

// Literals
LIT_INT       : [0-9]+;
LIT_FLOAT     : [0-9]+ '.' [0-9]+;
LIT_STRING    : '"' (~["\r\n])* '"';
LIT_CHAR      : '\'' [a-zA-Z0-9] '\'';

// Identifiers
IDENTIFIER    : [a-zA-Z_] [a-zA-Z0-9_]*;

// Comments
LINE_COMMENT      : '--' ~[\r\n]* -> skip;
MULTILINE_COMMENT : '/*' .*? '*/' -> skip;


//White spaces 

WS : [ \t\r\n]+ -> skip;



