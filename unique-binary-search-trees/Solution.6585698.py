class Solution:
    def numTrees(self, n):
        dpTable = [[0 for y in xrange(0, n + 2)] for x in xrange(0, n + 2)]
        for x in xrange(1, n + 2):
            dpTable[x][x] = 1

        for len in xrange(1, n + 1):
            for x in xrange(1, n + 1 - (len - 1)):
                for i in xrange(x, x + len):
                    dpTable[x][x + len] += dpTable[x][i] * dpTable[i + 1][x + len]

        return dpTable[1][n + 1]