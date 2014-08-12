class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        def do_row_major():
            dp = [0] * (n + 1)
            dp[1] = 1
            for i in xrange(m):
                for j in xrange(n):
                    if obstacleGrid[i][j] == 1:
                        dp[j + 1] = 0
                    else:
                        dp[j + 1] += dp[j]
            return dp[n]

        def do_col_major():
            dp = [0] * (m + 1)
            dp[1] = 1
            for j in xrange(n):
                for i in xrange(m):
                    if obstacleGrid[i][j] == 1:
                        dp[i + 1] = 0
                    else:
                        dp[i + 1] += dp[i]
            return dp[m]

        if m > n:
            return do_row_major()
        else:
            return do_col_major()
