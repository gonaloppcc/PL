import re

expr = re.compile(
    r'\((?P<X>(?:\+|\-)?\d+(?:.\d+)), (?P<Y>(?:\+|\-)?\d+(?:.\d+))\)')

with open('input3.txt', 'r', encoding='utf-8') as f:
    print('-------------')
    for line in f:
        if m := expr.search(line):
            print(m.groupdict())
        else:
            print('Invalid')

    print('-------------')

# Podemos dar replace com o $ para substituir por um n grupo
