class Solution:
    def getRow(self, rowIndex):
        def n_c_r(n, r):
            numerator = 1

            for i in xrange(1, r + 1):
                numerator *= n - (i - 1)
                numerator /= i

            return numerator

        return [n_c_r(rowIndex, i) for i in xrange(rowIndex + 1)]
