# Fazer o programa wc em python

# wc indica o número de linhas, palavras e chars

import re
import sys

nLines = 0
nWords = 0
nChars = 0

pal_expr = r'\b\w+\b'

for line in sys.stdin:
    nWords += len(re.findall(pal_expr, line))
    nLines += 1
    nChars += len(line)

print(f'NLines: {nLines}, NWords: {nWords}, nChars: {nChars}')
