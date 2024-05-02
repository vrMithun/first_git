'''def binary(n):
    a=n//2
    b=n%2
    if a==0:
        return 1
    else:
        print(b,end='')
    return binary(a)
print(binary(10))
a=str(binary(10))
print(len(a))'''
ary = []

def dec2bin(num):
    ary.append(num%2)
    num = num//2
    if (num!=0):
        return dec2bin(num)
a=int(input('Enter a number: '))
dec2bin(a)      
print(*ary[::-1])
