class Solution(object):
    def isValid(self, s):
            if len(s)%2!=0:
                return False
            else:
                lst=[]
                lst2=[]
                mydict={'(':')','{':'}','[':']'}
                i=0 
                j=0   
                while j<len(s):
                    if s[j]=='(' or s[j]=='[' or s[j]=='{':
                        lst.append(s[j])
                        i+=1
                    else:
                        lst2.append(s[i])
                        if len(lst)==0:
                            return False
                        if mydict[lst[i-1]]==s[j]:
                            lst.pop()
                            lst2.pop()
                            i-=1
                    j+=1
                if len(lst)!=0 or len(lst2)!=0:             
                    return False
                else:
                    return True               
