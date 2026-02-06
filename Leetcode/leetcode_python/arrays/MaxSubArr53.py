class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=nums[0]
        for i in range(1,len(nums)):
            nums[i]=max(nums[i],nums[i]+nums[i-1])
            result=max(nums[i],result)
        return result
            

        