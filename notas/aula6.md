# Aula 6

### Expressões regulares

> Definem linguagens regulares que podem ser descritos por autómatos finitos deterministas

### Grámaticas regulares

> Regras para a construção de frases


```(T, N, S, P)```

> T → Tokens / palavras

> N → Símbolos não terminais

> S → Símbolo especial

> P → Regras de construção de uma frase

#### Exemplo 1

Frases de uma linguagem:

```
()
(())
(())()((()))
```

```
T = {')', '('}

N = {}

P = { S -> ...}
```

#### Exemplo 2

Frases de uma linguagem:

```
[]
[1]
[1, 2, 3]
```

```
T = {'[', ']', inteiro, ','}

N = {S, Conteudo, Cont}

P = { S -> '[' Conteudo ']'
    Conteudo -> inteiro cont
              | vazio
    Cont -> vazio
          | ',' inteiro Cont
}
```

Devido à segunda produção derivada de `Cont` podemos dizer que a linguagem não é regular.

#### Símbolos terminais

1. Sinais constituidos por um caracter
2. Palavras reservadas: strings constantes
3. Terminais variáveis: identificadores, inteiros, etc...

---

> Estado final == Estado de aceitação

`inteiro = (\+|-)?\d+`

Tabela do autómato:

|      | +   | -   | d   |
|------|-----|-----|-----|
| \> S | A   | A   | B   |
| A    | -   | -   | B   |
| *B   | -   | -   | B   |

> O símbolo `>` é usado para identificar o estado inicial.

> O símbolo `*` é usado para identificar os estados finais ou de aceitação.

#### Derivação da gramática a partir da tabela:

```
S -> '+' A
   | '-' A 
   | d B
   
A -> d B

B -> d B
```

---

```
Automáto finito de estados:
Q - Conjunto de estados
Σ - alfateto
q0 - estado inicial
A - conjunto de estados finais / aceitação
A está contido em Q
ð - Q x Σ -> Q
```