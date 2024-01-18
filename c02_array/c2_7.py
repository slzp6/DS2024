""" c2_7.py """

import array

array_a = array.array('i', [10, 20, 30, 40])

print(array_a)
print("\nappend(50)")
array_a.append(50)
print(array_a)

print("\ninsert(2, 20):")
array_a.insert(2, 20)
print(array_a)

print("\nremove(30):")
array_a.remove(30)
print(array_a)

print("\nreverse:")
array_a.reverse()
print(array_a)

print("\ncount(20):")
C = array_a.count(20)
print(C)

print("\nsorted:")
array_b = sorted(array_a)
print(array_b)

print("\nlen:")
L = len(array_a)
print(L)
