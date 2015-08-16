class Solution:

    def maxProfit(self, k, prices):
        n = len(prices)

        if k >= n / 2:
            return self.maxProfitMax(k, prices)

        dp = [[0] * (n + 1) for _ in range(2)]

        for i in range(1, k + 1):
            maxOneLess = float("-inf")
            for j in range(1, n + 1):
                dp[i % 2][j] = max(dp[i % 2][j - 1], maxOneLess + prices[j - 1])
                maxOneLess = max(maxOneLess, dp[(i + 1) % 2][j - 1] - prices[j - 1])

        return dp[k % 2][n]

    def maxProfitMax(self, k, prices):
        n = len(prices)
        profit = 0
        for i in range(1, n):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]

        return profit
