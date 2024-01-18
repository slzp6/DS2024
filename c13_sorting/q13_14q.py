""" q13_14q.py """

import random
import time


def timer(func):
    """ timer """
    def inner(*args, **kwargs):
        """ inner function """
        t_start = time.perf_counter()
        f_execute = func(*args, **kwargs)
        t_end = time.perf_counter()
        t_execution = t_end - t_start
        print(f"{func.__name__} : {t_execution:.3f} sec.")
        return f_execute

    return inner


@timer
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


@timer
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


N = 20_000
random.seed(1)
a = random.sample(range(0, N), N)
random.seed(1)
b = random.sample(range(0, N), N)

# print("\n ---")
# print(f"n={N}")
# print(a[:3], " ... ", a[-3:])
# bubble_sort(a)
# print(a[:3], " ... ", a[-3:])

print("\n ---")
print(f"n={N}")
print(b[:3], " ... ", b[-3:])
quicksort_it(b, 0, len(b) - 1)
print(b[:3], " ... ", b[-3:])
