class Solution:

    def rotate(self, matrix):
        n = len(matrix)
        for i in xrange(n / 2):
            ilen = n - 2 * i - 1
            for j in xrange(i, i + ilen):
                temp = matrix[-(j + 1)][i]
                matrix[-(j + 1)][i] = matrix[-(i + 1)][-(j + 1)]
                matrix[-(i + 1)][-(j + 1)] = matrix[j][-(i + 1)]
                matrix[j][-(i + 1)] = matrix[i][j]
                matrix[i][j] = temp

        return matrix
