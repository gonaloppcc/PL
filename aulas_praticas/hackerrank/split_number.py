import re
import sys

# Input format
# Number of lines
# Phone number
# [Country code]-[Local Area Code]-[Number]  
# (\d{1,3})(\d{1,3})(\d{4,10})

expr = '(\d{1,3})(?:\-|\s)(\d{1,3})(?:\-|\s)(\d{4,10})'

# Output format
# CountryCode=[Country Code],LocalAreaCode=[Local Area Code],Number=[Number]

next(sys.stdin)

for line in sys.stdin:
    m = re.search(expr, line)
    if m:
        c, l, n = m.groups()
        print(f'CountryCode={c},LocalAreaCode={l},Number={n}')