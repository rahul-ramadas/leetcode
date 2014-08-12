class Solution:

    def canJump(self, A):
        if len(A) <= 1:
            return True

        minimum_distance = 1

        for i in xrange(len(A) - 2, 0, -1):
            if A[i] >= minimum_distance:
                minimum_distance = 1
            else:
                minimum_distance += 1

        return A[0] >= minimum_distance
