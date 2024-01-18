""" c14_1.py """

import heapq

h = [10, 20, 50, 80, 40, 30, 70, 60, 90]

print("list: ", h)

print("\n--- min heap")
heapq.heapify(h)
print(".heapify()")
print("heap: ", h)

print("\n---")
i = 25
heapq.heappush(h, i)
print(".heappush(): ", i)
print("heap: ", h)

print("\n---")
j = heapq.heappop(h)
print(".heappop():  ", j)
print("heap: ", h)
