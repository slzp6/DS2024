""" q5_4.py """

import random


class Node:
    """ node """
    def __init__(self, key):
        self.key = key
        self.ref_next = None


class LinkedList:
    """ linked list """
    def __init__(self):
        self.head = None

    def display(self):
        """ display """
        curr = self.head
        while curr is not None:
            print(curr.key, end=" ")
            curr = curr.ref_next

    def insert_head(self, key):
        """ insert a key into a LL (head) """
        node = Node(key)
        node.ref_next = self.head
        self.head = node

    def count_nodes(self):
        """ count nodes"""
        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.ref_next

        return count


ll = LinkedList()

N = 100000
random.seed(1)
rnbs = random.sample(range(N), N)

for i in rnbs:
    ll.insert_head(i)

print("n: ", N)
print("node(s): ", ll.count_nodes())
