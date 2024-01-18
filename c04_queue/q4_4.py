""" q4_4.py """

import queue
import random
import string


def rand_str(num):
    """ random string """
    rch = [random.choice(string.ascii_uppercase) \
           for _ in range(num)]
    return ''.join(rch)


N = 1000000

random.seed(1)
data_w_pri = [(random.randint(0, N), rand_str(10)) \
              for _ in range(N)]

q = queue.PriorityQueue()

print("n=", N)
print("[:5] -> ", data_w_pri[:5])

for i in data_w_pri:
    q.put(i)

print("priority queue (qsize):", q.qsize())

print("---")
for i in range(10):
    print("  get [priority, data] ->", q.get())

print("priority queue (qsize):", q.qsize())
