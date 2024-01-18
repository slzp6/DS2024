""" q13_7.py """


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


def quicksort_it(arr, left, right):
    """ Quicksort iteratiarre (stack) """
    stack_size = right - left + 1
    stack = [0] * stack_size

    top = -1
    top += 1
    stack[top] = left
    top += 1
    stack[top] = right

    while top >= 0:
        right = stack[top]
        top -= 1
        left = stack[top]
        top -= 1

        pivot = partition(arr, left, right)

        if pivot - 1 > left:
            top += 1
            stack[top] = left
            top += 1
            stack[top] = pivot - 1

        if pivot + 1 < right:
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = right


a = [80, 40, 30, 20, 10, 00, 70, 90, 50, 60]
print("unsorted list:              ")
print(a)
print()
quicksort_it(a, 0, len(a) - 1)
print("sorted list (Quicksort_iterative): ")
print(a)
