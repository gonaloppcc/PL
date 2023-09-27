import ply.lex as lex

tokens = [
    'PA',  # Parenteses abertos
    'PF',  # Parenteses fechados
    'NUM'  # Numero
]

t_PA = r'\('
t_PF = r'\)'
t_NUM = r'\d+'

t_ignore = ' \t\n'


def t_error(t):
    print("Caracter ilegal, ", t.value[0])
    t.lexer.skip(1)


lex.lex()
