""" q3_5.py """

import random
import time


class MyStack:
    """ stack """
    def __init__(self):
        self.data = []

    def push(self, data):
        """ push """
        self.data.append(data)

    def pop(self):
        """ pop """
        return self.data.pop()

    def display(self):
        """ display """
        print(self.data)

    def is_empty(self):
        """ is_empty """
        return not self.data
        # i.e.
        # return self.data == []

    def is_empty2(self):
        """ is_empty2 """
        return len(self.data) == 0

    def is_empty3(self):
        """ is_empty3 """
        return bool(not self.data)


st = MyStack()

N = 10_000_000
# N = 1_000_000
random.seed(1)
a = random.sample(range(0, N), N)
L = len(a)

print("N =", N)
print("statck: ", end="")
st.display()

print("push -> ", end="")
t_start = time.time()
for i in a:
    st.push(i)
t_end = time.time()
t_elapsed = t_end - t_start
print(f"elapsed time: {t_elapsed:.3f} sec.")

print("")
# st.display()

print("pop  -> ", end="")
t_start = time.time()
for i in range(L):
    st.pop()
t_end = time.time()
t_elapsed = t_end - t_start
print(f"elapsed time: {t_elapsed:.3f} sec.")
print("statck: ", end="")
st.display()
