""" q10_1.py """


def hash_function(key, modulus):
    """ hash function """
    return key % modulus


M = 7
for KEY in range(11):
    HV = hash_function(KEY, M)
    print(f"{KEY} mod {M} = {HV}")
