""" c1_9.py """

dict_a = {'k1': 100, 'k2': 200, 'k3': 300}
print(dict_a)

item = dict_a.get('k1')
print(item)
print(dict_a)

item = dict_a.pop('k1')
print(item)
print(dict_a)

dict_a.setdefault('k4', 400)
print(dict_a)
