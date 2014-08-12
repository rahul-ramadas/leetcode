class Solution:

    def search(self, A, target):
        lower = 0
        upper = len(A)
        while lower < upper:
            middle = (upper + lower) / 2
            if A[middle] == target:
                return middle
            elif A[middle] > target and A[lower] <= target:
                upper = middle
            elif A[middle] > target and A[lower] > A[middle]:
                upper = middle
            elif A[middle] > target and A[lower] > target:
                lower = middle + 1
            elif A[middle] < target and A[upper - 1] >= target:
                lower = middle + 1
            elif A[middle] < target and A[upper - 1] < A[middle]:
                lower = middle + 1
            elif A[middle] < target and A[upper - 1] < target:
                upper = middle
            else:
                raise Exception()

        return -1
