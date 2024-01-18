""" c10_1c.py """


def hash_function(key, modulus):
    """ hash function """
    return key % modulus


M = 10
keys = [383, 886, 777, 915, 793]
for KEY in keys:
    HV = hash_function(KEY, M)
    print(f"{KEY} mod {M} = {HV}")

print("---")
M = 20
for KEY in keys:
    HV = hash_function(KEY, M)
    print(f"{KEY} mod {M} = {HV}")
