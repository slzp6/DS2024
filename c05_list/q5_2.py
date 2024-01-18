""" q5_2.py """

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
        curr = self.head
        while curr is not None:
            print(curr.key, end=" ")
            curr = curr.ref_next

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

N = 10000000
random.seed(1)
rnbs = random.sample(range(N), N)
print("n = ", N)

ts_a = time.time()
for i in rnbs:
    ll_a.insert_head(i)
te_a = time.time()

print("head : ", te_a - ts_a)

#
# AMD_Ryzen_9_5950X
# n =  10000000
# head :  24.8464994430542
#
