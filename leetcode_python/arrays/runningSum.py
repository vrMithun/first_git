class Solution(object):
    def runningSum(self, nums):
        lst=[]
        for i in range(len(nums)): 
            count=0
            for j in range(i+1):
                count+=nums[j]
            lst.append(count)
        return lst    
        