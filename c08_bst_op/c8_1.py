""" c8_1.py """


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
        """ display (helper) """
        if node is None:
            return
        self.display(node.right, levels + 1)
        print('-' * 4 * levels + str(node.key))
        self.display(node.left, levels + 1)

    def display_nodes(self):
        """ display """
        self.display(self.root, 0)

    def search(self, key):
        """ search for a node in a bst"""
        curr = self.root
        while True:
            if curr is None:
                return None
            if curr.key is key:
                return key
            if curr.key > key:
                curr = curr.left
            else:
                curr = curr.right


nodes = [40, 30, 70, 10, 60, 90, 20, 80]
bst = BST()

for i in nodes:
    bst.insert(i)

print("BST:")
bst.display_nodes()

print("\n***")
N1 = 80
print("search", N1, "->", bst.search(N1))

N2 = 85
print("search", N2, "->", bst.search(N2))
