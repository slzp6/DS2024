""" c2_8.py """

import random


def linear_search(arr, key):
    """ linear search """
    arr_length = len(arr)
    for index in range(arr_length):
        if arr[index] == key:
            return index
    return None


random.seed(1)
N = 7
B = 50
M = 2
rnbs = random.sample(range(B, B + N), N)
print("org:", rnbs)

for i in range(B - M, B + N + M):
    R = linear_search(rnbs, i)
    print(f"linear_search:{i} -> index:{R}")
