""" q11_1.py """

for code in range(32, 127):
    ch = chr(code)
    print(f"{code:03} {ch:1}", end="  ")

# 32:  white space
# 126: Equivalency sign, tilde
# 127: del
