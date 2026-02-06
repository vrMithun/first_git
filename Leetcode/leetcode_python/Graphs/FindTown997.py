class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        left=[0]*(n+1)
        right=[0]*(n+1)
        for i in range(len(trust)):
            x,y=trust[i]
            left[x]+=1
            right[y]+=1

        for i in range(1,n+1):
            if left[i]==0 and right[i]==n-1:
                return i
        return -1
        