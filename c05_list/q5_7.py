""" q5_7.py """

#
# This code is intenstionally disabled by a docstring.
# If you remove the triple quotes you can run this code.
#
A = \
"""

import random

import llist
#  'conda install llist' or
#  'pip install llist'

N = 10
random.seed(1)
rnbs = random.sample(range(N), N)

ll = llist.sllist(rnbs)

print("linked list: ", ll)
print("size: ", ll.size)
print("first node: ", ll.first())
print("last node: ", ll.last())

print([method for method in dir(ll) if callable(getattr(ll, method))])

"""
