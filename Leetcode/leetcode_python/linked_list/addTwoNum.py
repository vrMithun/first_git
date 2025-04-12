# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        self.head=ListNode(None)
        n=self.head
        carry=0
        while l1 or l2:
            if l1 and l2:
                ssum=l1.val+l2.val
                if self.head.val==None:
                    self.head.val=(ssum+carry)%10
                    carry=(ssum+carry)//10
                    print(self.head.val)
                else:
                    newNode=ListNode()
                    newNode.val=(ssum+carry)%10
                    carry=(ssum+carry)//10 
                    n.next=newNode
                    n=n.next
                l1=l1.next
                l2=l2.next
            else:
                if l1:
                    newNode=ListNode()
                    newNode.val=(l1.val+carry)%10
                    carry=(l1.val+carry)//10
                    n.next=newNode
                    n=n.next
                    l1=l1.next
                else:
                    newNode=ListNode()
                    newNode.val=(l2.val+carry)%10
                    carry=(l2.val+carry)//10
                    n.next=newNode
                    n=n.next
                    l2=l2.next 
        if l1==None and l2==None and carry>0:
            newNode=ListNode()
            newNode.val=carry
            n.next=newNode                   
        return self.head                 


        