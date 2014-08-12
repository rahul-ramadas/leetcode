class Solution:
    def grayCode(self, n):
        result = [0]
        for i in xrange(1, n + 1):
            result += [2 ** (i - 1) + x for x in reversed(result)]

        return result