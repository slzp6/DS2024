""" c12_6.py """


def func_a(i):
    """ function a """
    if i > 5:
        return
    print(i, end=' ')
    func_a(i + 1)


func_a(0)
