""" q3_4.py """


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


def compute(operand, opr1, opr2):
    """ basic arithmetic operations """
    if operand == '+':
        return opr1 + opr2
    if operand == '-':
        return opr1 - opr2
    if operand == '*':
        return opr1 * opr2
    if operand == '/':
        return opr1 / opr2
    if operand == '^':
        return opr1**opr2
    return None


def eval_rpn(rpn_exp):
    """ evaluate rpn """
    op_list = ['+', '-', '*', '/', '^']
    stack = MyStack()
    t_list = rpn_exp.split(' ')

    for token in t_list:
        print(token, end=': ')
        if token in op_list:
            opr2 = stack.pop()
            opr1 = stack.pop()
            result = compute(token, opr1, opr2)
            stack.push(result)
        else:
            op_value = float(token)
            stack.push(op_value)

        stack.display()

    return stack.pop()


RPN = "5 1 2 + 4 * + 3 -"
print("RPN: ", RPN)
print("Result: ", eval_rpn(RPN))
