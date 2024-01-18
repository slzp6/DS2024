""" c13_8.py """


def merge_sort(arr):
    """ merge sort"""
    if 1 < len(arr):

        mid = len(arr) // 2

        arr_left = arr[:mid]
        arr_right = arr[mid:]

        merge_sort(arr_left)
        merge_sort(arr_right)

        i = j = k = 0
        while i < len(arr_left) and \
            j < len(arr_right):
            if arr_left[i] < arr_right[j]:
                arr[k] = arr_left[i]
                i += 1
            else:
                arr[k] = arr_right[j]
                j += 1
            k += 1

        while i < len(arr_left):
            arr[k] = arr_left[i]
            i += 1
            k += 1

        while j < len(arr_right):
            arr[k] = arr_right[j]
            j += 1
            k += 1


a = [300, 100, 200, 500, 400]
print("unsorted list:            ", a)

merge_sort(a)
print("sroted list (merge_sort): ", a)
