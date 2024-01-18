""" q13_11.py """

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


def quicksort_it(arr, left, right):
    """ Quicksort iterative (stack) """
    stack_size = right - left + 1
    stack = [0] * stack_size

    top = -1
    top += 1
    stack[top] = left
    top += 1
    stack[top] = right

    while top >= 0:
        right = stack[top]
        top -= 1
        left = stack[top]
        top -= 1

        pivot = partition(arr, left, right)

        if pivot - 1 > left:
            top += 1
            stack[top] = left
            top += 1
            stack[top] = pivot - 1

        if pivot + 1 < right:
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = right


N = 1_000_000
random.seed(1)
a = random.sample(range(0, N), N)
b = random.sample(range(0, N), N)
print("a=", len(a))
print("b=", len(b))

t_start = time.time()
quicksort(a, 0, len(a) - 1)
t_end = time.time()
t_elapsed = t_end - t_start
print(f"Quciksort_recursion: {t_elapsed:.3f} sec.")

t_start = time.time()
quicksort_it(b, 0, len(b) - 1)
t_end = time.time()
t_elapsed = t_end - t_start
print(f"Quciksort_iterative: {t_elapsed:.3f} sec.")
