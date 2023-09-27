# COMPILADOR

O compilador deve ser capaz de reconhecer os seguintes 3 programas.

```
print("Olá!")
```

```
int idade
str nome

idade = int(input("Introduza..."))
nome = input
print("Introduziste: ", idade, "e", nome)
```

```
int n1, n2

n1=int(input("Introduza 1 inteiro:"))
n2 = "

if(n1 > n2)
    print("O maior é:",n1)
else 
    print(("O maior é:",n2))
```

## QUESTÕES

Quais os símbolos terminais da linguagem?

```
T = {INT , STR , id , INPUT , PRINT , str , '=' , '(' , ')' , ','}
```

Definição da gramática:

```
Program -> Declarations Statements

Declarations -> Desclarations Declaration
              | Vazio
              
Declaration -> Type IdList

Type -> INT | STR

IdList -> id
        | IdList ',' id
        
Statements -> Statements Statement
            | Statement
            
Statement -> Atrib
           | Print
           
Atrib -> id '=' Exp

Print -> PRINT '(' PrintArgs ')'

PrintArgs -> PrintArgs ',' PrintArg
           | PrintArg
           
PrintArg -> id | str | Exp

Exp -> INPUT '(' str ')'
     | INT '(' Exp ')'
```

Implementação do If else

```
Statement -> IF '(' Cond ')' CondStatements
           | IF '(' Cond ')' CondStatements ELSE CondStatements
           
CondStatements -> Statement 
                | '{' Statements '}'
                
Cond -> Cond OR Cond2
      | Cond2
      
Cond2 -> Cond2 OR Cond3
       | Cond3
       

Cond3 -> NOT ExpRel
       | ExpRel
       
ExpRel -> Exp '>' Exp
        | ...
        
>
<
>= GE
<= LE
== EQ
NEQ !=
```

Resolução do conflito do if:

```
Statement -> IF '(' Cond ')' CondStatements ELSE

ELSE -> empty
      | ELSE CondStatements
```

