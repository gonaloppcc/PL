#!/usr/bin/env python3

'''
Z -> Sexp
Sexp -> '(' '+' Lista ')'
     | '(' '*' Lista ')'
     | num

Lista -> Lista Sexp
      | Sexp Sexp

'''
import ply.yacc as yacc
import math
from expS_lex import tokens, literals

def p_Program(p):
    "Program : Declarations Statements"

def p_Declarations_list(p):
    "Declarations : Declarations Declaration"

def p_Declarations_empty(p):
    "Declarations : "

def p_Declaration(p):
    "Declaration : Type IdList"

def p_Type_int(p):
    "Type : INT"

def p_IdList_str(p):
    "IdList : IdList ',' id"

def p_IdList_single(p):
    "IdList : id"

def p_Statements_list(p):
    "Statements : Statements Statement"

def p_Statements_single(p):
    "Statements : Statement"

def p_Statement_atrib(p):
    "Statement : id '=' Exp"

def p_Statement_print(p):
    "Statement : PRINT '(' PrintArgs ')' "

def p_PrintArgs_list(p):
    "PrintArgs : PrintArgs ','  PrintArg"

def p_PrintArgs_single(p):
    "PrintArgs : PrintArg"

def p_Exp_id(p):
    "Exp : id"

def p_PrintArg_str(p):
    "PrintArg : str"
  
def p_PrintArg_Exp(p):
    "PrintArg : Exp"

def p_Factor_int(p):
    "Factor : INT '(' Exp ')'"

def p_Factor_input(p):
    "Factor : INPUT '(' str ')'"

def p_Factor_id(p):
    "Factor : id"
def p_Factor_num(p):
    "Factor : NUM"

def p_error(p):
    print("Erro sintatioco:, ",p)
    parser.success = False


def p_Statement_if(p):
    "Statement : IF '(' Cond ')' CondStatements Else"

def p_Else_empty(p):
    "Else : "

def p_Else_outro(p):
    "Else : ELSE CondStatements"

def p_CondStatements_single(p):
    "CondStatements : Statement"

def p_CondStatements_multiple(p):
    "CondStatements : '{' Statements '}'"

def p_Cond_or(p):
    "Cond : Cond OR Cond2"
def p_Cond_simple(p):
    "Cond : Cond2"

def p_Cond2_and(p):
    "Cond2 : Cond2 AND Cond3"
def p_Cond2_simple(p):
    "Cond2 : Cond3"

def p_Cond3_not(p):
    "Cond3 : NOT ExpRel"

def p_Cond3_normal(p):
    "Cond3 : ExpRel"

# Expressões
def p_ExpRel_maior(p):
    "ExpRel : Exp '>' Exp"

def p_ExpRel_menor(p):
    "ExpRel : Exp '<' Exp"

def p_ExpRel_maiorIgual(p):
    "ExpRel : Exp GE Exp"

def p_ExpRel_menorIgual(p):
    "ExpRel : Exp LE Exp"

def p_ExpRel_Igual(p):
    "ExpRel : Exp EQ Exp"

def p_ExpRel_NotIgual(p):
    "ExpRel : Exp NEQ Exp"

def p_Exp_add(p):
    "Exp : Exp '+' Term"

def p_Exp_sub(p):
    "Exp : Exp '-' Term"

def p_Exp_term(p):
    "Exp : Term"

def p_Term_mult(p):
    "Term : Term '*' Factor "
def p_Term_div(p):
    "Term : Term '/' Factor "
def p_Term_factor(p):
    "Term : Factor "

# Build the parser
parser = yacc.yacc()

parser.registos = {}

# Read line from input and parse it
import sys
parser.sucess = True
program = sys.stdin.read()
parser.parse(program)
if parser.success:
    print("Sucesso")
else:
    print("Erro")