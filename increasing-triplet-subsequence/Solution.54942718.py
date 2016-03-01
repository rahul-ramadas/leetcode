class Solution:
    """O(n) solution that is simply a special case of the O(nlogn) LIS solution."""

    def increasingTriplet(self, nums):
        n = len(nums)
        if n < 3:
            return False

        dp = [0, 0]
        max_len = 0

        def find_prev_len(num):
            for i in xrange(max_len - 1, -1, -1):
                if dp[i] < num:
                    return i + 1
            return 0

        for num in nums:
            prev_len = find_prev_len(num)
            new_len = prev_len + 1
            if new_len == 3:
                return True
            dp[new_len - 1] = num
            max_len = max(max_len, new_len)

        return False
