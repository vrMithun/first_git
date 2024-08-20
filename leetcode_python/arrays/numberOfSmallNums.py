class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        lst=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            lst.append(count)
        return lst            

        