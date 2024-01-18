""" q4_1.py """


class MyQueue:
    """ queue """
    def __init__(self):
        self.data = []

    def enqueue(self, data):
        """ enqueue """
        self.data.append(data)

    def dequeue(self):
        """ dequeue """
        return self.data.pop(0)

    def items(self):
        """ items """
        return self.data


q = MyQueue()

print("queue:", q.items())

print(" enqueue: 10")
q.enqueue(10)
print(" enqueue: 30")
q.enqueue(30)
print(" enqueue: 20")
q.enqueue(20)
print("queue:", q.items())

print(" enqueue: 50")
q.enqueue(50)
print(" enqueue: 40")
q.enqueue(40)
print("queue:", q.items())

print(" dequeue:", q.dequeue())
print(" dequeue:", q.dequeue())
print("queue:", q.items())
