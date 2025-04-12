class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        print("Sorted input:", nums)
        count = 1
        arr = []
        if len(nums) == 0:
            return 0
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                pass
            elif nums[i + 1] - nums[i] == 1:
                count += 1
            else:
                arr.append(count)
                count = 1
        arr.append(count)
        maxi = arr[0]
        for j in range(len(arr)):
            if maxi < arr[j]:
                maxi = arr[j]
        return maxi

# Instantiate the solution
solution = Solution()

# Test cases
print("Test case 1 (Basic):", solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
# Expected: 4 (sequence: [1, 2, 3, 4])

print("Test case 2 (Duplicates):", solution.longestConsecutive([1, 2, 2, 3]))
# Expected: 3 (sequence: [1, 2, 3])

print("Test case 3 (Empty list):", solution.longestConsecutive([]))
# Expected: 0 (no numbers)

print("Test case 4 (Single element):", solution.longestConsecutive([10]))
# Expected: 1 (sequence: [10])

print("Test case 5 (Already consecutive):", solution.longestConsecutive([1, 2, 3, 4, 5]))
# Expected: 5 (sequence: [1, 2, 3, 4, 5])

print("Test case 6 (Negative numbers):", solution.longestConsecutive([-1, 0, 1]))
# Expected: 3 (sequence: [-1, 0, 1])

print("Test case 7 (Gaps in sequence):", solution.longestConsecutive([1, 3, 5, 2, 4]))
# Expected: 5 (sequence: [1, 2, 3, 4, 5])

print("Test case 8 (Unordered list):", solution.longestConsecutive([10, 5, 6, 1, 2, 3]))
# Expected: 4 (sequence: [1, 2, 3, 4])

print("Test case 9 (Multiple sequences):", solution.longestConsecutive([1, 2, 9, 10, 11, 3, 4]))
# Expected: 4 (sequence: [1, 2, 3, 4])

print("Test case 10 (Large gap):", solution.longestConsecutive([1, 100]))
# Expected: 1 (sequence: [1] or [100])
