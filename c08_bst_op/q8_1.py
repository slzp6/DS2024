""" q8_1.py """


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

    def preorder(self, node):
        """ preorder (helper) """
        if node is None:
            return
        print(node.key, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        """ inorder  (helper) """
        if node is None:
            return
        self.inorder(node.left)
        print(node.key, end=" ")
        self.inorder(node.right)

    def postorder(self, node):
        """ postorder (helper) """
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.key, end=" ")

    def display(self, node, levels=0):
        """ display a bst (helper function) """
        if node is None:
            return
        self.display(node.right, levels + 1)
        print('-' * 4 * levels + str(node.key))
        self.display(node.left, levels + 1)

    def print_preorder(self):
        """ preorder traversal """
        self.preorder(self.root)

    def print_inorder(self):
        """ inorder traversal """
        self.inorder(self.root)

    def print_postorder(self):
        """ postorder trarversal """
        self.postorder(self.root)

    def display_nodes(self):
        """ display """
        self.display(self.root, 0)


nodes = [25, 34, 38, 40, 50, 59, 63, 57, 37, 98]
bst = BST()

for i in nodes:
    bst.insert(i)

print("BST:")
bst.display_nodes()

print("\npreorder:")
bst.print_preorder()
print("\ninorder:")
bst.print_inorder()
print("\npostorder:")
bst.print_postorder()

print("")
