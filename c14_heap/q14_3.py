""" q14_3.py """

import random
import time


def heapify(arr, len_arr, i):
    """ heapify """
    max_idx = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len_arr and \
        arr[max_idx] < arr[left]:
        max_idx = left

    if right < len_arr and \
        arr[max_idx] < arr[right]:
        max_idx = right

    if max_idx != i:
        arr[i], arr[max_idx] = \
            arr[max_idx], arr[i]
        heapify(arr, len_arr, max_idx)


def heap_sort(arr):
    """ heap_sort"""
    len_arr = len(arr)

    for i in range(len_arr // 2 - 1, -1, -1):
        heapify(arr, len_arr, i)

    for i in range(len_arr - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def bubble_sort(arr):
    """ bubble sort """
    len_arr = len(arr)

    for i in range(0, len_arr - 1):
        swapped = False
        for j in range(0, len_arr - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = \
                    arr[j + 1], arr[j]
                swapped = True
        if swapped is False:
            # print('# swapped -> false')
            break


N = 10_000

random.seed(1)
a = random.sample(range(0, N), N)
b = random.sample(range(0, N), N)
print(f"a={N}")
print(f"b={N}")

t_start = time.time()
heap_sort(a)
t_end = time.time()
t_elapsed = t_end - t_start
print(f"heap sort: {t_elapsed:.5f} sec.")

t_start = time.time()
bubble_sort(b)
t_end = time.time()
t_elapsed = t_end - t_start
print(f"bubble sort: {t_elapsed:.5f} sec.")
