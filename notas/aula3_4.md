# Aula 3 e 4

### Expressão regular para inteiro

`Int = ('-'|'+')?('0'|...|'9')`

### Expressão regular para binário

`Binário = (0|1)*`

### Minúsculas

`[a-z]`

### Maiusculas

`[A-Z]`

### Raw String em Python

```py
string = r'\n'
```

### Métodos de Match

-   `match()` \- MatchObject com o inicio da linha com a primeira ocorrência

-   `fullmatch()` \- MatchObject com o inicio da linha e fim de linha com a primeira ocorrência

-   `search()` \- MatchObject com a primeira ocorrência

-   `findall()` \- Lista de substrings que fizeram match

-   `finditer()` \- Um iterador com vários MatchObject

### Propriedades do MatchObject

-   `.groups()` \- Ver o subgrupos

-   `.groupdict()` \- Ver o subgrupos num dicionário organizados por nome.

-   `.group()` \- Ver o grupo completo

-   `.span()` \- Ver o index de inicio e de fim

-   `.start()` \- Ver o index de inicio

-   `.end()` \- Ver o index de fim

-   `.string()` \- Ver a string que procuramos onde
