""" q6_5.py """

import random


class Node:
    """ node """
    def __init__(self, key=None):
        self.key = key
        self.ref_next = None


class CLL:
    """ circular linked list """
    def __init__(self):
        self.tail = None
        self.head = None

    def insert(self, key):
        """ insert a key into a CLL """
        node = Node(key)
        if self.tail:
            self.tail.ref_next = node
            self.tail = node
            node.ref_next = self.head
        else:
            self.head = node
            self.tail = node
            self.tail.ref_next = self.tail

    def delete(self, key):
        """ delete a key from a CLL """
        current = self.head
        prev = self.head
        find_key = False
        while prev == current or prev != self.tail:
            if current.key == key:
                if current == self.head:
                    self.head = current.ref_next
                    self.tail.ref_next = self.head
                elif current == self.tail:
                    self.tail = prev
                    prev.ref_next = self.head
                else:
                    prev.ref_next = current.ref_next
                return
            prev = current
            current = current.ref_next
        if find_key is False:
            # print("Not found:", key)
            return

    def get_list(self):
        """ get CLL items """
        items = []
        current = self.head
        loop = True
        while current is not None and loop:
            items.append(current.key)
            current = current.ref_next
            if current == self.head:
                loop = False
        return items

    def get_list_n(self, repeat=1):
        """ get DLL items (repeat n times) """
        items = []
        count = 0
        current = self.head
        loop = True
        while current is not None and loop:
            items.append(current.key)
            current = current.ref_next
            if current == self.head:
                count += 1
                if count == repeat:
                    loop = False
        return items


N = 8
M = N // 2
random.seed(1)
rnbs = random.sample(range(N), N)

cll = CLL()

for i in rnbs:
    cll.insert(i)
    print("insert: ", i)
    print("CLL: ", cll.get_list())

print("---")
for i in random.sample(rnbs, M):
    print("delete: ", i)
    cll.delete(i)
    print("CLL: ", cll.get_list())

print("---")
R = 3
print("CLL x", R, ":", cll.get_list_n(R))
