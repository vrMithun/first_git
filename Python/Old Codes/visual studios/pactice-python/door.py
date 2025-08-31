'''n=int(input('enter'))
l=[]
for i in range(0,n):
    x=int(input('enter'))
    for i in range(0,3):
        y=int(input('enter'))
        if y<=3:
            l.append(y)
    if l[x-1]!=0:
        print('yes')
    else:
        print('no')'''
n=int(input('enter number of inputs: '))
l=[]
for i in range(0,n):
    k1=int(input('enter initial key number: '))
    keys=list(map(int,input().split()))
    if 3>=keys[k1-1]>0 and 3>=keys[keys[k1-1]]>0:
            print('yes')
    else:
        print('no')   
    keys.clear()       