""" c10_1b.py """


def hash_function(key, modulus):
    """ hash function """
    return key % modulus


M = 7
keys = [383, 886, 777, 915]
for KEY in keys:
    HV = hash_function(KEY, M)
    print(f"{KEY} mod {M} = {HV}")
