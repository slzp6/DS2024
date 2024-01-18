""" q7_3.py """


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

    def find_tree_size(self, node):
        """ bst size """
        s_left = 0
        s_right = 0
        if node is None:
            return 0
        if node.left is not None:
            s_left = self.find_tree_size(node.left)
        if node.right is not None:
            s_right = self.find_tree_size(node.right)

        return s_left + s_right + 1


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

print("\nThe number of nodes in a BST: ", bst.find_tree_size(root))
