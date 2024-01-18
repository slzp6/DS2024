""" c12_2.py """


def fibonacci(i):
    """ Fibonacci """
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fibonacci(i-1) + \
        fibonacci(i-2)


print("Fibonacci:")
for j in range(11):
    fib = fibonacci(j)
    print(f"n={j:02} : {fib}")
