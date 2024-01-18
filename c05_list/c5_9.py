""" c5_9.py """


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
        print("\n")

    def insert_head(self, key):
        """ insert a key into a LL (head) """
        node = Node(key)
        node.ref_next = self.head
        self.head = node

    def delete_head(self):
        """ delete a key from a LL (head) """
        if self.head is None:
            print("Empty")
            return None
        node = self.head
        self.head = self.head.ref_next
        return node.key

    def delete_tail(self):
        """ delete a key from a LL (tail) """
        if self.head is None:
            print("Empty")
            return None
        curr = self.head
        prev = None
        while curr.ref_next is not None:
            prev = curr
            curr = curr.ref_next
        prev.ref_next = None
        return curr.key

    def delete_mid(self, pos):
        """ delete a key from a LL (middle) """
        if self.head is None:
            print("Empty")
            return None
        curr = self.head
        prev = None
        index = 0
        while curr.ref_next is not None and index < pos:
            prev = curr
            curr = curr.ref_next
            index += 1
        if curr == self.head:
            self.head = curr.ref_next
            mid_key = curr.key
        else:
            prev.ref_next = curr.ref_next
            mid_key = curr.key
        return mid_key


ll = LinkedList()

ll.insert_head(10)
ll.insert_head(20)
ll.insert_head(30)
ll.insert_head(40)
ll.insert_head(50)

print("linked list")
ll.display()

I = 3
print(f"deleted (index {I}): ", ll.delete_mid(I))
ll.display()

I = 2
print(f"deleted (index {I}): ", ll.delete_mid(I))
ll.display()
