# Definição de uma gramática para um programa

```
Calc -> Comando Comandos END

Comandos -> Vazio {END}
          | Comando Comandos {PRINT, READ, id, DUMP}

Comando -> PRINT Exp
         | READ id
         | id '=' Exp
         | DUMP
         
Exp -> Termo Exp2

Exp2 -> '+' Exp {'+'}
      | '-' Exp {'-'}
      | Vazio {')', END}
      
Termo -> Fator Termo2

Termo2 -> '*' Exp {'*'}
      | '/' Exp {'/'}
      | Vazio {'+', '-', ')', PRINT, READ, id, DUMP, END}
      
Fator -> id {id}
       | num {num}
       | '(' Exp ')' {'('}
```