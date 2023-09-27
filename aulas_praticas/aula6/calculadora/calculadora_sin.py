import ply.yacc as yacc
import sys
from calculadora_lex import tokens, literals


def p_Comandos_Lista(p):
    "Comandos : Comandos Comando"


def p_Comandos_Simples(p):
    "Comandos : Comando"


def p_Comando_Atrib(p):
    "Comando : id '=' Exp"
    p.parser.registos[p[1]] = p[3]


def p_Comando_Escrita(p):
    "Comando : '!' Exp"
    print(p[2])


def p_Comando_Leitura(p):
    "Comando : '?' id"
    p.parser.registos[p[2]] = int(input('Introduza o valor inteiro:'))


def p_Comando_dump(p):
    "Comando : DUMP"
    print(p.parser.registos)


def p_Exp_ad(p):
    "Exp : Exp '+' Termo"
    p[0] = p[1] + p[3]


def p_Exp_sub(p):
    "Exp : Exp '-' Termo"
    p[0] = p[1] - p[3]


def p_Exp_Termo(p):
    "Exp : Termo"
    p[0] = p[1]


def p_Termo_mul(p):
    "Termo : Termo '*' Fator"
    p[0] = p[1] * p[3]


def p_Termo_div(p):
    "Termo : Termo '/' Fator"
    if p[3] != 0:
        print('Erro: divisão por 0...')

    else:
        p[0] = p[1] / p[3]


def p_Termo_Fator(p):
    "Termo : Fator"
    p[0] = p[1]


def p_Fator_grupo(p):
    "Fator : '(' Exp ')'"
    p[0] = p[2]


def p_Fator_num(p):
    "Fator : num"
    p[0] = p[1]


def p_Fator_id(p):
    "Fator : id"
    if p[1] in p.parser.registos.keys():
        p[0] = p.parser.registos[p[1]]

    else:
        print('Erro: Não existe o registo - ', p[1])
        p[0] = 0


def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


parser = yacc.yacc()

parser.registos = {}

for line in sys.stdin:
    parser.success = True
    parser.parse(line)
