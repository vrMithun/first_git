def fun(num):
    if num==0:
        return 0
    return num%10+fun(num//10)
print(fun(1643))