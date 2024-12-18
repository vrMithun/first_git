def check(arr,length=None):
    if length is None:
        length=0
    if length==len(arr)-1:
        return True
    if arr[length]>arr[length+1]:
        return False
    return check(arr,length+1)   
print(check([1,2,3,0,5]))