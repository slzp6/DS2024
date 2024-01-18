""" q11_2b.py """

import random
import string


def rand_str(str_length):
    """ random string """
    rch = [random.choice(string.ascii_uppercase) \
           for _ in range(str_length)]
    return ''.join(rch)


def hash_function_str(str_item, modulus):
    """ hash function """
    sums = 0
    ls_ac = []
    len_item = len(str_item)
    for pos in range(len_item):
        ascii_code = ord(str_item[pos])
        ls_ac.append(ascii_code)
        sums = sums + ascii_code

    return ls_ac, sums, sums % modulus


random.seed(1)

M = 5
keys = []
for _ in range(3):
    keys.append(rand_str(7))

print(keys)

for key in keys:
    list_ac, s, h = hash_function_str(key, M)
    print(key)
    print(list_ac)
    print(f"{s} mod {M} = {h}\n")
