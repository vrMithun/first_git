class Solution(object):
    def productExceptSelf(self, nums):
        arr1=[1]*len(nums)
        arr2=[1]*len(nums)
        result=[]
        for i in range(1,len(nums)):
            arr1[i]=arr1[i-1]*nums[i-1]
        for j in range(len(nums)-2,-1,-1):  
            arr2[j]=arr2[j+1]*nums[j+1]
       
        for k in range(len(nums)):
            product=arr1[k]*arr2[k]
            result.append(product)
        return result    