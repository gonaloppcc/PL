import sys
import re

import ply.lex as lex

tokens = [
    'section',
    'subsection',
    'textbf',
    'textitf',
    'underline',
    'enumerate',  # 'begin{enumerate}'
    'endEnumerate',  # End enumerate
    'itemize',  # 'begin{itemize}'
    'endItemize',  # End itemize
    'item'

    'end',  # End of tag
    'text'  # Text of tag
]


def t_item(t):
    r'\\item\s.*'
    print(f'<li>{t.value[6:]}</li>', end='')


def t_endItemize(t):
    r'\\end{itemize}'
    print("<ul>", end='')
    t.lexer.tags.pop()  # Assuming that this token is use correctely


def t_itemize(t):
    r'\\begin{itemize}'
    print("<ul>", end='')
    t.lexer.tags.append("ul")


def t_endEnumerate(t):
    r'\\end{enumerate}'
    print("<ol>", end='')
    t.lexer.tags.pop()  # Assuming that this token is use correctely


def t_enumerate(t):
    r'\\begin{enumerate}'
    print("<ol>", end='')
    t.lexer.tags.append("ol")


def t_underline(t):
    r'\\underline{'
    print("<u>", end='')
    t.lexer.tags.append("u")


def t_textit(t):
    r'\\textit{'
    print("<i>", end='')
    t.lexer.tags.append("i")


def t_textbf(t):
    r'\\textbf{'
    print("<b>", end='')
    t.lexer.tags.append("b")


def t_subsection(t):
    r'\\subsection{'
    print("<h2>", end='')
    t.lexer.tags.append("h2")


def t_section(t):
    r'\\section{'
    print("<h1>", end='')
    t.lexer.tags.append("h1")


def t_end(t):
    r'}'
    print(f"</{t.lexer.tags.pop()}>", end='')


def t_text(t):
    r'.|\n'
    print(t.value, end='')


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Analisador léxico
lexer = lex.lex()

# Variaveis de estado
lexer.tags = []  # Stack with tags

for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        print(tok)

if len(lexer.tags) != 0:
    print('\nInvalid latex file!')
