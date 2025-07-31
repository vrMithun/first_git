class Solution(object):
    def twoSum(self, nums, target):
        lst = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    lst.append(i)
                    lst.append(j)
        return lst

# Instantiate the solution
solution = Solution()

# Test cases
print("Test case 1 (Basic case):", end=" ")
arr1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(arr1, target1))
# Expected: [0, 1] (Because nums[0] + nums[1] = 9)

print("Test case 2 (No solution):", end=" ")
arr2 = [1, 2, 3, 4]
target2 = 10
print(solution.twoSum(arr2, target2))
# Expected: [] (No two numbers add up to 10)

print("Test case 3 (Multiple pairs):", end=" ")
arr3 = [1, 3, 2, 3]
target3 = 6
print(solution.twoSum(arr3, target3))
# Expected: [1, 3] (Because nums[1] + nums[3] = 6)

print("Test case 4 (Same number multiple times):", end=" ")
arr4 = [3, 3, 3, 3]
target4 = 6
print(solution.twoSum(arr4, target4))
# Expected: [0, 1] (nums[0] + nums[1] = 6)

print("Test case 5 (Negative numbers):", end=" ")
arr5 = [-1, -2, -3, -4]
target5 = -6
print(solution.twoSum(arr5, target5))
# Expected: [2, 3] (Because nums[2] + nums[3] = -6)

print("Test case 6 (Single solution):", end=" ")
arr6 = [1, 2, 3, 4, 5]
target6 = 7
print(solution.twoSum(arr6, target6))
# Expected: [1, 5] (Because nums[1] + nums[5] = 7)

print("Test case 7 (Empty list):", end=" ")
arr7 = []
target7 = 5
print(solution.twoSum(arr7, target7))
# Expected: [] (Empty list, no pairs)

print("Test case 8 (Large numbers):", end=" ")
arr8 = [100000, 500000, 200000, 700000]
target8 = 700000
print(solution.twoSum(arr8, target8))
# Expected: [0, 2] (Because nums[0] + nums[2] = 700000)

print("Test case 9 (No two elements add up to target):", end=" ")
arr9 = [2, 4, 6, 8]
target9 = 15
print(solution.twoSum(arr9, target9))
# Expected: [] (No two elements add up to 15)

print("Test case 10 (Target is 0):", end=" ")
arr10 = [0, 0, 0, 0]
target10 = 0
print(solution.twoSum(arr10, target10))
# Expected: [0, 1] (Because nums[0] + nums[1] = 0)
