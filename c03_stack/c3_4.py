""" c3_4.py """


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


st = MyStack()

st.display()
st.push('H')
st.push('E')
st.push('L')
st.push('L')
st.push('O')
st.display()

print(" pop:", st.pop())
print(" pop:", st.pop())
print(" pop:", st.pop())
print(" pop:", st.pop())
print(" pop:", st.pop())
st.display()
