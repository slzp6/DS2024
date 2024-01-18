""" q12_3.py """


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


N = 300
print("Fibonacci (memoization):")
arr = [None] * (N + 1)
fib = fibonacci_m(N, arr)
print(f"n={N} : {fib}")
