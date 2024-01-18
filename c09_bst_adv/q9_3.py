""" q9_3.py """

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

    def inorder(self, node):
        """ inorder traversal (helper)  """
        if node is None:
            return
        self.inorder(node.left)
        print(node.key, end=" ")
        self.inorder(node.right)

    def traversal_inorder(self):
        """ inorder traversal """
        self.inorder(self.root)

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

    def find_height(self, node):
        """ find a height of a bst (helper) """
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

    def find_bst_height(self):
        """ height """
        return self.find_height(self.root)

    def insert_sorted_list(self, sorted_ls):
        """ convert a sorted list to a bst """
        if not sorted_ls:
            return None

        mid = len(sorted_ls) // 2
        # print("mid:", sorted_ls[mid])
        node = Node(sorted_ls[mid])
        if self.root is None:
            self.root = node

        node.left = \
            self.insert_sorted_list(sorted_ls[:mid])
        node.right = \
            self.insert_sorted_list(sorted_ls[mid + 1:])
        return node


N = 7
random.seed(1)
rnbs = random.sample(range(N), N)

nodes_a = sorted(rnbs)
nodes_b = sorted(rnbs)

print("nodes:    ", rnbs)
print("nodes (a):", nodes_a)
print("nodes (b):", nodes_b)
bst_a = BST()
bst_b = BST()

for i in nodes_a:
    bst_a.insert(i)

print("\nBST a:")
bst_a.display_nodes()

bst_b.insert_sorted_list(nodes_b)
print("\nBST b:")
bst_b.display_nodes()
