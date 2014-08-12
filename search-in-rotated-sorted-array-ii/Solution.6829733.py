class Solution:

    def search(self, A, target, lower=None, upper=None):
        if lower is None:
            lower = 0
        if upper is None:
            upper = len(A)
        while lower < upper:
            middle = (upper + lower) / 2
            if A[middle] == target:
                return True
            elif A[lower] < A[middle]:
                if A[lower] <= target and A[middle] > target:
                    upper = middle
                else:
                    lower = middle + 1
            elif A[upper - 1] > A[middle]:
                if A[upper - 1] >= target and A[middle] < target:
                    lower = middle + 1
                else:
                    upper = middle
            else:
                return self.search(A, target, lower, middle) or \
                    self.search(A, target, middle + 1, upper)

        return False
