class Solution:

    def solve(self, num, begin, target, cur_ops, cur_val, last_num, solutions):
        if begin == len(num):
            if cur_val == target:
                solutions.append("".join(str(i) for i in cur_ops))
            return

        def compute_new_val():
            if op == "+":
                return cur_val + next_num, next_num

            if op == "-":
                return cur_val - next_num, -1 * next_num

            if len(cur_ops) == 1:
                return cur_val * next_num, cur_val * next_num

            computed_val = cur_val - last_num + (last_num * next_num)
            computed_last = last_num * next_num
            return computed_val, computed_last

        for end in xrange(begin + 1, len(num) + 1):
            num_str = num[begin:end]
            if len(num_str) > 1 and num_str.startswith("0"):
                continue

            next_num = int(num_str)
            if cur_ops:
                for op in ["+", "-", "*"]:
                    new_val, new_last_num = compute_new_val()
                    cur_ops.append(op)
                    cur_ops.append(next_num)
                    self.solve(num, end, target, cur_ops, new_val, new_last_num, solutions)
                    del cur_ops[-2:]
            else:
                new_val = next_num
                cur_ops.append(next_num)
                self.solve(num, end, target, cur_ops, new_val, next_num, solutions)
                del cur_ops[-1:]

        return solutions

    def addOperators(self, num, target):
        solutions = []
        cur_ops = []
        cur_val = 0
        self.solve(num, 0, target, cur_ops, cur_val, 0, solutions)
        return solutions
