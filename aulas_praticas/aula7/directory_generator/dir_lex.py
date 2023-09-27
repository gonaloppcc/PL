import ply.lex as lex

literals = '[]()'

tokens = ['texto']


# r'\".+?\"'
def t_texto(t):
    r'\"[^"]\"'


t_ignore = ' \t\n'


def t_error(t):
    print("Caracter ilegal, ", t.value[0])
    t.lexer.skip(1)


lex.lex()
