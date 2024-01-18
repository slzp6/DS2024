""" c2_9.py """

import random


def binary_search(arr, key):
    """ binary search """
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        # print(low, mid, high)
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return None


random.seed(1)
N = 7
B = 50
M = 2
rnbs = random.sample(range(B, B + N), N)
print("org:", rnbs)

rnbs.sort()
print("asc:", rnbs)

for i in range(B - M, B + N + M):
    R = binary_search(rnbs, i)
    print(f"binary_search:{i} -> index:{R}")
