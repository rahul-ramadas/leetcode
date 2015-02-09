class Solution:

    def calculateMinimumHP(self, dungeon):
        if dungeon is None or not dungeon or not dungeon[0]:
            return 0

        M = len(dungeon)
        N = len(dungeon[0])
        dp = [0] * N

        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if j < (N - 1):
                    min_right = dp[j + 1]
                else:
                    min_right = float("inf")

                if i < (M - 1):
                    min_down = dp[j]
                else:
                    min_down = float("inf")

                min_dir = 1 if min_down == min_right == float("inf") else min(min_down, min_right)
                dp[j] = max(1, dungeon[i][j] * -1 + min_dir)

        return dp[0]
