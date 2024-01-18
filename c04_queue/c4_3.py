""" c4_3.py """

import queue

q = queue.Queue()
print(list(q.queue))

print(" enqueue: 10")
q.put(10)
print(" enqueue: 30")
q.put(30)
print(" enqueue: 20")
q.put(20)
print(list(q.queue))

print(" enqueue: 50")
q.put(50)
print(" enqueue: 40")
q.put(40)
print(list(q.queue))

print(" dequeue:", q.get())
print(" dequeue:", q.get())
print(list(q.queue))
