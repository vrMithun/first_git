class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==1:
            return 0
        left=0
        right=1
        profit=0
        result=0
        while right<len(prices):
            if prices[left]<prices[right]:
                profit+=prices[right]-prices[left]
            
            right+=1
            left+=1
        return profit