""" q11_3.py """

import hashlib

print(hashlib.algorithms_available)

ST = b"The_Open_University_of_Japan"

print(ST)
print(hashlib.sha1(ST).hexdigest())
