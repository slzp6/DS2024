""" c13_3.py """


def selection_sort(arr):
    """ selection sort """
    len_arr = len(arr)
    for i in range(0, len_arr - 1):
        min_index = i
        for j in range(i + 1, len_arr):
            if arr[j] < arr[min_index]:
                min_index = j
                print(i, j, arr)

        arr[i], arr[min_index] = arr[min_index], arr[i]


a = [300, 100, 200, 500, 400]
print("unsorted list:", a)

selection_sort(a)
print("sorted list:  ", a)
