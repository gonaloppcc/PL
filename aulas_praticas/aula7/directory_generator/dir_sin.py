import ply.yacc as yacc
import sys
from dir_lex import tokens, literals


def p_Z(p):
    "Z : Dir"
    print(*p[1])


def p_Dir_Pasta(p):
    "Dir : '(' texto Conteudo ')'"
    p[0] = [f'mkdir {p[2]}', f'cd {p[2]}' + p[3] + 'cd ..']


def p_Dir_Ficheiro(p):
    "Dir : Ficheiro"
    p[0] = [p[1]]


def p_Conteudo(p):
    "Conteudo : Conteudo Dir"
    p[0] = p[1] + p[2]


def p_Conteudo_vazio(p):
    "Conteudo : "
    p[0] = []


def p_Ficheiro(p):
    "Ficheiro : '[' texto texto ']'"
    p[0] = f'cp {p[3]} {p[2]}'


def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


parser = yacc.yacc()

lines = ""

for line in sys.stdin:
    lines += line

parser.parse(lines)
