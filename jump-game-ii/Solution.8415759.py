class Solution:

    def jump(self, A):

        if len(A) == 1:
            return 0

        steps = 0
        farthest = 0
        next_farthest = 0

        for current in xrange(len(A)):

            if current > farthest:
                farthest = next_farthest
                steps += 1

            next_farthest = max(next_farthest, current + A[current])

            if next_farthest >= (len(A) - 1):
                return steps + 1

        return -1
