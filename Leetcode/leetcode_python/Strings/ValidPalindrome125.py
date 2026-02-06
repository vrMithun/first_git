class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mystr=""
        for i in s:
            if i.isalnum():
                mystr+=i
        left=0
        right=len(mystr)-1
        print(mystr)
        while left<right:
            if mystr[left].lower()!=mystr[right].lower():
                return False
            left+=1
            right-=1
        return True
        