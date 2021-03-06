class Solution:
    """O(nlogn) solution that uses language facilities for binary search."""

    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * (n + 1)
        max_len = 0

        for i in xrange(n):
            cur = nums[i]
            new_len = self.binary_search_len(dp, max_len, cur)
            dp[new_len] = cur
            max_len = max(max_len, new_len)

        return max_len

    def binary_search_len(self, dp, max_len, cur):
        return bisect.bisect_left(dp, cur, lo=1, hi=max_len + 1)
