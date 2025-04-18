lexer grammar l_GreekBase;

ID  : [a-zA-Z][a-zA-Z0-9_]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
