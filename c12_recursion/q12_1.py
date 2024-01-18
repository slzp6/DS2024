""" q12_1.py """

import sys


def factorial(i):
    """ factorial """
    if i == 0:
        return 1
    return i * factorial(i - 1)


print("sys. int_max_str_digits:", \
      sys.get_int_max_str_digits())
# sys.set_int_max_str_digits(4300)

N = 100
F = factorial(N)
print(f"\n{N}! = \n{F}")
print(f"\nThe length of an integer: {len(str(F))}")
