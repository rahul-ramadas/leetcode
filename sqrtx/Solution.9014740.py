class Solution:

    def sqrt(self, x):
        low = 0
        high = 65536
        best = 0

        while high > low:

            mid = (high + low) / 2
            sqr = mid ** 2
            if sqr > x:
                high = mid
            elif sqr == x:
                return mid
            else:
                best = mid
                low = mid + 1

        return best
