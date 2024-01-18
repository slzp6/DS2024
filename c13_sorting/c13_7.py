""" c13_7.py """


def partition(arr, left, right):
    """ partition """
    piarrot = arr[right]
    ptr = left
    for i in range(left, right):
        if arr[i] <= piarrot:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    arr[ptr], arr[right] = arr[right], arr[ptr]
    return ptr


def quicksort(arr, left, right):
    """ Quicksort """
    if len(arr) == 1:
        return arr
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)
    return arr


a = [300, 100, 200, 500, 400]
print("unsorted list:           ", a)

quicksort(a, 0, len(a) - 1)
print("sorted list (Quicksort): ", a)
