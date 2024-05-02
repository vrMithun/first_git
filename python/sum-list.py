def exponent(x,n):
    if n==0:
        return 1
    else:
        return x*exponent(x,n-1)
    
print(exponent(2,3))   
        
    