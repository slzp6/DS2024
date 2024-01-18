""" q5_6.py """

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

    def replace(self, item_old, item_new):
        """ replace """
        count = 0
        curr = self.head
        while curr is not None:
            if curr.key == item_old:
                curr.key = item_new
                count += 1
            curr = curr.ref_next
        return count


ll = LinkedList()

N = 10
random.seed(1)
rnbs = random.sample(range(N), N)

for i in rnbs:
    ll.insert_head(i)

print("n: ", N)
print("linked list: ", ll.get_item_list())

val_x = rnbs[N // 2]
val_y = rnbs[N // 4]

val_a = val_x + 10
val_b = val_y + 100

S1 = ll.replace(val_x, val_a)
print(f"\n{val_x} -> {val_a}  [{S1}]")
print("linked list: ", ll.get_item_list())

S2 = ll.replace(val_y, val_a)
print(f"\n{val_y} -> {val_a}  [{S2}]")
print("linked list: ", ll.get_item_list())

S3 = ll.replace(val_a, val_b)
print(f"\n{val_a} -> {val_b}  [{S3}]")
print("linked list: ", ll.get_item_list())
