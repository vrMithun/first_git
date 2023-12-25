l=[]
l1=[]
l2=[]
l2=[]
x=[]
l=list(map(int,input().split()))
print(l)
def factor(a):
    for i in range(1,a):
        if a%i==0:
            x.append(i)
    return(x)        

for j in l:
    print(factor(j))
    
    
