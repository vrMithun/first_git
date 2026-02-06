class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        
        result = 0
        buy = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]  
            else:
                profit = prices[i] - buy
                result = max(result, profit)
        
        return result
