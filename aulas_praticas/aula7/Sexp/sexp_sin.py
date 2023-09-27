import ply.yacc as yacc
import sys
from sexp_lex import tokens, literals


def produtorio(lista):
    ac = 1
    for n in lista:
        ac *= n
    return ac


def somatorio(lista):
    ac = 0
    for n in lista:
        ac += n
    return ac


def p_Z(p):
    "Z : Sexp"
    print(p[1])


def p_Sexp_ad(p):
    "Sexp : '(' '+' Lista ')'"
    p[0] = somatorio(p[3])


def p_Sexp_mult(p):
    "Sexp : '(' '*' Lista ')'"
    p[0] = produtorio(p[3])


def p_Sexp_num(p):
    "Sexp : num"
    p[0] = p[1]


def p_Lista(p):
    "Lista : Lista Sexp"
    p[0] = p[1] + [p[2]]


def p_Lista_par(p):
    "Lista : Sexp Sexp"
    p[0] = [p[1], p[2]]


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
