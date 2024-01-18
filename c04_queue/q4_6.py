""" q4_6.py """


class MyCircularQueue:
    """ circular queue """
    def __init__(self, max_size):
        self.max_size = max_size
        self.key = [None] * max_size
        self.head = -1
        self.tail = -1

    def enqueue(self, key):
        """ enqueue """
        if self.head == (self.tail + 1) % self.max_size:
            print("circular queue (enqueue): Full")
            return None
        if self.head == -1:
            self.head = 0
            self.tail = 0
            self.key[self.tail] = key
        else:
            self.tail = (self.tail + 1) % self.max_size
            self.key[self.tail] = key
        return key

    def dequeue(self):
        """ dequeue """
        if self.head == -1:
            print("circular queue (dequeue): Empty")
            return None
        if self.head == self.tail:
            key = self.key[self.head]
            self.key[self.head] = None
            self.head = -1
            self.tail = -1
            return key
        key = self.key[self.head]
        self.key[self.head] = None
        self.head = (self.head + 1) % self.max_size
        return key

    def display(self):
        """ display """
        if self.head == -1:
            print("circular queue: Empty")

        elif self.head <= self.tail:
            for idx in range(self.head, self.tail + 1):
                print(self.key[idx], end=' ')
            print('')
        else:
            for idx in range(self.head, self.max_size):
                print(self.key[idx], end=' ')
            for idx in range(0, self.tail + 1):
                print(self.key[idx], end=' ')
            print('')


q = MyCircularQueue(64)

q.display()
q.enqueue('H')
q.enqueue('E')
q.enqueue('L')
q.enqueue('L')
q.enqueue('O')
q.display()

print(" dequeue:", q.dequeue())
print(" dequeue:", q.dequeue())
print(" dequeue:", q.dequeue())
print(" dequeue:", q.dequeue())
print(" dequeue:", q.dequeue())
q.display()
