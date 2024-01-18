""" c8_2.py """


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


nodes = [40, 30, 70, 10, 60, 90, 20]
bst = BST()

for i in nodes:
    bst.insert(i)

print("BST:")
bst.display_nodes()

print("\n***")
N1 = 15
print("insert:", N1)
bst.insert(N1)

print("\nBST:")
bst.display_nodes()
