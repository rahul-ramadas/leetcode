class Solution:

    def maxCoins(self, nums):
        n = len(nums)

        # First index is starting position of sub-sequence.
        # Second index is length of the sub-sequence.
        # dp[i][l] = maxCoins obtainable for sub-sequence of balloons [i, i + l)
        dp = [[0] * (n + 1 - i) for i in xrange(n + 1)]

        # Bottom-up construction for all possible sub-sequences.
        for l in xrange(1, n + 1):
            for i in xrange(n + 1 - l):
                # For this sub-sequence, search for the selection of the last balloon that must be
                # burst that yields the best solution.
                best = 0
                for j in xrange(i, i + l):
                    left_end = nums[i - 1] if i > 0 else 1
                    right_end = nums[i + l] if i + l < n else 1
                    left_best = dp[i][j - i]
                    right_best = dp[j + 1][i + l - (j + 1)]
                    best = max(best, left_best + (left_end * nums[j] * right_end) + right_best)
                dp[i][l] = best

        return dp[0][n]
