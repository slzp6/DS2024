""" c5_6.py """


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

    def insert_mid(self, pos, key):
        """ insert a key into a LL (middle) """
        index = 0
        curr = self.head
        while index < pos - 1 and curr is not None:
            index += 1
            curr = curr.ref_next
        if pos == 0:
            new_node = Node(key)
            new_node.ref_next = curr
            self.head = new_node
        else:
            new_node = Node(key)
            new_node.ref_next = curr.ref_next
            curr.ref_next = new_node


ll = LinkedList()

ll.insert_head(10)
ll.insert_head(20)
ll.insert_head(30)
ll.insert_head(40)
ll.insert_head(50)

ll.insert_mid(3, 25)

ll.display()
