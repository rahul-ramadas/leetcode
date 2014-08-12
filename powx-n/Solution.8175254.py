class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        base = x
        p = abs(n)
        
        result = 1
        while p > 0:
            if p % 2 == 0:
                base *= base
                p /= 2
            else:
                result *= base
                p -= 1
                
        if n < 0:
            result = 1.0 / result
        return result
