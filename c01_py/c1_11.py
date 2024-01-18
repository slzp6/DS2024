""" c1_11.py """

set_a = {10, 20, 30, 40}
set_b = {20, 30, 40, 50}

s_union = set_a | set_b
print(s_union)

s_intersection = set_a & set_b
print(s_intersection)

s_difference_ab = set_a - set_b
print(s_difference_ab)

s_difference_ba = set_b - set_a
print(s_difference_ba)
