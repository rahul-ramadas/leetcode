class Solution:

    def largestDivisibleSubset(self, nums):
        if not nums:
            return []

        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] != 0:
                    continue

                if dp[j] + 1 > dp[i]:
                    prev[i] = j
                    dp[i] = dp[j] + 1

        largest_size = max(dp)
        index = dp.index(largest_size)
        solution = []
        while index != -1:
            solution.append(nums[index])
            index = prev[index]

        return solution
