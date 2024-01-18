""" c6_2.py """


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


items = [10, 20, 30, 40, 50]

qll = QueueLL()

print(qll.get_items())

for i in items:
    qll.enqueue(i)
    print("enqueue:", i, end=" ")
    print(qll.get_items())

for i in range(len(items)):
    print("dequeue:", qll.dequeue(), end=" ")
    print(qll.get_items())
