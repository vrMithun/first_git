n=int(input('Enter any number: ')) 
for i in range (0,n):
    if i==0 or i==n-1:
        for a in range (0,n):
            print("*",end=' ') 
        print(end='\n')                   
                  
    else:
        for b in range(0,n):
            if b==0 or b==n-1:
                print("*",end=" ")    
            else:
                print("   ",end=" ")  
        print(end='\n')              
    
