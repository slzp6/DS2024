""" q14_1.py """

import heapq

a = [10, 20, 50, 80, 40, 30, 70, 60, 90]
print("list: ", a)

h = []
print("---")
for i in a:
    heapq.heappush(h, i)
    print("heap_push:", i, h)

print("---")
for _ in range(len(a)):
    j = heapq.heappop(h)
    print("heap_pop: ", j, h)
