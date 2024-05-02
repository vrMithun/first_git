def sumdig(n):
    a=n//10
    b=n%10
    if b==1:
        return 1
    else:
        return b+sumdig(a)
n=int(input('Enter any number: '))
print(sumdig(n))
