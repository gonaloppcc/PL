import ply.lex as lex
import sys

states = [('marcado', 'inclusive')]
tokens = ('MA', 'MF', 'MARCA', 'IGN')


def t_MA(t):
    r'\<[^>]+\>'
    t.lexer.begin('marcado')


def t_IGN(t):
    r'.|\n'
    print(f'IGN: {t.value}')


t_ignore = ' \t\r\n'


def t_marcado_MF(t):
    r'\<\/[^>]+\>'
    print(t.lexer.conteudo)
    t.lexer.conteudo = ""
    t.lexer.begin('INITIAL')


def t_marcado_MARCA(t):
    r'.|\n'
    t.lexer.conteudo += t.value


t_marcado_ignore = ''


def t_error(t):
    t.lexer.skip(1)


lexer = lex.lex()
lexer.conteudo = ""
for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        pass
