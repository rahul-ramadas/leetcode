class Solution:

    def longestIncreasingPath(self, matrix):
        lengths = [[0] * len(row) for row in matrix]

        max_length = 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                max_length = max(max_length, self.get_longest_path(matrix, i, j, lengths))

        return max_length

    def get_longest_path(self, matrix, i, j, lengths):
        if lengths[i][j] != 0:
            return lengths[i][j]

        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        max_length = 0
        for offset in offsets:
            ip = i + offset[0]
            jp = j + offset[1]

            if ip < 0 or ip >= len(matrix):
                continue

            if jp < 0 or jp >= len(matrix[ip]):
                continue

            if matrix[ip][jp] <= matrix[i][j]:
                continue

            max_length = max(max_length, self.get_longest_path(matrix, ip, jp, lengths))

        max_length += 1
        lengths[i][j] = max_length
        return max_length
