class Solution(object):
    def maxDepth(self, s):
        count=0
        max=0
        for i in s:
            if i=="(":
                count+=1
                if max<count:
                    max=count
            elif i==")": 
                count-=1
        return max        
        