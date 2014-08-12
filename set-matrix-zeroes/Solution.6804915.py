class Solution:
    def setZeroes(self, matrix):
        firstRowZeros = 0 in matrix[0]
        firstColZeros = 0 in next(itertools.izip(*matrix))

        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                if matrix[i][j]:
                    continue

                matrix[0][j] = 0
                matrix[i][0] = 0

        for i in xrange(1, len(matrix)):
            if matrix[i][0]:
                continue

            for j in xrange(1, len(matrix[i])):
                matrix[i][j] = 0

        for j in xrange(1, len(matrix[0])):
            if matrix[0][j]:
                continue

            for i in xrange(1, len(matrix)):
                matrix[i][j] = 0

        if firstRowZeros:
            for j in xrange(0, len(matrix[0])):
                matrix[0][j] = 0

        if firstColZeros:
            for i in xrange(0, len(matrix)):
                matrix[i][0] = 0
