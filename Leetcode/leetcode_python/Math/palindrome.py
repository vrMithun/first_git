class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            x=str(x)
            l1=list(x)
            new_lst = l1[::-1]
            print(new_lst)
            print(l1)
            if l1==new_lst:
                return True
            else:   
                return False 

        