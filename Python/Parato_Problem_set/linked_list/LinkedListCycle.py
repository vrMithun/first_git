class Solution(object):
    def hasCycle(self, head):
        n=head
        if n==None or n.next==None:
            return False
        while n:
            if n.next==None:
                return False
            elif n.next.val=='a':
                return True
            n.val='a'    
            n=n.next    
        return False
    
# Test Cases

# 1. Empty List
# Input: None
# Output: False

# 2. Single Node without Cycle
# Input: [1]
# Output: False

# 3. Single Node with Cycle
# Input: [1] (node points to itself)
# Output: True

# 4. Multiple Nodes without Cycle
# Input: [1 -> 2 -> 3 -> 4 -> None]
# Output: False

# 5. Multiple Nodes with Cycle (cycle at the beginning)
# Input: [1 -> 2 -> 3 -> 4 -> back to 1]
# Output: True

# 6. Multiple Nodes with Cycle (cycle in the middle)
# Input: [1 -> 2 -> 3 -> 4 -> back to 2]
# Output: True

# 7. Long List without Cycle
# Input: [1 -> 2 -> 3 -> ... -> 1000 -> None]
# Output: False

# 8. Long List with Cycle
# Input: [1 -> 2 -> 3 -> ... -> 1000 -> back to 500]
# Output: True

# 9. List with Repeating Values but No Cycle
# Input: [1 -> 2 -> 1 -> 2 -> None]
# Output: False

# 10. Complex List with Cycle (arbitrary structure with a loop)
# Input: [1 -> 2 -> 3 -> 4 -> 5 -> back to 3]
# Output: True
