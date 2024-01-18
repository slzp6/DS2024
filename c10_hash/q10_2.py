""" q10_2.py """

import random


def hash_function(key, modulus):
    """ hash function """
    return key % modulus


def mid_square(key, digit):
    """ middle square method """
    x_square = key * key
    x_square = x_square // 10**digit
    x_mid = x_square % (10**(2 * digit))
    return x_mid


M = 5
random.seed(1)
keys = random.sample(range(0, 10000), M)

Z = len(str(keys[0]))
ZH = len(str(keys[0])) // 2
ZD = len(str(keys[0])) * 2

print("--- division method:")
print("M=", M)
for hkey in keys:
    h = hash_function(hkey, M)
    print(f"{str(hkey).zfill(Z)}", end=" = ")
    print(f"{str(h).zfill(Z)}")
print("")

print("--- mid_square method:")
print("key[0] len.:", Z)
print("half:", ZH)
print("double:", ZD)
print("")

for KEY in keys:
    h = mid_square(KEY, ZH)
    print(f"{str(KEY).zfill(Z)}", end=" ")
    print(f"{str(KEY*KEY).zfill(ZD)}", end=" = ")
    print(f"{str(h).zfill(Z)}")
