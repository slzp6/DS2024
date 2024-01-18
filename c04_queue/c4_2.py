""" c4_2.py """

import collections

q = collections.deque()
print(q)

print(" enqueue: 10")
q.append(10)
print(" enqueue: 30")
q.append(30)
print(" enqueue: 20")
q.append(20)
print(q)

print(" enqueue: 50")
q.append(50)
print(" enqueue: 40")
q.append(40)
print(q)

print(" dequeue:", q.popleft())
print(" dequeue:", q.popleft())
print(q)
