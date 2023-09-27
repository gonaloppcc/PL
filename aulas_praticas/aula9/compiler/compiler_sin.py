import ply.yacc as yacc
import sys
from compiler_lex import tokens, literals


def p_Z(p):
    "Program : Declarations Statements"


def p_Declarations_list(p):
    "Declarations : Declarations Declaration"


def p_Declarations_empty(p):
    "Declarations : "


def p_Declaration(p):
    "Declaration : Type IdList"


def p_Type_int(p):
    "Type : INT"


def p_Type_str(p):
    "Type : STR"


def p_IdList_list(p):
    "IdList : IdList ',' id"


def p_IdList_single(p):
    "IdList : id"


def p_Statements_list(p):
    "Statements : Statements Statement"


def p_Statements_single(p):
    "Statements : Statement"


def p_Statements_atrib(p):
    "Statement : id '=' Exp"


def p_Statements_print(p):
    "Statement : PRINT '(' PrintArgs ')'"


def p_PrintArgs_list(p):
    "PrintArgs : PrintArgs ',' PrintArgs"


def p_PrintArgs_single(p):
    "PrintArgs : PrintArg"


def p_PrintArgs_str(p):
    "PrintArg : str"


def p_PrintArgs_exp(p):
    "PrintArg : Exp"


def p_Exp_int(p):
    "Exp : INT '(' Exp ')'"


def p_Exp_str(p):
    "Exp : INPUT '(' str ')'"


def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


parser = yacc.yacc()

parser.success = True

program = sys.stdin.read()
parser.parse(program)
if parser.success:
    print("Program structural correct!")
else:
    print('Program with errors! Try to resolve and try again!')
