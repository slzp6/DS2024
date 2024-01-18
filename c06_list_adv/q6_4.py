""" q6_4.py """

import random


class Node:
    """ node """
    def __init__(self, key):
        self.key = key
        self.ref_next = None
        self.ref_prev = None


class DLL:
    """ doubly linked list """
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key):
        """ insert a key into a DLL """
        node = Node(key)

        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.ref_prev = self.tail
            self.tail.ref_next = node
            self.tail = node

    def delete(self, key):
        """ delete a key from a DLL """
        curr = self.head
        node_del = False
        if curr is None:
            node_del = False

        elif curr.key == key:
            self.head = curr.ref_next
            self.head.ref_prev = None
            node_del = True
            key_val = key
        elif self.tail.key == key:
            self.tail = self.tail.ref_prev
            self.tail.ref_next = None
            node_del = True
            key_val = key
        else:
            while curr:
                if curr.key == key:
                    curr.ref_prev.ref_next = curr.ref_next
                    curr.ref_next.ref_prev = curr.ref_prev
                    node_del = True
                    key_val = key
                curr = curr.ref_next
        if node_del is True:
            return key_val
        return None

    def get_list(self):
        """ get DLL items """
        items = []
        curr = self.head
        while curr is not None:
            items.append(curr.key)
            curr = curr.ref_next
        return items

    def get_list_rev(self):
        """ get DLL items (reverse order) """
        items = []
        curr = self.tail
        while curr is not None:
            items.append(curr.key)
            curr = curr.ref_prev
        return items


N = 8
M = N // 2
random.seed(1)
rnbs = random.sample(range(N), N)

dll = DLL()

for i in rnbs:
    dll.insert(i)
    print("insert: ", i)
    print("DLL: ", dll.get_list())

print("---")
for i in random.sample(rnbs, M):
    print("delete: ", dll.delete(i))
    print("DLL: ", dll.get_list())

print("---")
print("DLL(forward): ", dll.get_list())
print("DLL(reverse): ", dll.get_list_rev())
