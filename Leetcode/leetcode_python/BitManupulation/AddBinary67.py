class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry=0
        ptr1=len(a)-1
        ptr2=len(b)-1
        def add(a,b,c):
            if a=="1" and b=="1":
                if c=="1":
                    return ("1","1")
                return ("0","1")
            elif (a=="1" and b=="0") or (a=="0" and b=="1"):
                if c=="1":
                    return ("0","1")
                return ("1","0")
            else:
                if c=="1":
                    return ("1","0")
                return ("0","0")

        def func(ptr1,ptr2,a,b,c):
            if ptr1<0 and ptr2<0:
                if c=="1":
                    return c
                return ""
            if ptr1<0:
                res,c=add("0",b[ptr2],c)
                return (func(ptr1,ptr2-1,a,b,c)+res)
            if ptr2<0:
                res,c=add(a[ptr1],"0",c)
                return (func(ptr1-1,ptr2,a,b,c)+res)
            res,c=add(a[ptr1],b[ptr2],c)
            return func(ptr1-1,ptr2-1,a,b,c)+res         
        return func(ptr1,ptr2,a,b,carry)
        