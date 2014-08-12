class Solution:
    def minPathSum(self, grid):
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in xrange(n)]
        process = collections.deque([(0, 0)])
        dp[0][0] = grid[0][0]

        while process:
            i, j = process.popleft()

            if j < m - 1:
                if dp[i][j + 1]:
                    dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + grid[i][j + 1])
                else:
                    dp[i][j + 1] = dp[i][j] + grid[i][j + 1]
                    process.append((i, j + 1))

            if i < n - 1:
                if dp[i + 1][j]:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + grid[i + 1][j])
                else:
                    dp[i + 1][j] = dp[i][j] + grid[i + 1][j]
                    process.append((i + 1, j))

        return dp[n - 1][m - 1]
