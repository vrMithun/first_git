# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev=None
        current=head
        while current:
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt
        self.head=prev
        return self.head    