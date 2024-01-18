""" c14_3.py """

import heapq


def heap_sort(arr):
    """ heap sort """
    len_arr = len(arr)
    heap = []

    for i in range(0, len_arr):
        heapq.heappush(heap, arr[i])

    for i in range(0, len_arr):
        arr[i] = heapq.heappop(heap)


a = [10, 20, 50, 80, 40, 30, 70, 60, 90]
print("unsorted list:")
print(a)
print("")
heap_sort(a)
print("sorted list (heap sort):")
print(a)
