class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result=0
        def division(n,result):
            if n==1:
                return (result+1)
            result+=n%2
            return division(n//2,result)
        return division(n,result)
        
        