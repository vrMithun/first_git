# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length=0
        test=head
        while test:
            test=test.next
            length+=1
        if length==n:
            temp=head.next
            del head
            head=temp
            return head  
        remove=length-n
        test=head   
        for _ in range(remove-1):
            test=test.next
        temp=test.next.next
        del test.next
        test.next=temp
        return head
