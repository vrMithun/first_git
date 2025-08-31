n=str(input("Enter original number: "))
m=str(input("Enter the gussed number: "))
a=0
b=0
c=0
d=0
for i in n:
    if m[a]==i:
            b=b+1                  
    else:
        for j in m:
            if i==j:
                c=c+1
    a=a+1
print(b,'-',c)
  
 