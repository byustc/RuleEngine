grammar RuleEngine ;
import RuleEngineLex ;


statements : statement ( SEMI statement )* SEMI ;

statements_block : LBRACE statements RBRACE ;


statement : expression                             # exprStmt
          | action_exp                             # exprAction
          | assign_statement                       # assignStmt
          | if_statement                           # ifStmt
          ;

assign_statement : LOCAL_VAR ASSIGN expression     # assignLocal
                 | REF_VAR ASSIGN expression       # assignRef
                 | CHINESE_VAR ASSIGN expression   # assignChinese
                 ;

if_statement : IF LPAREN condition RPAREN condition_branch
               ( ELIF LPAREN condition RPAREN condition_branch )*
               ELSE condition_branch ;

condition : expression ;

condition_branch : statement                         # branchStmt
                 | statements_block                  # branchBlock
                 ;

action_exp: OPEN statement | CLOSE statement;


expression : expression POW  expression               # Pow
           | SUB expression                           # Uminus
           | expression MUL expression                # Mul
           | expression DIV expression                # Div
           | expression MOD expression                # Mod
           | expression FLOOR_DIV expression          # Floor_Div
           | expression ADD expression                # Add
           | expression SUB expression                # Sub
           | expression EQ expression                 # Eq
           | expression NE expression                 # Ne
           | expression GT expression                 # Gt
           | expression LT expression                 # Lt
           | expression GE expression                 # Ge
           | expression LE expression                 # Le
           | NOT expression                           # Not
           | expression AND expression                # And
           | expression OR expression                 # Or
           | LPAREN expression RPAREN                 # Paren
           | CHINESE_VAR                              # ChineseVar
           | REF_VAR                                  # RefVar
           | LOCAL_VAR                                # LocalVar
           | INT_LITERAL                              # IntLiteral
           | FLOAT_LITERAL                            # FloatLiteral
           | STRING_LITERAL                           # StringLiteral
           | STRING_LITERAL REF_VAR (STRING_LITERAL)* # StringLiteralRefVar
           | BOOLEAN_LITERAL                          # BooleanLiteral
           | NULL_LITERAL                             # NullLiteral
           | SUM LPAREN paralist RPAREN               # Sum
           | AVG LPAREN paralist RPAREN               # Avg
           | SQRT LPAREN paralist RPAREN              # Sqrt
           | LOG LPAREN paralist RPAREN               # Log
           | COUNT LPAREN paralist RPAREN             # Count
           | LEN LPAREN paralist RPAREN               # Len
           | MAX LPAREN paralist RPAREN               # Max
           | MIN LPAREN paralist RPAREN               # Min
           | SUBSTR LPAREN paralist RPAREN            # Substr
           | TRIM LPAREN paralist RPAREN              # Trim
           | IS_NUMBER LPAREN paralist RPAREN         # Is_number
           | IS_INT LPAREN paralist RPAREN            # Is_int
           | IS_NULL LPAREN paralist RPAREN           # Is_null
           | TO_STR LPAREN paralist RPAREN            # To_str
           | TO_INT LPAREN paralist RPAREN            # To_int
           | TO_FLOAT LPAREN paralist RPAREN          # To_float
           | TO_DATE LPAREN paralist RPAREN           # To_date
           | ADD_TO_DATE LPAREN paralist RPAREN       # Add_to_date
           | DATE_DIFF LPAREN paralist RPAREN         # Date_diff
           | SYSDATE LPAREN RPAREN                    # Sysdate
           ;

paralist : para (COMMA para)* ;
para : expression ;

