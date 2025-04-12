class Solution(object):
    def minimumOperations(self, nums):
        test=0
        for i in range(len(nums)):
            if nums[i]%3==0:
                pass
            else:
                if (nums[i]-1)%3==0 or (nums[i]+1)%3==0:
                    test+=1
        return test       
