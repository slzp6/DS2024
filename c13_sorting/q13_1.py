""" q13_1.py """


def bubble_sort(arr):
    """ bubble sort """
    len_arr = len(arr)

    for i in range(0, len_arr - 1):
        swapped = False
        for j in range(0, len_arr - i - 1):
            print(i, j, arr)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped is False:
            print('# swapped -> false')
            break


a = [300, 100, 200, 500, 400]
print("unsorted list:", a)

bubble_sort(a)
print("sorted list:  ", a)
