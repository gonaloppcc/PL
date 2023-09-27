import re


def valid_ipv4(ip: str):
    valid = True
    for n in m.groups():
        n = int(n)
        if not 0 <= n <= 255:
            return False

    return valid


f = open('input2.txt', 'r', encoding='utf-8')

# Regular expressions with verification
ipv4 = re.compile(
    r"^((2[0-4]\d|25[0-5]|1\d\d|0?\d\d|0?0?\d)\.){3}(2[0-4]\d|25[0-5]|[0-1]\d\d|0?\d\d|0?0?\d)$"
)

ipv6 = re.compile(
    r"([\da-f]{1,4}:){7}([\da-f]{0,4})"
)

# Simple regular expressions with verification in the code
ipv4S = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$')
ipv4S2 = re.compile(r'^(?:(\d{1,3})\.){3}(\d{1,3})$')

print('----')
for line in f:
    if m := ipv4S.search(line):
        # print('IPv4')
        if valid_ipv4(m[0]):
            print('Valid IPv4')
        else:
            print('Invalid IPv4')
    elif ipv6.search(line):
        print('IPv6')
    else:
        print('Inválido')
    print('----')
