# MD to html converter

import sys
import re

for line in sys.stdin:
    line = re.sub(r'\*\*(.+)\*\*', r'<b>\1</b>', line)
    line = re.sub(r'__(.+)__', r'<i>\1</i>', line)
    print(line, end='')
