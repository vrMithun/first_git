class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        result=0
        while left<right:
            area=0
            if height[left]<height[right]:
                area=(right-left)*height[left]
                left+=1
            else:
                area=(right-left)*height[right]
                right-=1
            result=max(result,area)
        return result
                