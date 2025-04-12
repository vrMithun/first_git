# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        result=ListNode()
        head=result
        while list1 and list2:
            if list1.val>list2.val:
                result.next=list2
                list2=list2.next
            else:
                result.next=list1
                list1=list1.next
            result=result.next
        if list1:
            result.next=list1
        else:
            result.next=list2        
        return head.next   

# Test Cases

# 1. Both lists are empty
# Input: list1 = None, list2 = None
# Output: None

# 2. One list is empty, the other has elements
# Input: list1 = [1, 2, 3], list2 = None
# Output: [1, 2, 3]

# Input: list1 = None, list2 = [1, 2, 3]
# Output: [1, 2, 3]

# 3. Both lists have one element
# Input: list1 = [1], list2 = [2]
# Output: [1, 2]

# Input: list1 = [2], list2 = [1]
# Output: [1, 2]

# 4. Both lists have multiple elements, no overlap in values
# Input: list1 = [1, 3, 5], list2 = [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]

# 5. Both lists have overlapping values
# Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]

# 6. One list is a subset of the other
# Input: list1 = [1, 2, 3, 4], list2 = [2, 3]
# Output: [1, 2, 2, 3, 3, 4]

# 7. Both lists are identical
# Input: list1 = [1, 2, 3], list2 = [1, 2, 3]
# Output: [1, 1, 2, 2, 3, 3]

# 8. Lists with negative values
# Input: list1 = [-3, -1, 2], list2 = [-2, 0, 3]
# Output: [-3, -2, -1, 0, 2, 3]

# 9. One list is much longer than the other
# Input: list1 = [1, 2, 3], list2 = [4, 5, 6, 7, 8]
# Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Input: list1 = [1, 2, 3, 4, 5], list2 = [6]
# Output: [1, 2, 3, 4, 5, 6]

# 10. Large input lists (test for performance)
# Input: list1 = [1, 3, 5, ..., 9999], list2 = [2, 4, 6, ..., 10000]
# Output: [1, 2, 3, 4, 5, ..., 10000]

                
        