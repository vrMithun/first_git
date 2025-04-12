# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        mid=slow
        current=mid.next
        prev=None
        while current:
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt
        current=prev    
        n=head
        while current:
            temp=n.next
            temp2=current.next
            n.next=current
            current.next=temp
            current=temp2
            n=n.next.next
        mid.next=None    
        return head    
        