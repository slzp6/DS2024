""" q11_2.py """

import random
import string


def rand_str(num):
    """ randomn strings """
    rstr = [random.choice(string.ascii_uppercase) \
            for _ in range(num)]
    return ''.join(rstr)


def hash_function_str(str_item, modulus):
    """ hash function """
    sums = 0
    list_ac = []
    len_str = len(str_item)
    for pos in range(len_str):
        acode = ord(str_item[pos])
        list_ac.append(acode)
        sums = sums + acode
    return list_ac, sums, sums % modulus


random.seed(1)
M = 37
KEYS = []
for _ in range(3):
    KEYS.append(rand_str(7))

for ht_key in KEYS:
    ls_ac, sum_ac, h = hash_function_str(ht_key, M)
    print(ht_key)
    print(ls_ac)
    print(f"{sum_ac} mod {M} = {h}\n")
