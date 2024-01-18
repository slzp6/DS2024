""" c9_5.py """

import random
import sys
import time


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


print("get recursion limit:", sys.getrecursionlimit())
sys.setrecursionlimit(3000)
print("get recursion limit:", sys.getrecursionlimit())

N = 1000
random.seed(1)
rnbs_a = random.sample(range(N), N)

random.seed(2)
rnbs_b = random.sample(range(N), N)
rnbs_b.sort()

print("n=", N)
print("rnbs_a: ", rnbs_a[:3], "...", rnbs_a[-3:])
print("rnbs_b: ", rnbs_b[:3], "...", rnbs_b[-3:])
print("")

bst_a = BST()
bst_b = BST()

ta_start = time.time()
for i in rnbs_a:
    bst_a.insert(i)
ta_end = time.time()
print(f"elapsed time (a): {ta_end - ta_start} (sec.)")

tb_start = time.time()
for i in rnbs_b:
    bst_b.insert(i)
tb_end = time.time()
print(f"elapsed time (b): {tb_end - tb_start} (sec.)")
print(f"(b)/(a): {(tb_end - tb_start)/(ta_end - ta_start)}")

print("\n*** height")
print("BST a:", bst_a.find_bst_height())
print("BST b:", bst_b.find_bst_height())

# print("\n*** BST a:")
# bst_a.display(bst_a.root)
# print("\n*** BST b:")
# bst_b.display(bst_b.root)
