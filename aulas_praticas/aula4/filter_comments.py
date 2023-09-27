import sys

import ply.lex as lex

states = (
    ('COM', 'exclusive'),
)

tokens = [
    'BCOM',  # Begin comment
    'ECOM',  # End comment
    'TEXT'  # Text
]


def t_BCOM(t):
    r'<!--'
    t.lexer.begin('COM')


def t_TEXT(t):
    r'.|\n'
    print(t.value, end='')


def t_COM_ECOM(t):
    r'-->'
    t.lexer.begin('INITIAL')


def t_COM_TEXT(t):
    r'.|\n'
    pass


# Analisador léxico
lexer = lex.lex()

for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        print(tok)
