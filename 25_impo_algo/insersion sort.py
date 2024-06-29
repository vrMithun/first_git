arr=[5,2,4,6,1,3]  #creating an array
for i in range(1,len(arr)):  #iterating the array throught for loop
    key=arr[i]                  
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j=j-1
        print(arr)
    print("break")
    arr[j+1]=key
