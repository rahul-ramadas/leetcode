class Solution(object):

    def moveZeroes(self, nums):
        num_zeroes = 0
        move_to = 0
        for move_from in xrange(0, len(nums)):
            if nums[move_from] == 0:
                num_zeroes += 1
            else:
                nums[move_to] = nums[move_from]
                move_to += 1

        nums[move_to:] = [0] * num_zeroes
