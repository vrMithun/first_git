n=int(input('Enter any number: '))
for i in range(0,n):
    for a in range(0,n-i):
        print('-',end=" ")
    for b in range(0,i+1):
        print('*',end='   ')
    print(end='\n')      
for i in range(0,n):
    for a in range(0,i+2):
        print(' ',end=" ")
    for b in range(0,n-i-1):
        print('*',end='   ')
    print(end='\n') 
   
