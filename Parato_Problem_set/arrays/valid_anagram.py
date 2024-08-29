class Solution(object):
    def isAnagram(self, s, t):
        set1=set(s)
        if len(s)==len(t):
            for i in set1:
                if s.count(i)!=t.count(i):
                    return False
            return True
        return False                   