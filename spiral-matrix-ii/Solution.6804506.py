class Solution:
    def generateMatrix(self, n):
        result = [[0] * n for _ in xrange(n)]

        num = 1
        for k in xrange(n, 0, -2):
            i = (n - k) / 2
            for j in xrange(i, i + k):
                result[i][j] = num
                num += 1

            for i in xrange(i + 1, i + k):
                result[i][j] = num
                num += 1

            for j in xrange(j - 1, j - k, -1):
                result[i][j] = num
                num += 1

            for i in xrange(i - 1, i - (k - 1), -1):
                result[i][j] = num
                num += 1

        return result
