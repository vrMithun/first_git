name=[]
att=[]
i=0
j=0
k=0
l=0
a=[]
p=[]
dec=[]
m=0
for i in range(0,5):
    name.append(str(input()))
for j in range(0,5)   :
    att.append(int(input())) 
d=dict(zip(name,att))
e=dict(zip(att,name)) 
for k in range(0,5):
    if (d.get(name[k])/60)*100>=80:
         a.append(name[k])   
print(a)
att.sort()
att.reverse()
for l in range(0,5):
    f=e.get(att[l])
    dec.append(f)
print(dec)   
while m<5:
    if 48-d.get(name[m])>=0:
        z=48-d.get(name[m])
        p.append(z)
        m=m+1
    else:
        m=m+1    
print(dict(zip(name,p)))
'''
n=int(input('enter'))
l=[]
for i in range(0,n):
    x=int(input('enter'))
    for i in range(0,3):
        y=int(input('enter'))
        if y<=3:
            l.append(y)
    if l[x-1]!=0 and l[l[x-1]-1]!=0:
        print('yes')
    else:
        print('no')'''

'''dict={}
dict2={}
dict3={}
n=int(input('enter'))
for i in range(0,n):
    name=input('enter')
    percentage=int(input('enter'))
    dict.update({name:percentage})
    if percentage>=80:
        dict2.update({name:percentage})
print(dict2)
l1=list(dict.values())
l=len(l1)
l1=l1.sort()
l2=list(dict.keys())
for i in range(0,l):
    dict3.update({l2.index(l1[i]):l1[i]})
print(dict3)'''

