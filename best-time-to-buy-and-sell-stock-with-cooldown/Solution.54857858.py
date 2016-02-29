class Solution:

    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        prev_prev_sell = 0
        prev_buy = -prices[0]
        prev_sell = 0

        for i in xrange(1, len(prices)):
            buy = max(prev_prev_sell - prices[i], prev_buy)
            sell = max(prev_buy + prices[i], prev_sell)
            prev_buy = buy
            prev_prev_sell = prev_sell
            prev_sell = sell

        return sell
