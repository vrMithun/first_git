class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        point1=0
        point2=0
        mergelist=[]
        while point1<len(nums1) and point2<len(nums2):
            if nums1[point1]>=nums2[point2]:
                mergelist.append(nums2[point2])
                point2+=1
            else :
                mergelist.append(nums1[point1])
                point1+=1
        
        mergelist.extend(nums1[point1:])
        mergelist.extend(nums2[point2:])
        median=len(mergelist)//2
        print(mergelist)
        if len(mergelist)%2==0:
            return ((mergelist[median]+mergelist[median-1])/2.0)
        return (mergelist[median])

        