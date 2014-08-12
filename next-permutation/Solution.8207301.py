class Solution:

    def nextPermutation(self, num):
        res = num[:]
        if not res:
            return []

        index = len(res) - 2
        while index >= 0 and res[index] >= res[index + 1]:
            index -= 1

        if index < 0:
            return sorted(res)

        index2 = len(res) - 1
        while res[index2] <= res[index]:
            index2 -= 1

        res[index], res[index2] = res[index2], res[index]
        return res[:index + 1] + res[-1:index:-1]
