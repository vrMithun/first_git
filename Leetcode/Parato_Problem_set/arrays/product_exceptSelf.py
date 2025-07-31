class Solution(object):
    def productExceptSelf(self, nums):
        arr1 = [1] * len(nums)
        arr2 = [1] * len(nums)
        result = []
        
        for i in range(1, len(nums)):
            arr1[i] = arr1[i - 1] * nums[i - 1]
        
        for j in range(len(nums) - 2, -1, -1):  
            arr2[j] = arr2[j + 1] * nums[j + 1]
       
        for k in range(len(nums)):
            product = arr1[k] * arr2[k]
            result.append(product)
        
        return result

# Instantiate the solution
solution = Solution()

# Test cases
print("Test case 1 (Basic):", solution.productExceptSelf([1, 2, 3, 4]))
# Expected: [24, 12, 8, 6]

print("Test case 2 (Contains zero):", solution.productExceptSelf([1, 2, 0, 4]))
# Expected: [0, 0, 8, 0]

print("Test case 3 (All zeros):", solution.productExceptSelf([0, 0, 0, 0]))
# Expected: [0, 0, 0, 0]

print("Test case 4 (Single element):", solution.productExceptSelf([5]))
# Expected: [1] (Nothing to multiply)

print("Test case 5 (Negative numbers):", solution.productExceptSelf([-1, 2, -3, 4]))
# Expected: [-24, 12, -8, 6]

print("Test case 6 (Two elements):", solution.productExceptSelf([3, 4]))
# Expected: [4, 3]

print("Test case 7 (Large numbers):", solution.productExceptSelf([100000, 200000, 300000, 400000]))
# Expected: [24000000000000, 12000000000000, 8000000000000, 6000000000000]

print("Test case 8 (Mixed numbers):", solution.productExceptSelf([2, -1, 3, 0, 5]))
# Expected: [0, 0, 0, 30, 0]

print("Test case 9 (All ones):", solution.productExceptSelf([1, 1, 1, 1]))
# Expected: [1, 1, 1, 1]

print("Test case 10 (Alternating signs):", solution.productExceptSelf([-1, 1, -1, 1]))
# Expected: [-1, 1, -1, 1]
