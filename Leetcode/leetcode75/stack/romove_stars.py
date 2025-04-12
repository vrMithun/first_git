def removeStars(s):
    lst=[]
    str1=""
    for i in range(len(s)):
        if s[i]=='*':
            lst.pop(i-1)
        else:
            lst.append(s[i])
    for j in range(len(lst)):
        str1=str1+lst[j]
    return str1    
print(removeStars("leet*cod*e*"))