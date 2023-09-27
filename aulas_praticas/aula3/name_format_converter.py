# Guilherme Fernandes
# Para
# Fernandes, G.

import sys
import re

for line in sys.stdin:
    line = re.sub(r'([^\W\d])\S*\s+([^\W\d]+)', r'\2, \1.', line)
    print(line, end='')