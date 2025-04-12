def fun(arr,num,length=None):
    if length is None:
        length=0
    if length==len(arr):
        return 0
    if arr[length]==num:
        return 1+fun(arr,num,length+1)    
    else:
        return 0+fun(arr,num,length+1)
print(fun([1, 2, 3, 2, 2, 2],2))    

'''def fun(arr, num, length=None):
    if length is None:
        length = 0
    if length == len(arr):
        return 0
    if arr[length] == num:
        return 1 + fun(arr, num, length + 1)
    else:
        return fun(arr, num, length + 1)'''
