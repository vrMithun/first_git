'''class Solution(object):
    def twoSum(self, nums, target):
        lst=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                        lst.append(i)
                        lst.append(j)
        return lst
'''

# two sum updated using hash map

class Solution(object):
    def twoSum(self, nums, target):
        myhash={}
        for i in range(len(nums)):
            if (target-nums[i]) in myhash:
                return [i,myhash[target-nums[i]]]
            myhash[nums[i]]=i
