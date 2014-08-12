class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        sellHere = [0] * len(prices)
        buyHere = [0] * len(prices)

        minPrice = prices[0]
        for i in xrange(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            sellHere[i] = max(sellHere[i - 1], prices[i] - minPrice)

        maxPrice = prices[-1]
        for i in xrange(len(prices) - 2, -1, -1):
            maxPrice = max(maxPrice, prices[i])
            buyHere[i] = max(buyHere[i + 1], maxPrice - prices[i])

        maxProfit = 0
        for i in xrange(0, len(prices)):
            maxProfit = max(maxProfit, sellHere[i] + buyHere[i])

        return maxProfit
