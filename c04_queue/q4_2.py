""" q4_2.py """

import collections

q = collections.deque()
print(q)

items = [10, 20, 30, 40, 50]
for i in items:
    print(" append: ", i)
    q.append(i)

print(q)

print(" popleft:", q.popleft())
print(q)

print(" appendleft: 60")
q.appendleft(60)
print(q)

print(" extendleft: [70]")
q.extendleft([70])
print(q)

print(" append: 80")
q.append(80)
print(q)

print(" extend: [90,100,110]")
q.extend([90, 100, 110], )
print(q)

print(" pop:", q.popleft())
print(q)

print(" rotate(3) ")
q.rotate(3)
print(q)

print(" remove: 30")
q.remove(30)
print(q)

print(" clear() ")
q.clear()
print(q)
