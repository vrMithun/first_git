def mergeSort(arr,left,right):
    if left==right:
        return [arr[left]]
    else:
        mid=(right+left)//2
        leftarr=mergeSort(arr,left,mid)
        rightarr=mergeSort(arr,mid+1,right)
    return merge(leftarr,rightarr)
def merge(leftarr,rightarr):
    result=[]
    rightIndex=0
    leftIndex=0
    while leftarr and rightarr:
        if leftarr[leftIndex]>rightarr[rightIndex]:
            result.append(rightarr[rightIndex])
            rightarr.pop(rightIndex)
        else:
            result.append(leftarr[leftIndex])
            leftarr.pop(leftIndex)
    if len(leftarr)>0:
        result+=leftarr
    else:
        result+=rightarr
    return result
lst=[4,2,66,7,9] 
print(mergeSort(lst,0,len(lst)-1))                  
