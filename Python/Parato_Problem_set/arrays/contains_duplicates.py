class Solution(object):
    def containsDuplicate(self, nums):
        nums_set = set(nums)
        if len(nums) != len(nums_set):
            return True
        else:
            return False

# Main method with various test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print("Test case 1 (No duplicates):", solution.containsDuplicate([1, 2, 3, 4]))  # Expected: False
    print("Test case 2 (Has duplicates):", solution.containsDuplicate([1, 2, 2, 3]))  # Expected: True
    print("Test case 3 (Single element):", solution.containsDuplicate([1]))  # Expected: False
    print("Test case 4 (Empty list):", solution.containsDuplicate([]))  # Expected: False
    print("Test case 5 (All duplicates):", solution.containsDuplicate([7, 7, 7, 7]))  # Expected: True
    print("Test case 6 (Large input with no duplicates):", solution.containsDuplicate(list(range(1000000))))  # Expected: False
    print("Test case 7 (Large input with duplicates):", solution.containsDuplicate(list(range(100000)) + [99999]))  # Expected: True
    print("Test case 8 (Negative numbers, no duplicates):", solution.containsDuplicate([-1, -2, -3, -4]))  # Expected: False
    print("Test case 9 (Negative numbers, with duplicates):", solution.containsDuplicate([-1, -2, -2, -4]))  # Expected: True
    print("Test case 10 (Mixed positive and negative, no duplicates):", solution.containsDuplicate([-1, 1, 2, -2]))  # Expected: False
    print("Test case 11 (Mixed positive and negative, with duplicates):", solution.containsDuplicate([-1, 1, -1, 2]))  # Expected: True
    print("Test case 12 (Zeros only):", solution.containsDuplicate([0, 0, 0, 0]))  # Expected: True
    print("Test case 13 (Zeros and other numbers):", solution.containsDuplicate([0, 1, 2, 3]))  # Expected: False
