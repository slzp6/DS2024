""" q11_7.py """

fruits = {'apple': 10, 'banana': 20, 'cranberry': 30}
print("dict:", fruits)

print("\nkeys: ", end="")
for key in fruits:
    print(key, end=" ")

print("\n\nvalues: ", end="")
for value in fruits.values():
    print(value, end=" ")

print("\n\nitems: ", end="")
for item in fruits.items():
    print(item, end=" ")

print("\n")
print("dict:", fruits)

print("  insert ('durian': 40)")
fruits['durian'] = 40
print("dict:", fruits)

KEY = 'banana'
item_value = fruits.pop(KEY)
print(f"  pop '{KEY}' -> ", end="")
print(KEY, item_value)

print("dict:", fruits)
