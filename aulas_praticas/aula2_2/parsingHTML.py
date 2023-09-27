# Objectivo: Obter todos os links de uma pagina html
# Caracterização de uma pagina html:
# <head> </head>
# <body> </body>

# Assumimos que o html é bem formado

# Tag dos links:
# <a href="http:www.di.uminho.pt"> texto </a>

# Queremos apanhar o href de uma tag

# Ordem dos subgrupos: (()())()
#                      12 3  4

import re
import sys

expr = r'(?i)href\s*=\s*"([^"]+)"'

for line in sys.stdin:
    enderecos = re.finditer(expr, line)
    for endereco in enderecos:
        print(endereco.group(1))
