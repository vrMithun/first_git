n=int(input('Enter number of input for a list: '))
i=0
j=0
k=0
list=[]
for i in range(0,n):
    a=int(input('Enter any number: '))
    list.append(a)
while j<len(list):
    for k in range(list[j]):
        print('*',end='')
    print() 
    j+=1   

