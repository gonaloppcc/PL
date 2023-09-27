import ply.yacc as yacc
from lp_lex import tokens, literals


def p_Program(p):
    "Program : Declarations Statements"
    p[0] = p[1] + "start\n" + p[2] + "stop\n"


def p_Declarations_list(p):
    "Declarations : Declarations Declaration"
    p[0] = p[1] + p[2]


def p_Declarations_empty(p):
    "Declarations : "
    p[0] = ""


def p_Declaration(p):
    'Declaration : Type IdList'
    res = ""
    for id in p[2]:
        if p[1] == 'int':
            p.parser.ts[id] = {'type': 'int', 'pos': p.parser.contaPos}
            res += "\tpushi 0\n"
        else:
            p.parser.ts[id] = {'type': 'str', 'pos': p.parser.contaPos}
            res += "\tpushs \"\"\n"
        p.parser.contaPos += 1
    p[0] = res


def p_Type_int(p):
    'Type : INT'
    p[0] = p[1]


def p_Type_str(p):
    'Type : STR'
    p[0] = p[1]


def p_IdList_list(p):
    "IdList : IdList ',' id"
    p[0] = p[1] + [p[3]]


def p_IdList_single(p):
    "IdList : id"
    p[0] = [p[1]]


def p_Statements_list(p):
    "Statements : Statements Statement"
    p[0] = p[1] + p[2]


def p_Statements_single(p):
    "Statements : Statement"
    p[0] = p[1]


def p_Statement_atrib(p):
    "Statement : id '=' Exp"
    p[0] = p[3] + "\tstoreg " + str(p.parser.ts[p[1]]['pos']) + "\n"


def p_Statement_print(p):
    "Statement : PRINT '(' PrintArgs ')'"
    p[0] = p[3]


def p_PrintArgs_list(p):
    "PrintArgs : PrintArgs ',' PrintArg"
    p[0] = p[1] + p[3]


def p_PrintArgs_single(p):
    "PrintArgs : PrintArg"
    p[0] = p[1]


def p_PrintArg_str(p):
    "PrintArg : str"
    p[0] = "\tpushs " + p[1] + "\n\twrites\n"


def p_PrintArg_exp(p):
    "PrintArg : Exp"
    p[0] = p[1] + "\twritei\n"


def p_Exp_ad(p):
    "Exp : Exp '+' Term"
    p[0] = p[1] + p[3] + "\tadd\n"


def p_Exp_sub(p):
    "Exp : Exp '-' Term"
    p[0] = p[1] + p[3] + "\tsub\n"


def p_Exp_term(p):
    "Exp : Term"
    p[0] = p[1]


def p_Term_mul(p):
    "Term : Term '*' Factor"
    p[0] = p[1] + p[3] + "\tmul\n"


def p_Term_div(p):
    "Term : Term '/' Factor"
    p[0] = p[1] + p[3] + "\tdiv\n"


def p_Term_factor(p):
    "Term : Factor"
    p[0] = p[1]


def p_Factor_int(p):
    "Factor : INT '(' Exp ')'"
    p[0] = p[3] + "\tatoi\n"


def p_Factor_input(p):
    "Factor : INPUT '(' str ')'"
    p[0] = "\tpushs " + p[3] + "\n\twrites\n\tread\n"


def p_Factor_id(p):
    "Factor : id"
    p[0] = "\tpushg " + str(p.parser.ts[p[1]]['pos']) + "\n"


def p_Factor_num(p):
    "Factor : num"
    p[0] = "\tpushi " + p[1] + "\n"


def p_Statement_while(p):
    "Statement : WHILE '(' Cond ')' CondStatements"
    p.parser.contaWhiles += 1
    p[0] = "while" + str(p.parser.contaWhiles) + ":\n"
    p[0] += p[3] + "\tjz endwhile" + str(p.parser.contaWhiles) + "\n"
    p[0] += p[5] + "\tjump while" + str(p.parser.contaWhiles) + "\n"
    p[0] += "endwhile" + str(p.parser.contaWhiles) + ":\n"


def p_Statement_if(p):
    "Statement : IF '(' Cond ')' CondStatements"
    p.parser.contaIfs += 1
    p[0] = p[3] + "\tjz endif" + str(p.parser.contaIfs) + "\n"
    p[0] += p[5] + "endif" + str(p.parser.contaIfs) + ":\n"


def p_Statement_if_else(p):
    "Statement : IF '(' Cond ')' CondStatements ELSE CondStatements"
    p.parser.contaIfs += 1
    p[0] = p[3] + "\tjz else" + str(p.parser.contaIfs) + "\n"
    p[0] += p[5] + "\tjump endif" + str(p.parser.contaIfs) + "\n"
    p[0] += "else" + str(p.parser.contaIfs) + ":\n" + p[7]
    p[0] += "endif" + str(p.parser.contaIfs) + ":\n"


def p_CondStatements_simple(p):
    "CondStatements : Statement"
    p[0] = p[1]


def p_CondStatements_compound(p):
    "CondStatements : '{' Statements '}'"
    p[0] = p[2]


def p_Cond_or(p):
    "Cond : Cond OR Cond2"
    p[0] = p[1] + p[3] + "\tadd\n"


def p_Cond(p):
    "Cond : Cond2"
    p[0] = p[1]


def p_Cond2_and(p):
    "Cond2 : Cond2 AND Cond3"
    p[0] = p[1] + p[3] + "\tmul\n"


def p_Cond2(p):
    "Cond2 : Cond3"
    p[0] = p[1]


def p_Cond3_not(p):
    "Cond3 : NOT ExpRel"
    p[0] = p[2] + "\tnot\n"


def p_Cond3(p):
    "Cond3 : ExpRel"
    p[0] = p[1]


def p_Cond3_true(p):
    "Cond3 : TRUE"
    p[0] = "\tpushi 1\n"


def p_Cond3_false(p):
    "Cond3 : FALSE"
    p[0] = "\tpushi 0\n"


def p_ExpRel_exp(p):
    "ExpRel : Exp"
    p[0] = p[1]


def p_ExpRel_gt(p):
    "ExpRel : Exp '>' Exp"
    p[0] = p[1] + p[3] + "\tsup\n"


def p_ExpRel_lt(p):
    "ExpRel : Exp '<' Exp"
    p[0] = p[1] + p[3] + "\tinf\n"


def p_ExpRel_ge(p):
    "ExpRel : Exp GE Exp"
    p[0] = p[1] + p[3] + "\tsupeq\n"


def p_ExpRel_le(p):
    "ExpRel : Exp LE Exp"
    p[0] = p[1] + p[3] + "\tinfeq\n"


def p_ExpRel_eq(p):
    "ExpRel : Exp EQ Exp"
    p[0] = p[1] + p[3] + "\tequal\n"


def p_ExpRel_neq(p):
    "ExpRel : Exp NEQ Exp"
    p[0] = p[1] + p[3] + "\tequal\n\tnot\n"


def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


# Build the parser
parser = yacc.yacc()
parser.ts = {}
parser.contaPos = 0
parser.contaIfs = 0
parser.contaWhiles = 0

# Read line from input and parse it
import sys

parser.success = True
program = sys.stdin.read()
codigo = parser.parse(program)
if parser.success:
    print(parser.ts)
    print(codigo)
else:
    print("Programa com erros... Corrija e tente novamente!")
