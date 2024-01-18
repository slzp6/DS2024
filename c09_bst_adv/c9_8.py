""" c9_8.py """

import random


class Node:
    """ node """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.count = 1


class BST:
    """ bst """
    def __init__(self):
        self.root = None

    def insert(self, key):
        """ insert a key into a bst  """
        node = Node(key)
        if self.root is None:
            self.root = node
        else:
            curr = self.root
            parent = None
            while True:
                parent = curr
                if node.key == curr.key:
                    print("dup. key:", node.key)
                    curr.count += 1
                    return
                if node.key < parent.key:
                    curr = curr.left
                    if curr is None:
                        parent.left = node
                        return
                else:
                    curr = curr.right
                    if curr is None:
                        parent.right = node
                        return

    def display(self, node, levels=0):
        """ display (helper function) """
        if node is None:
            return
        self.display(node.right, levels + 1)
        print('-' * 4 * levels + str(node.key))
        self.display(node.left, levels + 1)

    def display_nodes(self):
        """ display """
        self.display(self.root, 0)

    def display_dup(self, node, levels=0):
        """ display dup. nodes (helper) """
        if node is None:
            return
        self.display_dup(node.right, levels + 1)
        print('-' * 4 * levels, end="")
        print(str(node.key), end="")
        print('[' + str(node.count) + ']')
        self.display_dup(node.left, levels + 1)

    def display_dup_nodes(self):
        """ display dup. nodes """
        self.display_dup(self.root, 0)


N = 10
random.seed(1)
rnbs = random.sample(range(N), N)

M = N // 2
random.seed(2)
rnbs_h = random.sample(range(N), M)

print("rnbs:   ", rnbs)
print("rnbs_h: ", rnbs_h)

bst = BST()

for i in rnbs:
    bst.insert(i)

for j in rnbs_h:
    bst.insert(j)

print("\n*** BST:")
bst.display_dup_nodes()
