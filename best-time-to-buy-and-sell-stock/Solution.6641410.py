class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        maxProfit = 0
        maxPrice = 0
        
        for p in reversed(prices):
            maxPrice = max(maxPrice, p)
            maxProfit = max(maxProfit, maxPrice - p)
            
        return maxProfit
