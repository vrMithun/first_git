def nextPermutation(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        print(i)
        if i>=0:
            j=len(nums)-1
            while j>=0 and nums[i]>=nums[j]:
                j-=1
            if j>=0:
                nums[i],nums[j]=nums[j],nums[i]
        nums[i+1:]=reversed(nums[i+1:])
        return nums
mylist=[5,1,1]
print(nextPermutation(mylist))