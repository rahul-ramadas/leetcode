class Solution:
    """O(nlogn) solution with some corrections to remove unnecessary checks."""

    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * (n + 1)
        max_len = 0

        for i in xrange(n):
            cur = nums[i]
            prev_len = self.binary_search_len(dp, max_len, cur)
            new_len = prev_len + 1
            dp[new_len] = cur
            max_len = max(max_len, new_len)

        return max_len

    def binary_search_len(self, dp, max_len, cur):
        start = 0
        end = max_len + 1
        while end - start > 1:
            mid = (start + end) / 2
            if dp[mid] < cur:
                start = mid
            else:
                end = mid

        return start
