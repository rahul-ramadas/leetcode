class Solution:

    def firstMissingPositive(self, A):

        for i in xrange(len(A)):
            num = A[i]
            while num > 0 and num <= len(A) and A[num - 1] != num:
                temp = A[num - 1]
                A[num - 1] = num
                num = temp

        for i in xrange(len(A)):
            if A[i] != i + 1:
                return i + 1

        return len(A) + 1
