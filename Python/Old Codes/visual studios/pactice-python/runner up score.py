n=int(input("Enter the number of inputs: "))
list=[]
y=[]
for i in range(0,n):
    x=int(input("Enter any number: "))
    list.append(x)
print(list)
list.sort()
print(list[1])