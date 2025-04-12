n=int(input('Enter number of inputs: '))
l=[]
l1=[]
for i in range(n):
    entry=str(input('enter subject: '))
    l.append(entry)
'''test=0
l1=[]
for j in range(n):
    count=0
    for k in l[test]:
        count+=1
    l1.append(count)
    test=test+1
print(l1)'''
def length(l,s):
    a=len(l[s-1])
    l1.append(a)
    if s==1:
        return 0
    
    else:
        return length(l,s-1)
length(l,n)
print(l1[::-1])
        
        
    
