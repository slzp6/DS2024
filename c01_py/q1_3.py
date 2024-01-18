""" q1_3.py """

import random

random.seed(1)
list_a = [1, 2, 3, 4, 5, 6, 7]
print(list_a)

nums = random.sample(list_a, 5)
print(nums)

nums = random.choices(list_a, k=5)
print(nums)
