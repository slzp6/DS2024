""" c5_5.py """


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
        print("")

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


ll = LinkedList()

ll.insert_tail(10)
ll.insert_tail(20)
ll.insert_tail(30)
ll.insert_tail(40)
ll.insert_tail(50)

ll.display()
