""" q11_8.py """

import hashlib
from PIL import Image

hash_a = \
hashlib.md5(Image.open('./cat_a.png').tobytes())
print("cat_a: ", hash_a.hexdigest())

hash_b = \
hashlib.md5(Image.open('./cat_b.png').tobytes())
print("cat_b: ", hash_b.hexdigest())
