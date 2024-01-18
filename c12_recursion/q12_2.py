""" q12_2.py """


def fibonacci(num):
    """ Fibonacci """
    print(f"fib({num}) = ", end="")
    if num == 0:
        print("0", end="\n")
        return 0
    if num == 1:
        print("1", end="\n")
        return 1
    print(f"fib({num-1}) + fib({num-2})")
    return fibonacci(num-1) + \
            fibonacci(num-2)


i = 5
fib = fibonacci(i)
print(f"\nFibonacci({i}) = {fib}")
