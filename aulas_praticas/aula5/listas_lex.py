import sys
import re

import ply.lex as lex

tokens = [
    'PA',  # Parênteses abertos
    'PF',  # Parênteses fechados
    'NUM',  # Número
    'VIRG',  # Vírgula
]

t_PA = r'\['
t_PF = r'\]'
t_NUM = r'\d+'
t_VIRG = r','

t_ignore = ' \t\n'


def t_error(t):
    print("Caracter ilegal, ", t.value[0])
    t.lexer.skip(1)


lex.lex()
