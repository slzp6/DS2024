""" q7_4.py """


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

    def inorder(self, node):
        """ inorder traversal """
        if node is None:
            return
        self.inorder(node.left)
        print(node.key, end=" ")
        self.inorder(node.right)

    def display(self, node, levels=0):
        """ display """
        if node is None:
            return
        self.display(node.right, levels + 1)
        print('-' * 4 * levels + str(node.key))
        self.display(node.left, levels + 1)

    def find_height(self, node):
        """ find a bst height """
        h_left = 0
        h_right = 0
        if node is None:
            return 0
        if node.left is not None:
            h_left = self.find_height(node.left)
        if node.right is not None:
            h_right = self.find_height(node.right)
        if h_left > h_right:
            return h_left + 1
        return h_right + 1


root = Node(40)

root.left = Node(30)
root.right = Node(70)

root.left.left = Node(10)
root.left.right = None
root.right.left = Node(60)
root.right.right = Node(90)

root.left.left.left = None
root.left.left.right = Node(20)
root.right.left.left = None
root.right.left.right = None
root.right.right.left = None
root.right.right.right = None

bst = BST()

print("BST:")
bst.display(root)

print("\nThe height of a BST: ", bst.find_height(root))
