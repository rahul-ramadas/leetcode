class Solution:

    def evalRPN(self, tokens):
        theStack = []
        ops = ['+', '-', '*', '/']
        for elem in tokens:
            if elem in ops:
                operand2 = float(theStack.pop())
                operand1 = float(theStack.pop())
                theStack.append(int(eval(str(operand1) + elem + str(operand2))))
            else:
                theStack.append(int(elem))
        return theStack.pop()
