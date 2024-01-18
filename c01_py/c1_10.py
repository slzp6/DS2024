""" c1_10.py """

set_a = {10, 20, 30, 10, 20, 40}
print(set_a)

set_b = {3.14, "apple", 3.14, "banana"}
print(set_b)

set_a.add(50)
print(set_a)

set_a.remove(10)
print(set_a)

fset_a = frozenset(set_a)
print(fset_a)
