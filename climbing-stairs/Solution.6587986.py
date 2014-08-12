class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        a = 1
        b = 2
        c = 0
        for i in xrange(3, n + 1):
            c = a + b
            a, b = b, c
        return c
