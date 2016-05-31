class Solution:

    def convert_to_postfix(self, s):
        op_pri = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2
        }

        elems = [elem if elem in op_pri.keys() else int(elem.strip()) for elem in re.split("([\+\-\*/])", s)]

        postfix = []
        op_stack = []
        for elem in elems:
            if elem not in op_pri.keys():
                postfix.append(elem)
                continue

            while op_stack and op_pri[op_stack[-1]] >= op_pri[elem]:
                postfix.append(op_stack.pop())
            op_stack.append(elem)

        while op_stack:
            postfix.append(op_stack.pop())

        return postfix

    def eval_postfix(self, s):
        ops = {
            "+": lambda lhs, rhs: lhs + rhs,
            "-": lambda lhs, rhs: lhs - rhs,
            "*": lambda lhs, rhs: lhs * rhs,
            "/": lambda lhs, rhs: lhs / rhs
        }

        stack = []
        for elem in s:
            if elem not in ops.keys():
                stack.append(elem)
                continue

            rhs = stack.pop()
            lhs = stack.pop()
            stack.append(ops[elem](lhs, rhs))

        return stack[-1]

    def calculate(self, s):
        s = self.convert_to_postfix(s)
        res = self.eval_postfix(s)
        return res
