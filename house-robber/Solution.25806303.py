class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if not num:
            return 0
            
        n = len(num)
        even = 0
        odd = 0

        for i in xrange(n):
            if i % 2:
                odd = max(num[i] + odd, even)
            else:
                even = max(num[i] + even, odd)

        return max(odd, even)
