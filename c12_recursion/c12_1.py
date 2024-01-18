""" c12_1.py """


def factorial(i):
    """ factorial """
    if i == 0:
        return 1
    return i * factorial(i - 1)


print("factorial:")
for n in range(6):
    fact = factorial(n)
    print(f"n={n:02} : {fact}")
