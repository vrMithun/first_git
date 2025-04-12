list1=[3,2,5,9,6]
for i in range(len(list1)):
    key=i
    min=i
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            min=j
    if list1[key]>list1[min]:
        list1[key],list1[min]= list1[min],list1[key]     
print(list1)