""" q13_6.py """

import random
import time


def insertion_sort(arr):
    """ insertion sort """
    len_arr = len(arr)
    for i in range(1, len_arr):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


N = 10000
random.seed(1)
a = random.sample(range(0, N), N)

print(f"n={N}")

t_start = time.time()
insertion_sort(a)
t_end = time.time()
t_elapsed = t_end - t_start
print(f"insertion_sort 1st: {t_elapsed:.3f} sec.")

t_start = time.time()
insertion_sort(a)
t_end = time.time()
t_elapsed = t_end - t_start
print(f"insertion_sort 2nd: {t_elapsed:.3f} sec.")
