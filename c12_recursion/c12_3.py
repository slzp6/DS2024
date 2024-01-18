""" c12_3.py """


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


N = 11
print("Fibonacci (memoization):")
for j in range(N):
    arr = [None] * (j + 1)
    fib = fibonacci_m(j, arr)
    print(f"n={j:02} : {fib}")

# Example of slightly more efficient code
#
# print("Fibonacci (memoization):")
# arr = [None] * N
# fib = fibonacci_m(N-1, arr)
# for j in range(N):
#    print(f"n={j:02} : {arr[j]}")
#
