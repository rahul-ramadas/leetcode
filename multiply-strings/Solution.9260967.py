class Solution:

    def add(self, num1, num2):
        num = []
        carry = 0

        maxLen = max(len(num1), len(num2))
        num1.extend(itertools.repeat(0, maxLen - len(num1)))
        num2.extend(itertools.repeat(0, maxLen - len(num2)))

        for a, b in zip(num1, num2):
            sum = a + b + carry
            num.append(sum % 10)
            carry = sum / 10

        if carry:
            num.append(carry)

        return num

    def multiply_digit(self, num, digit, place):
        res = [0] * place
        carry = 0

        for d in num:
            prod = digit * d + carry
            res.append(prod % 10)
            carry = prod / 10

        if carry:
            res.append(carry)

        return res

    def multiply_numbers(self, num1, num2):

        res = [0]
        place = 0

        for d in num2:
            prod = self.multiply_digit(num1, d, place)
            res = self.add(res, prod)
            place += 1

        return res

    def multiply(self, num1, num2):

        if num1 == '0' or num2 == '0':
            return '0'

        num1List = list(map(int, reversed(num1)))
        num2List = list(map(int, reversed(num2)))

        res = self.multiply_numbers(num1List, num2List)

        return ''.join(map(str, reversed(res)))
