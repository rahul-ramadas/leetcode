class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        begin = 0
        end = 0
        min_length = len(nums) + 1
        trial_sum = 0
        
        while True:
            if trial_sum < s:
                if end == len(nums):
                    break
                trial_sum += nums[end]
                end += 1
            else:
                trial_sum -= nums[begin]
                begin += 1
                
            if trial_sum >= s:
                min_length = min(min_length, end - begin)
                
        if min_length > len(nums):
            return 0
        return min_length
