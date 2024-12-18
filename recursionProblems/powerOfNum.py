def fun(a,b):
    if b==0:
        return 1
    return a*fun(a,b-1)
print(fun(2,3))