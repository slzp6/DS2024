""" c6_1.py """


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


items = [10, 20, 30, 40, 50]

sll = StackLL()

print(sll.get_items())

for i in items:
    sll.push(i)
    print("push:", i, end=" ")
    print(sll.get_items())

for i in range(len(items)):
    print("pop: ", sll.pop(), end=" ")
    print(sll.get_items())
