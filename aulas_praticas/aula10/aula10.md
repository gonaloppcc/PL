# Implementar while

## Exemplos

```
while(a < 10)
    i = i + 1
```

```
while(!)
    
```

## Definição da gramática

```
T = {WHILE, '(', ')'}

While -> WHILE '(' Cond ')' CondStatements
```

## Geração de código

### Formas de gerar código

1. T. D. Sintaxe : Código fonte -> parser -> código
2. Geração de uma estrutura media (AST) : Código fonte -> parser -> AST -> código

---

1. > print(4)

    ```
    start
      pushi 4
      writei
    stop
    ```
2. > Print exemplos

   ```
   print(4 * 23)
   print("Dois inteiros :", a, 3 + b)
   print(2, 3 + 1, 7)
   ```

   > print(2, 3 + 1, 7)
   ```
   start
      pushi 2
      writei
   
      pushi 3
      pushi 1
      add
      writei
   
      pushi 7
      writei
   stop
   ```

3. > Ler 3 inteiros e dizer qual é o maior

```
int a, b, c
```

### Tabela de símbolos

```
ts = {'a' : 
   {'type' : 'int', 'pos': 0},
   {'b' : 
   {'type' : 'int', 'pos': 1},
   ...
}
   
```