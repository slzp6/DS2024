""" c4_1.py """

q = []
print("queue:", q)

print(" enqueue: 10")
q.append(10)
print(" enqueue: 30")
q.append(30)
print(" enqueue: 20")
q.append(20)
print("queue:", q)

print(" enqueue: 50")
q.append(50)
print(" enqueue: 40")
q.append(40)
print("queue:", q)

print(" dequeue:", q.pop(0))
print(" dequeue:", q.pop(0))
print("queue:", q)
