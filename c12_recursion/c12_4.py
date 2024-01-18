""" c12_4.py """

import time


def fibonacci(i):
    """ Fibonacci """
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fibonacci(i-1) + \
            fibonacci(i-2)


def fibonacci_m(i, memo):
    """ Fibonacci (memoization) """
    if memo[i] is None:
        if i == 0:
            memo[i] = 0
            return 0
        if i == 1:
            memo[i] = 1
            return 1
        memo[i] = fibonacci_m(i-1, memo) + \
            fibonacci_m(i-2, memo)
    return memo[i]


N = 39

print("Fibonacci:")
ta_start = time.time()
for j in range(N):
    fib = fibonacci(j)
    print(f"{fib}", end=" ")
ta_end = time.time()

print("\n")
print("Fibonacci (memoization):")
tb_start = time.time()

for j in range(N):
    arr = [None] * (j + 1)
    fib = fibonacci_m(j, arr)
    print(f"{fib}", end=" ")
tb_end = time.time()

print("\n")
print("Fibonacci        :", ta_end - ta_start)
print("Fibonacci (memo.):", tb_end - tb_start)

# AMD Ryzen 9 5950X
# Fibonacci        : 17.58215570449829
# Fibonacci (memo.): 0.000499725341796875
