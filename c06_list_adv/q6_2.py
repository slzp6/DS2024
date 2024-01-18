""" q6_2.py """

import random
import time


class Node:
    """ node """
    def __init__(self, key):
        self.key = key
        self.ref_next = None


class QueueLL:
    """ linked list implementation of a queue """
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, key):
        """ enqueue """
        node = Node(key)

        if self.rear is None:
            self.front = node
            self.rear = node
            return

        self.rear.ref_next = node
        self.rear = node

    def dequeue(self):
        """ dequeue """
        if self.front is None:
            print("empty")
            return None

        node = self.front
        dequeue_key = node.key
        self.front = node.ref_next

        if self.front is None:
            self.rear = None

        return dequeue_key

    def get_items(self):
        """ get queue items """
        q_items = []
        curr = self.front
        while curr is not None:
            q_items += [curr.key]
            curr = curr.ref_next
        return q_items


N = 30000
random.seed(1)
rnbs = random.sample(range(N), N)

qll = QueueLL()

print(qll.get_items())

ts_a = time.time()
for i in rnbs:
    qll.enqueue(i)
te_a = time.time()

print(qll.get_items()[0:10])

ts_b = time.time()
for i in range(len(rnbs)):
    qll.dequeue()
te_b = time.time()

print(qll.get_items()[0:10])

print("n: ", N)
print("enqueue : ", te_a - ts_a)
print("dequeue : ", te_b - ts_b)
