import re

expr = re.compile(r'(\d{2})(-|\.\.\.|:)(\d{2})\2(\d{2})\2(\d{2})')

with open('input4.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    matriculas = re.finditer(expr, content)
    print([matricula for matricula in matriculas])
