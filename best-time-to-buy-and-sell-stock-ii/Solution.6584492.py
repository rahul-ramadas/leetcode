class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        priceIter = iter(prices)
        buyPrice = next(priceIter)
        profit = 0
        for price in priceIter:
            if price > buyPrice:
                profit += price - buyPrice
            buyPrice = price
        return profit