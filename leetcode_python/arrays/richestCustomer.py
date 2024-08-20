class Solution(object):
    def maximumWealth(self, accounts):
        sum=[]
        count=0
        for i in range(len(accounts)):
            count=0
            for j in range(len(accounts[i])):
                count+=accounts[i][j]
            sum.append(count)
        max=sum[0]    
        for k in sum:
            if max<k:
                max=k
        return max            
        