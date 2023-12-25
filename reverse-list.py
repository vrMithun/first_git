n=int(input('Enter number of inputs: '))
l=[]
for i in range(0,n):
    l.append(int(input()))
print(l) 
for j in range(0,n):
     l.insert(j,l[n-1])  
     l.pop(n)  
print(l)
