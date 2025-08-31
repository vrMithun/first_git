n=int(input("Enter any number: "))
j=0
for i in range(2,n):
    if n%i==0:
        print("it is not a prime number")
        j=j+1
        break
if j!=1:
    print("it is a prime number")    
  