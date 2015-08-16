class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if not num:
            return 0
            
        n = len(num)
        dp = [0] * (n + 1)
        dp[n] = 0
        dp[n - 1] = num[n - 1]
        
        for i in xrange(n - 2, -1, -1):
            dp[i] = max(num[i] + dp[i + 2], dp[i + 1])
            
        return dp[0]
