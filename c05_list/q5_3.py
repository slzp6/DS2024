""" q5_3.py """

import random
import time


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
        node_temp = self.head
        while node_temp is not None:
            print(node_temp.key, end=" ")
            node_temp = node_temp.ref_next

    def insert_head(self, key):
        """ insert a key into a LL (head) """
        node = Node(key)
        node.ref_next = self.head
        self.head = node

    def insert_tail(self, key):
        """ insert a key into a LL (tail) """
        node = Node(key)
        if self.head is None:
            self.head = node
            return

        last = self.head

        while last.ref_next is not None:
            last = last.ref_next

        last.ref_next = node


ll_a = LinkedList()
ll_b = LinkedList()

N = 10000
print("n = ", N)
random.seed(1)
rnbs = random.sample(range(N), N)

ts_a = time.time()
for i in rnbs:
    ll_a.insert_head(i)
te_a = time.time()

ts_b = time.time()
for i in rnbs:
    ll_b.insert_tail(i)
te_b = time.time()

print("head : ", te_a - ts_a)
print("tail : ", te_b - ts_b)

# ll.display()
