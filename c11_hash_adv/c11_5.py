""" c11_5.py """


def hash_function_a(str_item, bucket_size):
    """ hash function a """
    sums = 0
    len_item = len(str_item)
    for pos in range(len_item):
        sums = sums + ord(str_item[pos])
    return sums % bucket_size


def hash_function_c(str_item, bucket_size):
    """ hash function c """
    sums = 0
    len_item = len(str_item)
    for pos in range(len_item):
        sums = sums + \
            ord(str_item[pos]) * (pos + 1)
    return sums % bucket_size


S1 = "PineApple"
S2 = "ApplePine"
S3 = "elppAeniP"  # S3 = S1[::-1]

print(S1, hash_function_c(S1, 10))
print(S2, hash_function_c(S2, 10))
print(S3, hash_function_c(S3, 10))
