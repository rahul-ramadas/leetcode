class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        if k == 0:
            return
        
        self.rotate_sublist(nums, 0, n - k)
        self.rotate_sublist(nums, n - k, n)
        self.rotate_sublist(nums, 0, n)

    def rotate_sublist(self, nums, i, j):
        a = i
        b = j - 1
        
        while a < b:
            nums[a], nums[b] = nums[b], nums[a]
            a += 1
            b -= 1
