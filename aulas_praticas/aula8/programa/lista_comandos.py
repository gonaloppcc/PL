# ------------------------------------------------------------
# recdesc.py
#
# Parser recursivo descendente para listas de inteiros:
# []
# [8]
# [4,5,6,7]
# ------------------------------------------------------------
import ply.lex as lex

tokens = ('num', 'id', 'PRINT', 'READ','END','DUMP')
literals = ['+', '-','*','/','(',')','='  ]

def t_PRINT(t):
    r'(?i)print'
    return t

def t_DUMP(t):
    r'(?i)dump'
    return t

def t_READ(t):
    r'(?i)read'
    return t

def t_END(t):
    r'(?i)end'
    return t

def t_id(t):
    r'[A-Za-z_]\w*'
    return t

def t_num(t):
    r'\d+'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Erro léxico no token '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

###########################
prox_simb = ('Erro', '', 0, 0)

# estado da máquina
registos = {}

def parserError(simb):
    print("Erro Sintático: ", simb)

def rec_term(simb):
    global prox_simb
    if prox_simb.type == simb:
        v_term = prox_simb.value
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)
        v_term = 'Erro'
    return v_term


def rec_Termo2(v):
    global prox_simb
    if prox_simb.type == '*':
        rec_term('*')
        v_termo = rec_Termo()
        v_termo2 = v * v_termo
    elif prox_simb.type == '/':
        rec_term('/')
        v_termo = rec_Termo()
        v_termo2 = v / v_termo
    elif prox_simb.type in ['END','PRINT','DUMP','READ','id',')', '-','+']:
        v_termo2 = v
    else:
        parserError(prox_simb)
    return v

def rec_Fator():
    global prox_simb
    if prox_simb.type == 'id':
        rec_term(id)
    elif prox_simb.type == 'num':
        rec_term('num')
    elif prox_simb.type == '(':
        rec_term('(')
        rec_Exp()
        rec_term(')')
    else:
        parserError(prox_simb)

def rec_Termo():
    v_fator = rec_Fator()
    return rec_Termo2(v_fator)

def rec_Exp2():
    global prox_simb
    if prox_simb.type == '+':
        rec_term('+')
        rec_Exp()
    elif prox_simb.type == '-':
        rec_term('-')
        rec_Exp()
    elif prox_simb.type in ['END','PRINT','DUMP','READ','id',')']:
        pass
    else:
        parserError(prox_simb)


def rec_Exp():
    v_Termo = rec_Termo()
    return rec_Exp2(v_Termo)


def rec_Comando():
    global prox_simb
    if prox_simb.type == 'PRINT':
        rec_term('PRINT')
        rec_Exp()
    elif prox_simb.type == 'READ':
        rec_term('READ')
        rec_term('id')
    elif prox_simb.type == 'DUMP':
        rec_term('DUMP')
    elif prox_simb.type == 'id':
        v_id = rec_term('id')
        rec_term('=')
        v_Exp = rec_Exp()
        registos[v_id] = v_Exp
    else:
        parserError(prox_simb)


def rec_Comandos():
    global prox_simb
    if prox_simb.type == 'END':
        pass
    elif prox_simb.type in ['PRINT', 'READ', 'DUMP','id']:
        rec_term('-')
        rec_Exp()
    else:
        parserError(prox_simb)


def rec_Calc():
    rec_Comando()
    rec_Comandos()
    rec_term('END')


def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    rec_Calc()
    print("That's the end...")


# Programa de teste
import sys
programa = sys.stdin.read()
# Teste do tokenizer
# lexer.input(linha)
# for tok in lexer:
#     print(tok)
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)
rec_Parser(programa)
    

