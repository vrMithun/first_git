class Solution(object):
    def isPalindrome(self, s):
        lst=[]
        s=s.lower()
        for i in s:
            if i.isalnum():
                lst.append(i)
        lst2=lst[::-1]        
        if lst==lst2:
            return True
        return False           
        