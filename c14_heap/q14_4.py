""" q14_4.py """

import heapq
import random


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

    def heap_list(self):
        """ heap list """
        heap_neg = [x * (-1) for x in self.heap]
        return heap_neg

    def heap_display(self):
        """ heap display """
        heap_neg = [x * (-1) for x in self.heap]
        print(heap_neg)

    def heap_delete(self):
        """ heap delete """
        self.heap = []

    def is_max_heap(self, arr):
        """ is max heap """
        len_arr = len(arr)
        index = int((len_arr - 2) / 2) + 1
        # print('Left Right i len_arr')
        for i in range(0, index):
            left = 2 * i + 1
            right = 2 * i + 2
            # print(left, right, i, len_arr)
            if arr[left] > arr[i]:
                return False
            if right < len_arr and arr[right] > arr[i]:
                return False
        return True


L = 3
max_heap = MaxHeap()
random.seed(1)

for _ in range(L):
    N = random.sample(range(5, 10), 1)[0]
    rand_arr = random.sample(range(0, N), N)
    for j in rand_arr:
        max_heap.heap_push(j)

    heap = max_heap.heap_list()

    print(rand_arr, end=" ")
    print(max_heap.is_max_heap(rand_arr))

    print(max_heap.heap_list(), end=" ")
    print(max_heap.is_max_heap(heap))

    print(" ")
    max_heap.heap_delete()
