""" q2_6.py """

import random
import time


def linear_search(arr, key):
    """ linear search """
    arr_length = len(arr)
    for index in range(arr_length):
        if arr[index] == key:
            return index
    return None


def sentinel_search(arr, key):
    """ sentinel search """
    arr_length = len(arr)
    high = arr_length - 1
    temp = arr[high]
    arr[high] = key
    index = 0
    while arr[index] != key:
        index += 1
    arr[high] = temp
    if index == high and key != temp:
        return None
    return index


def sentinel_search_slow(arr, key):
    """ sentinel search (slow) """
    arr_length = len(arr)
    arr.append(key)
    index = 0
    while arr[index] != key:
        index += 1
    if index == arr_length:
        return None
    return index


N = 5000
random.seed(1)
rnbs_a = random.sample(range(N), N)
rnbs_b = random.sample(range(N), N)
random.seed(2)
rnbs_k = random.sample(range(N * 2), N * 2)

print("rnbs_a (linear search):", len(rnbs_a))
print("rnbs_b (sentinel search):", len(rnbs_b))
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
print(f"elapsed time: {t_elapsed:.5f} sec.")

F = 0
NF = 0
print("---")
print("sentinel search")
t_start = time.time()
for i in rnbs_k:
    R = sentinel_search(rnbs_b, i)
    if R is None:
        NF += 1
    else:
        F += 1
t_end = time.time()
t_elapsed = t_end - t_start
print(f"found:{F} , not_found:{NF}")
print(f"elapsed time: {t_elapsed:.5f} sec.")
