class Solution(object):
    def getConcatenation(self, nums):
        length=len(nums)
        ans=[0]*(2*length)
        for i in range(0,length):
            ans[i]=nums[i]
            ans[i+length]=nums[i] 
        return ans 
        