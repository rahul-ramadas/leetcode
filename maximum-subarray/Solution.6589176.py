class Solution:
    def maxSubArray(self, A):
        if len(A) == 1:
            return A[0]

        maxEndingHere = A[0]
        maxest = A[0]

        for number in A[1:]:
            maxEndingHere = max(maxEndingHere + number, number)
            maxest = max(maxest, maxEndingHere)

        return maxest
