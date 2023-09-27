# Somador on/off:

# 1. No inicio o somador está ON;

# 2. Se apanhar ON -> passa a ON;

# 3 Se "OFF" -> passa a OFF;

# 4. Se "\d+" => Se on soma, Se off n faz nada

# 5. Se "=" -> Imprimir a soma


import ply.lex as lex


tokens = [
    "ON", # ON
    "OFF", # OFF
    "NUM", # Numero
    "PRINT" # Imprimir a soma
]

def t_ON(t):
    r'[oO][Nn]'
    t.lexer.semaforo = True

def t_OFF(t):
    r'[oO][fF][fF]'
    t.lexer.semaforo = False

def t_NUM(t):
    r'\d+'
    if t.lexer.semaforo:
        t.lexer.soma += int(t.value) 

def t_PRINT(t):
    r'='
    print("Soma:", t.lexer.soma)

# Caracteres a ignorar
t_ignore = '\n\t '

# Função de erro
def t_error(t):
    # print(f"")
    t.lexer.skip(1) # Para continuar a analisar a string


# Analisador léxico
lexer = lex.lex()

# Definição de estado
lexer.semaforo = True
lexer.soma = 0

import sys

for line in sys.stdin:
    lexer.af = 0
    lexer.input(line)
    for tok in lexer:
        print(tok)
