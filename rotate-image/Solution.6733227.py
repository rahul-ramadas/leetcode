class Solution:

    def transpose(self, matrix):
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def mirror_vertical(self, matrix):
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(n / 2):
                ind = -(j + 1)
                matrix[i][j], matrix[i][ind] = matrix[i][ind], matrix[i][j]

    def rotate(self, matrix):
        self.transpose(matrix)
        self.mirror_vertical(matrix)
        return matrix
