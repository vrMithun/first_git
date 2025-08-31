n,m,k=map(int,input().split())
l2=[]
for i in range(m):
    l1=[]
    a,b,f=list(map(int,input().split()))
    l1.append(a)
    l1.append(b)
    l1.append(f)
    l2.append(l1)
j=n
t=0
while j>0:
    t=t+j-1
    j=j-1
print(t)    
q=t**k
print(q)
l=[]
for k in range(1,n+1):
    l.append(k)
print(l)   
print(l2)

    