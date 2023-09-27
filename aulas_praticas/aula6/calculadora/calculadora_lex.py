import ply.lex as lex

literals = ['+', '-', '*', '/', '(', ')', '=', '?', '!']

tokens = ['id', 'num', 'DUMP']

t_id = r'[_a-zA-Z]\w*'

t_DUMP = r'!!'


def t_num(t):
    r'\d+'
    t.value = int(t.value)

    return t


t_ignore = ' \t\n'


def t_error(t):
    print("Caracter ilegal, ", t.value[0])
    t.lexer.skip(1)


lex.lex()
