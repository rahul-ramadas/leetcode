class Solution:
    def searchInsert(self, A, target):
        return bisect.bisect_left(A, target)
