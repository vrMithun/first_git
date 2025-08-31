n=int(input('Enter number of inputs: '))
l=[]
for i in range(n):
    a=input('enter name of the list: ')
    l.append(a)
for j in range(n):
    a=str(input('enter experiment name: '))
    b=str(input('enter field name: '))
    c=list(map(str,input().split( )))
    d=int(input('enter year: '))
    l[j]=[]
    l[j].append(a)
    l[j].append(b)
    l[j].append(c)
    l[j].append(d)
print(l)
field=[]
field=l[0][2]+l[1][2]
print(field)
country=str(input())
for m in range(len(l)):
    for o in range(len(l[m][2])):
        if l[m][2][o]==country:
            print(l[1],end=' ')