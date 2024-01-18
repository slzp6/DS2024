""" q13_4.py """

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


N = 10_000
random.seed(1)
a = random.sample(range(0, N), N)
print(f"n={N}")
bubble_sort(a)
