""" c5_1.py """


class Node:
    """ node """
    def __init__(self, key):
        self.key = key
        self.ref_next = None


node1 = Node(30)
print(node1.key)
print(node1.ref_next)
