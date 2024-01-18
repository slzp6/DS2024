""" q4_7.py """


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

    def display_all_elements(self):
        """ display all elements in Q"""
        if self.head == -1:
            print("circular queue: Empty")
        print("[ ", end='')
        for idx in range(0, self.max_size):
            if self.key[idx] is None:
                print('_', end=' ')
            else:
                print(self.key[idx], end=' ')
        print('] ', end='')
        print("head:", self.head, "tail:", self.tail)


q = MyCircularQueue(5)
q.display_all_elements()

for i in range(0, 5):
    ch = chr(ord('A') + i)
    print(" enqueue:", ch)
    q.enqueue(ch)
    q.display_all_elements()

print('')
for i in range(0, 3):
    print(" dequeue:", q.dequeue())
    q.display_all_elements()

print('')
for i in range(0, 2):
    ch = chr(ord('X') + i)
    print(" enqueue:", ch)
    q.enqueue(ch)
    q.display_all_elements()

print('')
for i in range(0, 3):
    print(" dequeue:", q.dequeue())
    q.display_all_elements()
