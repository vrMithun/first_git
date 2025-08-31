class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        myStack=[]
        mydict={')':'(','}':'{',']':'['}
        for i in s:
            if myStack==[]:
                myStack.append(i)
            elif i in mydict and myStack[-1]==mydict[i]:
                myStack.pop()
            else:
                myStack.append(i)
        if len(myStack)>0:
            return False
        return True