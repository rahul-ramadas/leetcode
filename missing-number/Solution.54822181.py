class Solution:

    def missingNumber(self, nums):
        xor_all_in_nums = reduce(operator.xor, nums)
        xor_all = reduce(operator.xor, xrange(len(nums) + 1))
        return xor_all ^ xor_all_in_nums
