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