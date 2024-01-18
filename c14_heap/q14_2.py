""" q14_2.py """

import heapq


class MaxHeap:
    """ max heap """
    def __init__(self):
        self.heap = []

    def heap_push(self, val):
        """ heap push """
        heapq.heappush(self.heap, -val)

    def heap_pop(self):
        """ heap pop """
        return -heapq.heappop(self.heap)

    def heap_display(self):
        """ heap display """
        heap_neg = [x * (-1) for x in self.heap]
        print(heap_neg)


a = [10, 20, 50, 80, 40, 30, 70, 60, 90]
print("list: ", a)

max_heap = MaxHeap()

for i in a:
    print("heap_push:", i, end=" ")
    max_heap.heap_push(i)
    max_heap.heap_display()

print('')

for i in range(len(a)):
    print("heap_pop: ", max_heap.heap_pop(), end=" ")
    max_heap.heap_display()
