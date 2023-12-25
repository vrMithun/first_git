n=str(input("Enter any word: "))
l=[]
for i in str(n):
    l.append(i)
print(l)
s=set(l)
for j in range(0,len(l)):
    for k in range(0,len(s)):
        if s[k]==l[j] and j<len(s):
            x=x+1
    print(x)        


