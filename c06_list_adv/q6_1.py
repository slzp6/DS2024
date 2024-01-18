""" q6_1.py """

import random
import time


class Node:
    """ node """
    def __init__(self, key):
        self.key = key
        self.ref_next = None


class StackLL:
    """ linked list implementation of a stack """
    def __init__(self):
        self.head = None

    def push(self, key):
        """ push """
        node = Node(key)
        node.ref_next = self.head
        self.head = node

    def pop(self):
        """ pop """
        if self.head is None:
            print("Empty")
            return None
        node = self.head
        self.head = self.head.ref_next
        return node.key

    def get_items(self):
        """ get stack items """
        stack_items = []
        curr = self.head
        while curr is not None:
            stack_items += [curr.key]
            curr = curr.ref_next
        return stack_items


sll = StackLL()

N = 30000
random.seed(1)
rnbs = random.sample(range(N), N)

print(sll.get_items())

ts_a = time.time()
for i in rnbs:
    sll.push(i)
te_a = time.time()

print(sll.get_items()[0:10])

ts_b = time.time()
for i in range(len(rnbs)):
    sll.pop()
te_b = time.time()

print(sll.get_items()[0:10])

print("n: ", N)
print("push : ", te_a - ts_a)
print("pop  : ", te_b - ts_b)
