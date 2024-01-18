""" q13_8.py """

import random
import time


def bubble_sort(arr):
    """ bubble sort """
    len_arr = len(arr)

    for i in range(0, len_arr - 1):
        swapped = False
        for j in range(0, len_arr - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped is False:
            break


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


N = 10000
random.seed(1)
a = random.sample(range(0, N), N)
b = random.sample(range(0, N), N)

print(f"a={N}")
print(f"b={N}")

t_start = time.time()
bubble_sort(a)
t_end = time.time()
t_elapsed = t_end - t_start
print(f"bubble_sort: {t_elapsed:.3f} sec.")

t_start = time.time()
quicksort(b, 0, len(b) - 1)
t_end = time.time()
t_elapsed = t_end - t_start
print(f"Quciksort: {t_elapsed:.3f} sec.")
