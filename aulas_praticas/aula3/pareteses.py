from ast import type_ignore
import ply.lex as lex

# ()
# ()(())
# ()()()

# Para contar os parenteses
# af = 0

tokens = [
    "PA", # Parênteses aberto
    "PF", # Parênteses fechado 
]

def t_PA(t):
    r'\('
    t.lexer.af += 1
    return t

def t_PF(t):
    r'\)'
    t.lexer.af -= 1
    if t.lexer.af < 0:
        print("Erro: paretesis a fechar sem ter aberto...")
        t.lexer.af = 0
    return t

# Caracteres a ignorar
t_ignore = '\n\t '

# Função de erro
def t_error(t):
    print(f"")
    t.lexer.skip(1) # Para continuar a analisar a string


# Analisador léxico
lexer = lex.lex()

# Definição de estado
lexer.af = 0

import sys

for line in sys.stdin:
    lexer.af = 0
    lexer.input(line)
    for tok in lexer:
        print(tok)
