class Solution:

    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        row = [0] * len(matrix[0])
        res = 0

        for i in xrange(len(matrix)):
            top_left = 0
            for j in xrange(len(matrix[i])):
                if matrix[i][j] == "0":
                    top_left = row[j]
                    row[j] = 0
                else:
                    val = min(row[j], row[j - 1] if j > 0 else 0, top_left) + 1
                    top_left = row[j]
                    row[j] = val
                res = max(res, row[j])

        return res ** 2
