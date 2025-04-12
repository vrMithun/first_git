def gcdOfStrings(str1, str2):
    result=""
    if str1[0]!=str2[0]:
        return ""
    else:
        test=0
        for i in range(len(str1)-1):
            if str1[0]==str1[i+1]:
                test+=1
                break
        if test==1:
            a=len(str1)/(i+1)
            b=len(str2)/(i+1)
            if a>b:
                for j in range(b):
                    result+=b[j]
            else:
                for j in range(a):
                    result+=a[j]         
        else:
            print(len(str1))    
gcdOfStrings("abc","abc")        