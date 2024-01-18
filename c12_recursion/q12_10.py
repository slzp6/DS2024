""" q12_10.py """

import time


def fibonacci_it(i):
    """ Fibonacci iterative """
    j, k = 0, 1
    while i > 0:
        j, k = k, j + k
        i -= 1
    return j


def fibonacci_t(i, cur=0, nxt=1):
    """ Fibonacci tail call"""
    if i == 0:
        return cur
    return fibonacci_t(i - 1, nxt, cur + nxt)


N = 300

print("Fibonacci iterative:")
ta_start = time.time()
F = fibonacci_it(N)
ta_end = time.time()

print(f"n: {N}")
print(f"Fib.: {F}")
print(f"time: {ta_end - ta_start}(sec)")

print("\n---")
print("Fibonacci tail call:")
ta_start = time.time()
F = fibonacci_t(N)
ta_end = time.time()

print(f"n: {N}")
print(f"Fib.: {F}")
print(f"time: {ta_end - ta_start}(sec)")
