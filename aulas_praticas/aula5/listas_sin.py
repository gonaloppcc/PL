import ply.yacc as yacc
import sys
from listas_lex import tokens


def p_gramatica(p):
    """
    Lista : PA PF
          | PA NUM Elems PF

    Elems : Elem Resto

    Resto :
         | VIRG Elem

    Elem : NUM
         | Lista
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
