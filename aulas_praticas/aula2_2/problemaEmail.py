# Email

import re
import sys

# Objectivo: Validar formato de um email

# user@dom.top-dom
# User - caracteres alfanumericos e caracteres especial '-' e '.'
# 1 e ultimo caracteres não podem ser especiais
# Não pode haver dois caracteres especiais consecutivos
# dom - alfanúmericos e hífen
# top-dom - alfanumericos e hifen com 2 ou + caracteres

expr = r'^(\w+[-.]?\w+)+@(\w+\-?\w+\.)+(\w+\-?\w+)+$'

for (n, linha) in enumerate(sys.stdin):
    if re.search(expr, linha):
        print(n, ' :: ', "Válido")
    else:
        print(n, ' :: ', "Inválido")


# for line in sys.stdin:
#    m = re.search(expr, line)
