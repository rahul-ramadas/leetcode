class Solution:

    def find_left(self, A, target):
        lo = 0
        hi = len(A)

        while lo < hi:
            mid = (lo + hi) / 2

            if A[mid] >= target:
                hi = mid
            else:
                lo = mid + 1

        if lo == len(A) or A[lo] != target:
            return -1
        return lo

    def find_right(self, A, target):
        lo = 0
        hi = len(A)

        while lo < hi:
            mid = (lo + hi) / 2

            if A[mid] > target:
                hi = mid
            else:
                lo = mid + 1

        if lo == 0 or A[lo - 1] != target:
            return -1
        return lo - 1

    def searchRange(self, A, target):
        return [self.find_left(A, target), self.find_right(A, target)]
