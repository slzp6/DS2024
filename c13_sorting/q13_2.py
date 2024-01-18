""" q13_2.py """

import random
import time

N = 1_000_000
random.seed(1)
a = random.sample(range(0, N), N)

t_start = time.time()
a.sort()
t_end = time.time()

print(f"n={N}")
t_elapsed = t_end - t_start
print(f"elapsed time: {t_elapsed:.3f} sec.")
