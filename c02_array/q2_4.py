""" q2_4.py """

import random
import time


def linear_search_r(arr, low, high, key):
    """ linear search """
    if high < low:
        return None
    if arr[low] == key:
        return low
    if arr[high] == key:
        return high
    return linear_search_r(arr, low + 1, high - 1, key)


def binary_search_r(arr, low, high, key):
    """ binary search """
    if low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            return binary_search_r(arr, low, mid - 1, key)
        # if arr[mid] < key:
        return binary_search_r(arr, mid + 1, high, key)
    return None


N = 1_000
M = N // 2
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
print("linear search (recursive)")
t_start = time.time()
for i in rnbs_k:
    R = linear_search_r(rnbs_a, 0, len(rnbs_a) - 1, i)
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
print("binary search (recursive)")
t_start = time.time()
for i in rnbs_k:
    R = binary_search_r(rnbs_b, 0, len(rnbs_b) - 1, i)
    if R is None:
        NF += 1
    else:
        F += 1
t_end = time.time()
t_elapsed = t_end - t_start
print(f"found:{F} , not_found:{NF}")
print(f"elapsed time: {t_elapsed:.3f} sec.")
