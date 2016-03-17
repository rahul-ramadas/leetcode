class Solution:
    
    def minPatches(self, nums, n):
        next_missing_sum = 1
        i = 0
        patched = 0
        while next_missing_sum <= n:
            if i < len(nums) and nums[i] <= next_missing_sum:
                next_missing_sum += nums[i]
                i += 1
            else:
                patched += 1
                next_missing_sum += next_missing_sum
        
        return patched
