""" q2_3.py """

import random
import time


def linear_search(arr, key):
    """ linear search """
    arr_length = len(arr)
    for index in range(arr_length):
        if arr[index] == key:
            return index
    return None


def binary_search(arr, key):
    """ binary search """
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        # print( low, mid, high)
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1

    return None


N = 5_000
random.seed(1)
rnbs_a = random.sample(range(N), N)
rnbs_b = random.sample(range(N), N)
rnbs_b.sort()

random.seed(2)
rnbs_k = random.sample(range(N * 2), N * 2)
print("rnbs_a (linear search):", len(rnbs_a))
print("rnbs_b (binary search):", len(rnbs_b))
print("rnbs_k (search keys):", len(rnbs_k))

F = 0
NF = 0
print("---")
print("linear search")
t_start = time.time()
for i in rnbs_k:
    R = linear_search(rnbs_a, i)
    if R is None:
        NF += 1
    else:
        F += 1
t_end = time.time()
t_elapsed = t_end - t_start
print(f"found:{F} , not_found:{NF}")
print(f"elapsed time: {t_elapsed:.3f} sec.")

F = 0
NF = 0
print("---")
print("binary search")
t_start = time.time()
for i in rnbs_k:
    R = binary_search(rnbs_b, i)
    if R is None:
        NF += 1
    else:
        F += 1
t_end = time.time()
t_elapsed = t_end - t_start
print(f"found:{F} , not_found:{NF}")
print(f"elapsed time: {t_elapsed:.3f} sec.")
