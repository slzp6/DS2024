""" q12_9.py """

import time


def fibonacci(i):
    """ Fibonacci """
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fibonacci(i-1) + \
            fibonacci(i-2)


N = 40
print("Fibonacci:\n")
ta_start = time.time()
fib = fibonacci(N)
ta_end = time.time()

print(f"n: {N}")
print(f"Fib.: {fib}")
print(f"time: {ta_end - ta_start}(sec)")
