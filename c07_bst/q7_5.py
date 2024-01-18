""" q7_5.py """


class Node:
    """ node """
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key

    def display(self, node, levels=0):
        """ display """
        if node is None:
            return
        self.display(node.right, levels + 1)
        print('-' * 4 * levels + str(node.key))
        self.display(node.left, levels + 1)


bt = Node('A', Node('B', Node('D'), None), Node('C', None, Node('E')))
bt.display(bt)
