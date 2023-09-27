# Objetivo: Fazer uma calculadora
# Fazer um tokenizer

# >> 5 + 3 * 21

# -> int = 5
# -> op = +
# -> int = 5
# -> op = *
# -> int = 21

# (ab) | (cd) | (ef)
# m = re.search(expr, linha)
# m.groups()

import re
import sys

expr = r'(\d+)|([-+*/])'
comExp = re.compile(expr)

for line in sys.stdin:
    tokens = comExp.finditer(line)
    for t in tokens:
        if t.group(1):
            print("int:", t.group(1))
        else:
            print("op:", t.group(2))
