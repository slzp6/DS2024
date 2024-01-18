""" q5_1.py """

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
        print("")

    def insert_head(self, key):
        """ insert a key into a LL (head) """
        node = Node(key)
        node.ref_next = self.head
        self.head = node


ll = LinkedList()

random.seed(1)
rnbs = random.sample(range(15), 10)

for i in rnbs:
    ll.insert_head(i)

ll.display()
