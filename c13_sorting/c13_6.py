""" c13_6.py """


def insertion_sort(arr):
    """ insertion sort """
    len_arr = len(arr)
    for i in range(1, len_arr):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            print(f'i={i} j={j}')
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


a = [300, 100, 200, 500, 400]
print("unsorted list:", a)
a.sort(reverse=True)
print("sorted list (desc.):", a)

insertion_sort(a)
print("sorted list:", a)
