class Solution(object):
    def isAnagram(self, s, t):
        set1 = set(s)
        if len(s) == len(t):
            for i in set1:
                if s.count(i) != t.count(i):
                    return False
            return True
        return False

# Instantiate the solution
solution = Solution()

# Test cases
print("Test case 1 (Basic anagram):", end=" ")
arr1_1, arr1_2 = "anagram", "nagaram"
print(solution.isAnagram(arr1_1, arr1_2))
# Expected: True (Both are anagrams)

print("Test case 2 (Not an anagram):", end=" ")
arr2_1, arr2_2 = "rat", "car"
print(solution.isAnagram(arr2_1, arr2_2))
# Expected: False (Not an anagram)

print("Test case 3 (Different lengths):", end=" ")
arr3_1, arr3_2 = "hello", "helloo"
print(solution.isAnagram(arr3_1, arr3_2))
# Expected: False (Different lengths)

print("Test case 4 (Empty strings):", end=" ")
arr4_1, arr4_2 = "", ""
print(solution.isAnagram(arr4_1, arr4_2))
# Expected: True (Two empty strings are anagrams)

print("Test case 5 (Same characters, different order):", end=" ")
arr5_1, arr5_2 = "aabbcc", "bbccaa"
print(solution.isAnagram(arr5_1, arr5_2))
# Expected: True (Both are anagrams)

print("Test case 6 (Different characters):", end=" ")
arr6_1, arr6_2 = "abc", "def"
print(solution.isAnagram(arr6_1, arr6_2))
# Expected: False (Different characters)

print("Test case 7 (Single character):", end=" ")
arr7_1, arr7_2 = "a", "a"
print(solution.isAnagram(arr7_1, arr7_2))
# Expected: True (Both are the same)

print("Test case 8 (Single character, different):", end=" ")
arr8_1, arr8_2 = "a", "b"
print(solution.isAnagram(arr8_1, arr8_2))
# Expected: False (Different characters)

print("Test case 9 (With spaces):", end=" ")
arr9_1, arr9_2 = "hello world", "world hello"
print(solution.isAnagram(arr9_1, arr9_2))
# Expected: True (Both are anagrams, considering spaces)

print("Test case 10 (Uppercase and lowercase):", end=" ")
arr10_1, arr10_2 = "Listen", "Silent"
print(solution.isAnagram(arr10_1, arr10_2))
# Expected: False (Case-sensitive check, not anagrams)
