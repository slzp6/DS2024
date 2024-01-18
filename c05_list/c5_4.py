""" c5_4.py """


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
        """ insert a key into a LL """
        node = Node(key)
        node.ref_next = self.head
        self.head = node


ll = LinkedList()

ll.insert_head(10)
ll.insert_head(20)
ll.insert_head(30)
ll.insert_head(40)
ll.insert_head(50)

ll.display()
