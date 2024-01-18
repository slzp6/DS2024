""" c8_3.py """


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

    def find_parent_node(self, key):
        """ find a parent node """
        parent = None
        curr = self.root

        if curr is None:
            return (parent, None)
        while True:
            if curr.key == key:
                return parent, curr
            if curr.key > key:
                parent = curr
                curr = curr.left
            else:
                parent = curr
                curr = curr.right
        return parent, curr

    def count_child_node(self, node):
        """ count child nodes """
        n_child_node = 0

        if node.left and node.right:
            n_child_node = 2
        elif (node.left is None) and (node.right is None):
            n_child_node = 0
        else:
            n_child_node = 1
        return n_child_node

    def delete_node_0(self, parent, node):
        """ n_child_node == 0 """
        if parent:
            if parent.right is node:
                parent.right = None
            else:
                parent.left = None
        else:
            self.root = None

    def delete_node_1(self, parent, node):
        """ n_child_node == 1 """
        next_node = None
        if node.left:
            next_node = node.left
        else:
            next_node = node.right

        if parent:
            if parent.left is node:
                parent.left = next_node
            else:
                parent.right = next_node
        else:
            self.root = next_node

    def delete_node_2(self, node):
        """ n_child_node == 2 """
        parent_lm_node = node
        lm_node = node.right
        while lm_node.left:
            parent_lm_node = lm_node
            lm_node = lm_node.left

        node.key = lm_node.key

        if parent_lm_node.left == lm_node:
            parent_lm_node.left = lm_node.right
        else:
            parent_lm_node.right = lm_node.right

    def delete(self, key):
        """ delete a key from a bst """
        parent, node = self.find_parent_node(key)

        if parent is None and node is None:
            return None

        n_child_node = self.count_child_node(node)
        if n_child_node == 0:
            self.delete_node_0(parent, node)
        elif n_child_node == 1:
            self.delete_node_1(parent, node)
        else:
            self.delete_node_2(node)
        return None


nodes = [90, 50, 20, 70, 10, 30, 60, 25, 35]
bst = BST()

for i in nodes:
    bst.insert(i)

print("BST:")
bst.display_nodes()

print("\n***")
# N1 = 35
# N1 = 70
N1 = 50

print("delete:", N1)
bst.delete(N1)

print("\nBST:")
bst.display_nodes()
