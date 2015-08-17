class Solution:

    def calculate(self, op, lhs, rhs):
        if op == "*":
            return lhs * rhs
        if op == "-":
            return lhs - rhs
        if op == "+":
            return lhs + rhs

    def diffWaysToCompute(self, input):
        operands = [int(o) for o in re.split("[*+-]", input)]
        operators = re.findall("[*+-]", input)

        num = len(operands)
        results = [[[] for j in range(num + 1)] for i in range(num)]

        for i in range(num):
            results[i][1].append(operands[i])

        for l in range(2, num + 1):
            for i in range(0, num - l + 1):
                for j in range(i + 1, i + l):
                    lhs = results[i][j - i]
                    rhs = results[j][i + l - j]
                    op = operators[j - 1]

                    for a, b in itertools.product(lhs, rhs):
                        results[i][l].append(self.calculate(op, a, b))

        return results[0][num]
