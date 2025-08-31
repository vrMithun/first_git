i='my name is mithun. i am studying in amrita vishwa vidhyapeetham'
x=i.split(sep=' ')
y=['a','e','i','o','u']
print(x)
for a in range(0,11):
    if a%3==0:
        for b in x[a]:
            if b in y:           
                print(b.upper() , end='')
            else:
                print(b.lower(),end="")    
        print(end=' ')
    else :
        print(x[a],end='')   
        print(end=' ') 
            
