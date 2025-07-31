def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product=1
        count=0
        for i in nums:
            if i==0:
                count+=1
        if count>1:
            return [0 for i in nums]
        else:
            for i in nums:
                if i!=0:
                    product*=i
            if 0 in nums:
                return [product if i == 0 else 0 for i in nums]

            else:
                return [product/x for x in nums]