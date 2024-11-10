class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        print(nums)
        count=1
        arr=[]
        if len(nums)==0:
            return 0
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]:
                pass
            elif nums[i+1]-nums[i]==1:
                count+=1
            else:
                arr.append(count)
                count=1
            print(count)
        arr.append(count)    
        maxi=arr[0]
        for j in range(len(arr)):
            if  maxi<arr[j]:
                maxi=arr[j]   
        return maxi
        