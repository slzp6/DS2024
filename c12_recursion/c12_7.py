""" c12_7.py """


def func_b(i):
    """ function b """
    if i > 5:
        return
    func_b(i + 1)
    print(i, end=' ')


func_b(0)
