'''import os
l=[]
l1=[]
l2=[]
file=open("myfile.txt",'w')
file.write(''' '''welcome to my code
i would like to welcome you'''''')
file.close()
with open('myfile.txt') as file:
    line=file.read()
    l=line.split('\n')
print(l)
for i in l:
    l1=i.split(' ')
    l2.extend(l1)  
print(l2)
os.remove("myfile.txt")
file=open("myfile.txt",'r')
file.read()
file.close()'''

'''import pdb
def addition(a,b):
    return(a+b)
pdb.set_trace()
x=int(input())
y=int(input())
print(addition(x,y))'''

'''l=[1,2,3,4,5,6,7]
def binary_search(low,high,l,value):
    m=(low+high)//2
    if l[m]>value:
        return (binary_search(low,m,l,value))
    elif l[m]<value:
        return (binary_search(m+1,high,l,value))
    else:
        return m
print(binary_search(0,len(l)-1,l,3))'''
'''l1=[]
l=[2,5,3,1,4,7,6]
for i in range(len(l)-1,0,-1):
    l2=l
    print(l1,l2)
    for j in range(0,len(l)-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
    l1=l2'''
    

'''l=[2,5,4,3,1]
for i in range(0,len(l)-1):
    j=i
    while(j>=0 and l[j]>l[j+1]):
        l[j],l[j+1]=l[j+1],l[j]
        j-=1
    print(l) '''     
'''import numpy as py
matrix=py.array([1,2],[2,3])
print(matrix)'''
l=[3,2,4,5,1]
for i in range(len(l)-1):
    smallest=i
    for j in range(i+1,len(l)):
        if l[j]<l[smallest]:
            smallest=j
    l[i],l[smallest]=l[smallest],l[i]        
print(l)
'''alist=[3,2,4,5,1]
for i in range(0, len(alist) - 1):
    smallest = i
    for j in range(i + 1, len(alist)):
        if alist[j] < alist[smallest]:
            smallest = j
    alist[i], alist[smallest] = alist[smallest], alist[i]
print(alist)'''    