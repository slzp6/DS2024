""" c13_2.py """


def bubble_sort(arr):
    """ bubble_sort """
    len_arr = len(arr)

    for i in range(0, len_arr - 1):
        for j in range(0, len_arr - i - 1):
            print(i, j, arr)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


a = [300, 100, 200, 500, 400]
print("unsorted list:", a)

bubble_sort(a)
print("sorted list:  ", a)
