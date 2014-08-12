class Solution:

    def jump(self, A):

        steps = 0
        farthest = 0
        next_farthest = 0

        for current in xrange(len(A)):

            if current > farthest:
                farthest = next_farthest
                steps += 1

            next_farthest = max(next_farthest, current + A[current])

        return steps
