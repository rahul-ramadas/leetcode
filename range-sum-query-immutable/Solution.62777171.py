class NumArray(object):
    def __init__(self, nums):
        self.cum_sum = [0] * (len(nums) + 1)
        for i, v in enumerate(nums):
            self.cum_sum[i + 1] = self.cum_sum[i] + v

    def sumRange(self, i, j):
        return self.cum_sum[j + 1] - self.cum_sum[i]
