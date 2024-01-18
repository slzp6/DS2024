""" c2_5.py """

import array

array_a = array.array('i', [10, 20, 30, 40])
print(array_a)
print("\narray_a[2] = 300")
array_a[2] = 300
print(array_a)

print("\ndel array_a[1]")
del array_a[1]
print(array_a)

print("\n10 in array_a")
print(10 in array_a)
print("\n50 in array_a")
print(50 in array_a)
