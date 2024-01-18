""" q12_4.py """


def func_a(arr, i):
    """ function a """
    if i < len(arr):
        print(arr[i], end=" ")
        func_a(arr, i + 1)


def func_b(arr, i):
    """ function b """
    if i < len(arr):
        func_b(arr, i + 1)
        print(arr[i], end=" ")


num_list = [1, 5, 7, 9, 4, 5, 2]

print("func_a: ")
func_a(num_list, 0)

print("\n--------")

print("func_b: ")
func_b(num_list, 0)
