""" q5_5.py """

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

    def get_item_list(self):
        """ get items """
        items = []
        curr = self.head
        while curr is not None:
            items += [curr.key]
            curr = curr.ref_next
        return items


ll = LinkedList()

N = 10
random.seed(1)
rnbs = random.sample(range(N), N)

for i in rnbs:
    ll.insert_head(i)

print("n: ", N)
print("linked list: ", ll.get_item_list())
