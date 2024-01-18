""" c11_3.py """


def hash_function_a(str_item, bucket_size):
    """ hash function a """
    sums = 0
    len_item = len(str_item)
    for pos in range(len_item):
        sums = sums + ord(str_item[pos])
    return sums % bucket_size


def hash_function_b(str_item, bucket_size):
    """ hash function b """
    return sum(ord(ch) for ch in str_item) \
        % bucket_size


S1 = "Apple"
print(S1, hash_function_a(S1, 10))
print(S1, hash_function_b(S1, 10))

S2 = "Banana"
print(S2, hash_function_a(S2, 10))
print(S2, hash_function_b(S2, 10))
