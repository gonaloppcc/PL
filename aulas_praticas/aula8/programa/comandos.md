Exemplos:
print 12
read a
b = 2*a+b
print b+1
dump
end

Calc -> Comando Comandos end

COmandos -> empty {end}
        | Comando Comandos {print, read, id, dump}

comando -> Print Exp
        |read id
        | id '=' Exp
        | dump

Vais ter de alterar os look ahead de Exp2 e termo2, porque já não é ., mas sim o novo Follow de Exp