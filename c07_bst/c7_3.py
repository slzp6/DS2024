""" c7_3.py """


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

    def preorder(self, node):
        """ preorder traversal """
        if node is None:
            return
        print(node.key, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        """ inorder traversal """
        if node is None:
            return
        self.inorder(node.left)
        print(node.key, end=" ")
        self.inorder(node.right)

    def postorder(self, node):
        """ postorder traversal """
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.key, end=" ")

    def display(self, node, levels=0):
        """ display """
        if node is None:
            return
        self.display(node.right, levels + 1)
        print('-' * 4 * levels + str(node.key))
        self.display(node.left, levels + 1)

    def find_min_node(self, node):
        """ find minimum node """
        while node.left:
            node = node.left
        return node.key

    def find_max_node(self, node):
        """ find maximum node """
        while node.right:
            node = node.right
        return node.key


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

print("\ninorder: ")
bst.inorder(root)

print("\n")
print("min: ", bst.find_min_node(root))
print("max: ", bst.find_max_node(root))
