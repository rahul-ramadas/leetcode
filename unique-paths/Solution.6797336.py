class Solution:
    def uniquePaths(self, m, n):
        dp = [[0] * n for i in xrange(m)]
        dp[m - 1][n - 1] = 1
        process = collections.deque([(m - 1, n - 1)])

        while process:
            i, j = process.popleft()

            if j < n - 1:
                a = dp[i][j + 1]
            else:
                a = 0

            if i < m - 1:
                b = dp[i + 1][j]
            else:
                b = 0

            dp[i][j] = max(a + b, 1)

            if i > 0 and dp[i - 1][j] != -1:
                dp[i - 1][j] = -1
                process.append((i - 1, j))

            if j > 0 and dp[i][j - 1] != -1:
                dp[i][j - 1] = -1
                process.append((i, j - 1))

        return dp[0][0]
