""" q4_3.py """

import queue
import random

q = queue.Queue()
print(list(q.queue))

N = 1000000
H = N // 2
random.seed(1)
rnbs = random.sample(range(N), N)

print("n=", N)
print("[:5]  -> ", rnbs[:5])
print("[-5:] -> ", rnbs[-5:])

for i in rnbs:
    q.put(i)

print("qsize:", q.qsize())

for i in range(H):
    q.get()

print("qsize:", q.qsize())
