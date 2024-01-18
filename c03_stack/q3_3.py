""" q3_3.py """


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

st.display()
print("empty:", st.is_empty())

st.push(100)
st.push(200)
st.push(300)
st.display()
print("empty:", st.is_empty())

st.pop()
st.pop()
st.pop()
st.display()
print("empty:", st.is_empty())
