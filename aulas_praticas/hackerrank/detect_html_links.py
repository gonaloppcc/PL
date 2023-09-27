import re
import sys

expr = r'(?i)href=\"([^\"<]*)\"[^>]*>(?:<[^>]*>)*([^<>]*)(?:</[^>]*>)*</a>'

for m in re.finditer(expr, sys.stdin.read()):
    (link, title) = m.groups()
    print(link, title.strip(), sep=',')