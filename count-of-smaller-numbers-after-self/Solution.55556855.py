class Solution:

    def countSmaller(self, nums):
        smaller = [0] * len(nums)
        self.sort(list(enumerate(nums)), smaller)
        return smaller

    def sort(self, nums, smaller):
        n = len(nums)
        if n <= 1:
            return

        mid = n / 2
        left = nums[:mid]
        right = nums[mid:]
        self.sort(left, smaller)
        self.sort(right, smaller)

        left_ind = 0
        right_ind = 0
        for i in xrange(len(nums)):
            if (left_ind < len(left) and (right_ind == len(right) or left[left_ind][1] <= right[right_ind][1])):
                smaller[left[left_ind][0]] += right_ind
                nums[i] = left[left_ind]
                left_ind += 1
            else:
                nums[i] = right[right_ind]
                right_ind += 1
