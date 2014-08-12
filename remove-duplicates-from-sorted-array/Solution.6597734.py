class Solution:
    def removeDuplicates(self, A):
        if not A:
            return 0

        j = 0
        for i in xrange(1, len(A)):
            if A[i] != A[j]:
                j += 1
                A[j] = A[i]
        return j + 1
