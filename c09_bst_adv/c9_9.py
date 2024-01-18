""" c9_9.py """

import random
import gc
import psutil

G_DATA_SIZE = 1000000
# Data size of each node.
# Do not set the value too high.
# This is the value tested on
# a PC with 32GB of memory.


class Node:
    """ node """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.data = [1] * G_DATA_SIZE


class BST:
    """ bst """
    def __init__(self):
        self.root = None

    def inorder(self, node):
        """ inorder traversal (helper) """
        if node is None:
            return
        self.inorder(node.left)
        print(node.key, end=" ")
        self.inorder(node.right)

    def traversal_inorder(self):
        """ inorder traversal """
        self.inorder(self.root)

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

    def delete_bst(self, node):
        """ delete a bst """
        if node is None:
            return
        self.delete_bst(node.left)
        self.delete_bst(node.right)
        node.left = None
        node.right = None
        node.key = None

    def delete_bst_nodes(self):
        """ delete a bst (wrapper function)"""
        self.delete_bst(self.root)
        self.root = None


N = 1000
random.seed(1)
rnbs = random.sample(range(N), N)

bst = BST()

print("gc collect: ", gc.collect())

mem = psutil.virtual_memory()
print("memory (0):", mem.percent)

print("\nBST(insert):")
for i in rnbs:
    bst.insert(i)
print(" n:", N)
print(" node data size:", G_DATA_SIZE)
print(" height:", bst.find_bst_height())

mem = psutil.virtual_memory()
print("memory (1):", mem.percent)

print("\nBST (delete):")
# bst.delete_bst_nodes()

print("gc collect: ", gc.collect())

mem = psutil.virtual_memory()
print("memory (2):", mem.percent)
