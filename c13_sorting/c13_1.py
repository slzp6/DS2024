""" c13_1.py """

a = [300, 100, 200, 500, 400]
print("unsorted list:     ", a)

a.sort()
print("sorted list (asc.): ", a)

a.sort(reverse=True)
print("sorted list (desc.): ", a)
