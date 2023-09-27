import re
import sys

password_expr = '^[_\.]\d+[A-Za-z]*_?$'

next(sys.stdin)

for line in sys.stdin:
    username = re.search(password_expr, line)
    print('VALID' if username else 'INVALID')
