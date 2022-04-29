lexer grammar RuleEngineLex;

INT_LITERAL : [0-9]+ ;
FLOAT_LITERAL : ('0'..'9')+ '.' ('0'..'9')* EXPONENT?
      | '.' ('0'..'9')+ EXPONENT?
      | ('0'..'9')+ EXPONENT
      ;

fragment
EXPONENT : ('e'|'E') ('+'|'-')? ('0'..'9')+ ;

STRING_LITERAL : '"' ( ESC | ~('\\'|'"') )* '"' ;
/*STRING_LITERAL : '"' ( ESC | .)*? '"' ;*/
fragment
ESC : '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\\') ;
/*ESC : '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\''|'\\') ;*/
/*ESC : '\\"' | '\\\\';*/

BOOLEAN_LITERAL : 'True' | 'true' | 'False' | 'false' ;

NULL_LITERAL : 'null';

SUM : 'sum';

AVG : 'avg';

SQRT : 'sqrt';

LOG : 'log';

COUNT : 'count';

LEN : 'len';

MAX : 'max';

MIN : 'min';

SUBSTR : 'substr';

TRIM : 'trim';

IS_NUMBER : 'is_number';

IS_INT : 'is_int';

IS_NULL : 'is_null';

TO_STR : 'to_str';

TO_INT : 'to_int';

TO_FLOAT : 'to_float';

TO_DATE : 'to_date';

ADD_TO_DATE : 'add_to_date';

DATE_DIFF : 'date_diff';

SYSDATE : 'sysdate';


OPEN : '打开';

CLOSE :  '关闭';

IF : 'if' | '当';

ELIF : 'elif' ;

ELSE : 'else' ;

CHINESE_VAR : [\u4E00-\u{9FA5}]+ ;

LOCAL_VAR : ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')* ;

REF_VAR : '$' ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')* ;

ADD : '+' ;

SUB : '-' ;

MUL : '*' ;

DIV : '/' ;

FLOOR_DIV : '//' ;

MOD : '%' ;

POW : '**' ;

ASSIGN : '=' ;

NOT : '!' ;

AND : '&&' ;

OR : '||' ;

EQ : '==' ;

NE : '!=' ;

GT : '>' ;

LT : '<' ;

GE : '>=' ;

LE : '<=' ;

LPAREN : '(' ;

RPAREN : ')' ;

LBRACE : '{' ;

RBRACE : '}' ;

SEMI : ';' ;

COMMA : ',' ;

BLOCK_COMMENT : '/*' .*? '*/' -> channel(HIDDEN) ;

WS : [ \r\t\u000C\n]+ -> channel(HIDDEN) ;

LINE_COMMENT : '//' ~[\r\n]* '\r'? '\n' -> channel(HIDDEN) ;

