import re

fileName = 'test1.txt'
file = open(fileName)

fileContent = file.read()

# print(lines)

string1 = 'ssss'

expr = r'^hello'
matches = re.findall(expr, fileContent, re.MULTILINE)

print("Regex flags in python:", [e for e in re.RegexFlag])

print("Matches:", matches)

# Unpacking

# With tuples
tuple1 = (1, 2, 3, 4, 5)

t1, t2, *t3 = tuple1

# With lists
list1 = [x for x in range(10)]

t1, t2, *t3 = list1

# With dictionaries
dict1 = {
    20: "1",
    5: "10",
    31: "100",
    53: "1000",
}

t1, t2, *t3 = dict1

# Prints the test values
print("T1:", t1, "T2:", t2, "T3:", t3)


def primos(n: int):
    return [x for x in range(2, 100) if len(
        [y for y in range(2, x) if x % y == 0]) == 0]


primos100 = primos(100)

filtered = [x+1 for x in primos100]

print("Primos:", primos100)
print("Test:  ", filtered)


print("*:", *primos100, primos100)
