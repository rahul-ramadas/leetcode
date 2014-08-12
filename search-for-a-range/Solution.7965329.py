class Solution:

    def searchRange(self, A, target):
        left = bisect.bisect_left(A, target)
        if left == len(A) or A[left] != target:
            return [-1, -1]

        right = bisect.bisect_right(A, target)
        return [left, right - 1]
