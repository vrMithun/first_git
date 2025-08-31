s=str(input("Enter any word: "))
c=1
i=0
while i<len(s)-1:
    if s[i]==s[i+1] :
        c=c+1
    elif s[i]!=s[i+1]:
        print(c,end='')  
        print(s[i],end='')
        c=1
    i=i+1  
if s[i]==s[i-1]: 
    print(c,end='')  
    print(s[i],end='')   
else:
    print(1,end='')
    print(s[i])

