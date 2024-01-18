""" c12_8.py """

import collections
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
        """ display (helper) """
        if node is None:
            return
        self.display(node.right, levels + 1)
        print('-' * 4 * levels + str(node.key))
        self.display(node.left, levels + 1)

    def display_nodes(self):
        """ display """
        self.display(self.root, 0)

    def inorder(self, node):
        """ inorder traversal """
        if node is None:
            return
        self.inorder(node.left)
        print(node.key, end=" ")
        self.inorder(node.right)

    def inorder_list(self, node):
        """ inorder traversal returning a list """
        if node is None:
            return []
        left_list = self.inorder_list(node.left)
        right_list = self.inorder_list(node.right)
        return left_list + [node.key] + right_list

    def inorder_stack(self, node):
        """ iterative inorder traversal (stack) """
        stack = collections.deque()
        nodes = []
        while len(stack) > 0 or node is not None:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                nodes.append(node.key)
                node = node.right
        return nodes


N = 10000
random.seed(1)
rnbs = random.sample(range(N), N)

print("rnbs: ", rnbs[:3], "...", rnbs[-3:])

bst = BST()

print("bst insert ", N, "...")
for i in rnbs:
    bst.insert(i)

print("done")

print("\ninorder traversal using stack: ")
ra = bst.inorder_stack(bst.root)
print(ra[:3], "...", ra[-3:])

print("\ninorder_recursion: ")
rb = bst.inorder_list(bst.root)
print(rb[:3], "...", rb[-3:])
