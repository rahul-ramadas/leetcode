class Solution:
    """O(n^2) solution."""

    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * n

        for i in xrange(n - 1, -1, -1):
            best = 0
            for j in xrange(i + 1, n):
                if nums[j] > nums[i]:
                    best = max(best, dp[j])
            dp[i] = 1 + best

        return max(dp)
