
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        n=head
        digit=1
        result=0
        while n.next!=None:
            digit+=1
            n=n.next
        n=head    
        for i in range(digit-1,-1,-1):
            if n.val==1:
                result+=2**(i)
                print(result, i)
            n=n.next
        return result