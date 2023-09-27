import ply.yacc as yacc
import sys
from abin_lex import tokens


def p_S(p):
    "S: ABin"
    print(p[1])


def p_ABin_vazia(p):
    "ABin : PA PF"
    p[0] = 'null'


def p_ABin(p):
    "Abin : PA NUM ABin ABin PF"
    p[0] = '("{")'
    p[0] += '("\t\"root\": ", p[2], ",")'
    p[0] += '("\t\"left\": ", p[3], ",")'
    p[0] += '("\t\"right\": ", p[4])'
    p[0] += '("}")'


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
