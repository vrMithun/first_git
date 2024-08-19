def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quickSort(arr,low,high):
           if low<high:
                pivot_index=partition(arr,low,high)
                quickSort(arr,low,pivot_index-1)
                quickSort(arr,pivot_index+1,high)
arr=[10,7]
quickSort(arr,0,len(arr)-1)
print(arr)               