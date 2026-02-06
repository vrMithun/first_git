class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=prices[0]
        result=0
        for i in range(1,len(prices)):
            if buy>prices[i]:
                buy=prices[i]
            else:
                result=max(result,prices[i]-buy)
        return result