class Solution:

    def minimumTotal(self, triangle):
        dp = triangle[-1][:]

        for i in xrange(len(triangle) - 2, -1, -1):
            for j in xrange(0, len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]
