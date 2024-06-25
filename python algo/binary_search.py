'''n=int(input())'''
l=[23,12,11,65,43]
'''for i in range(0,n):
    a=int(input("Enter any number: "))
    l.append(a)'''
t=int(input())    
l.sort()
j=0
index=len(l)-1
high=index
low=0
while j<=index+1:
    mid=(high+low)//2
    if l[mid]==t:
        print(mid)
        break
    elif t>l[mid]:
        low=mid-1
        j=j+1
    else:
        high=mid    
        j=j+1