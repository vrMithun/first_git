class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target=len(nums)-1
        curr=target-1
        if len(nums)==1:
            return True
        while curr>=0:
            dist=target-curr
            if dist<=nums[curr]:
                if curr==0:
                    return True
                target=curr
            curr-=1
        return False
        

            
        