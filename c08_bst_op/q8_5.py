""" q8_5.py """

import random


class Node:
    """ node """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    """ bst """
    def __init__(self):
        self.root = None

    def insert(self, key):
        """ insert a key into a bst """
        node = Node(key)
        if self.root is None:
            self.root = node
        else:
            curr = self.root
            parent = None
            while True:
                parent = curr
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


N = 6
random.seed(1)
rnbs_a = random.sample(range(N), N)

random.seed(2)
rnbs_b = random.sample(range(N), N)

bst_a = BST()
bst_b = BST()

print("rnbs a: ", rnbs_a)
print("rnbs b: ", rnbs_b)
print("\n***")

for i in rnbs_a:
    bst_a.insert(i)
for i in rnbs_b:
    bst_b.insert(i)

print("BST a:")
bst_a.display_nodes()
print("\n***")
print("BST b:")
bst_b.display_nodes()
