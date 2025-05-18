import sys

inp = sys.argv[1]
n_str = ""

print(inp)

for c in inp:
    if 65 <= ord(c) <= 90: # test for capital letters
        c = chr(ord(c) + 13)
        if ord(c) > 90:
            c = chr(ord(c) - 26)
    elif 97 <= ord(c) <= 122: # test for small letters
        c = chr(ord(c) + 13)
        if ord(c) > 122:
            c = chr(ord(c) - 26)
    else: # not an alphabet
        n_str = n_str + c
        continue
    n_str = n_str + c

print(n_str)