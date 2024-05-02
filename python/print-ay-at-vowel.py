n=str(input("Enter any word:"))
x=['a','e','i','o','u']
l=[]
k=0
for i in str(n):
    l.append(i)
print(l)
a=l[0]
print(x[0])   
for j in range(0,5):
    if x[j]==l[0]:
        print(n,end='')
        print('hay')
        k=k+1
print(k)         
if k==0:
    l.pop(0)
    l.append(a)
    for i in range (0,len(l)):
        print(l[i],end='')
print('ay')