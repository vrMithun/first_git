from array import *
a=array('i',[])
arr=array('i',[1,2,3,4,5])
'''for i in range(len(arr)-1,-1,-1):#tried to print the array in reverse
    r=arr.pop(i)                    #the range indicates that go from
    a.append(r)                     #len(arr)-1 to -1 by the step -1
print(a)'''
arr.reverse()#just can be done like this :<
print(arr)