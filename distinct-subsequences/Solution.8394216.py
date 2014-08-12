class Solution:

    def numDistinct(self, S, T):
        m = len(S)
        n = len(T)

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in xrange(1, m + 1):
            for j in xrange(n, 0, -1):
                if S[i - 1] == T[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]
