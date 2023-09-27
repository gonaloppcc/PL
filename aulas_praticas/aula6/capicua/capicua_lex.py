import ply.lex as lex

# literals = ['0', '1']
# Ou
# literals = "01"

tokens = ['z', 'u']

t_z = r'0'

t_u = r'1'

t_ignore = ' \t\n'


def t_error(t):
    print("Caracter ilegal, ", t.value[0])
    t.lexer.skip(1)


lex.lex()
