# Exemplo de expressões 
# 2 + 3
# 2 - 5 + 3
# (2 * 2) + 5 / 7

import ply.lex as lex


tokens = [
    "PA", # Parênteses aberto
    "PF", # Parênteses fechado 
    "NUM", # Numero
    "ID", # Nome da variavel
    "OP" # Operador
]

# t_PA = r'\('

# Fazer em funções para evitar ambiguidade
def t_NUM(t):
    pass

# Caracteres a ignorar
t_ignore = '\n\t '

# Função de erro
def t_error(t):
    print(f"")
    t.lexer.skip(1) # Para continuar a analisar a string

# Analisador léxico
lexer = lex.lex()

import sys

for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        print(tok)

# LexToken (Tipo do caracter terminal, caracteres, linha, coluna)