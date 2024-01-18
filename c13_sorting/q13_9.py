""" q13_9.py """

import random
import time


def partition(arr, left, right):
    """ partition """
    piarrot = arr[right]
    ptr = left
    for i in range(left, right):
        if arr[i] <= piarrot:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    arr[ptr], arr[right] = arr[right], arr[ptr]
    return ptr


def quicksort(arr, left, right):
    """ Quicksort """
    if len(arr) == 1:
        return arr
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)
    return arr


N = 10_000_000
random.seed(1)
n = random.sample(range(0, N), N)
print("n=", len(n))

t_start = time.time()
quicksort(n, 0, len(n) - 1)
t_end = time.time()
t_elapsed = t_end - t_start
print(f"Quciksort: {t_elapsed:.3f} sec.")
