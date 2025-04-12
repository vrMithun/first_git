def gcd(a,b,divisor=None):
    if divisor==None:
        divisor=a//2
    elif a==b or b%a==0:
        return a
    elif a%divisor==0 and b%divisor==0:
        return divisor
    return gcd(a,b,divisor-1)
print(gcd(56,98))
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)  # Recursive case using Euclid's algorithm

print(gcd(56, 98))  # Output: 14
