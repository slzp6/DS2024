""" c12_5.py """


def gcd(i, j):
    """ Greatest Common Divisor """
    print(f"  {i:3},{j:3} ")
    if j == 0:
        return i
    v_gcd = gcd(j, i % j)
    print(f"  return {v_gcd} ")
    return v_gcd


A = 36
B = 84
print(f"a = {A:2} b = {B:2}")
gcd = gcd(A, B)
print(f"GCD({A},{B}) = {gcd}")
