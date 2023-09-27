import sys
import re


def match_line(expr: str):
    for line in sys.stdin:
        m = re.search(expr, line)
        if m:
            print('Válido')
        else:
            print('Inválido')


expr = re.compile(r"^[_.]\d+[a-zA-Z]{3,}_?$")


match_line(expr)
