import ply.yacc as yacc
import sys
from capicua_lex import tokens


def p_gramatica(p):
    """
    capicua : z capicua z
            | u capicua u
            | z
            | u
            |
    """


def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


parser = yacc.yacc()

for line in sys.stdin:
    parser.success = True
    parser.parse(line)
    if parser.success:
        print("Frase valida", line)
    else:
        print("Frase inválida", line)
