""" q12_6.py """

import time


def fib(i):
    """ fibonacci """
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fib(i - 1) + fib(i - 2)


def fib_tail(i, acc_a=0, acc_b=1):
    """ fibonacci tail recursion """
    if i == 0:
        return acc_a
    if i == 1:
        return acc_b
    return fib_tail(i - 1, acc_b, acc_a + acc_b)


N = 36

t_start = time.time()
print(fib(N))
t_end = time.time()
t_elapsed = t_end - t_start
print(f"{t_elapsed:.20f} sec.")

t_start = time.time()
print(fib_tail(N))
t_end = time.time()
t_elapsed = t_end - t_start
print(f"{t_elapsed:.20f} sec.")
