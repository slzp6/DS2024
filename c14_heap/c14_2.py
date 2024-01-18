""" c14_2.py """

import heapq

h = [(30, "Apple"), \
     (10, "Banana"), \
     (40, "Cranberry"), \
     (20, "Durian")]

print("list:", h)
print("---")
print(".heapify()")
heapq.heapify(h)

print("---")
print("heap:", h)

print("---")
print(".heappop()")
print("n =", len(h))
for _ in range(len(h)):
    print(heapq.heappop(h))
