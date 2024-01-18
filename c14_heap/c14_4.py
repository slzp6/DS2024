""" c14_4.py """


def heapify(arr, len_arr, i):
    """ heapify """
    max_idx = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len_arr and \
        arr[max_idx] < arr[left]:
        max_idx = left

    if right < len_arr and \
        arr[max_idx] < arr[right]:
        max_idx = right

    if max_idx != i:
        arr[i], arr[max_idx] = \
            arr[max_idx], arr[i]
        heapify(arr, len_arr, max_idx)


def heap_sort(arr):
    """ heap sort """
    len_arr = len(arr)

    for i in range(len_arr // 2 - 1, -1, -1):
        heapify(arr, len_arr, i)

    for i in range(len_arr - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


a = [10, 20, 50, 80, 40, 30, 70, 60, 90]
print("unsorted list: ")
print(a)
heap_sort(a)
print("")
print("sorted list (heap sort): ")
print(a)
