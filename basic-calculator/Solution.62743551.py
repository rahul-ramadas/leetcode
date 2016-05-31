class Solution:

    def convert_to_postfix(self, s):
        op_pri = {
            "(": 0,
            ")": 0,
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2
        }

        elems = [elem if elem in op_pri.keys() else int(elem.strip()) for elem in re.split("([\+\-\*/\(\)])", s) if elem.strip() != ""]

        postfix = []
        op_stack = []
        for elem in elems:
            if elem not in op_pri.keys():
                postfix.append(elem)
            elif elem == "(":
                op_stack.append(elem)
            elif elem == ")":
                while op_stack[-1] != "(":
                    op = op_stack.pop()
                    postfix.append(op)
                op_stack.pop()
            else:
                while op_stack and op_pri[op_stack[-1]] >= op_pri[elem]:
                    op = op_stack.pop()
                    postfix.append(op)
                op_stack.append(elem)

        while op_stack:
            op = op_stack.pop()
            if op != "(":
                postfix.append(op)

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
