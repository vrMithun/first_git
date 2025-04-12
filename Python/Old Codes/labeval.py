test=open('descending_numbers.txt','w')
test.write('98 87 76 65 54 43 32 21 10 5')
test.close()
with open('descending_numbers.txt') as file:
    for line in file:
        number=line.split( )
l1=[]
def reverse_list_recursive(l,s):
    if s==0:
        return 0
    else:
        l1.append(l[s-1])
        return reverse_list_recursive(l,s-1)
reverse_list_recursive(number,len(number))    
def binary_search_recursive(n,h,l,l1):
    m=(h+l)//2
    print(m)
    if l1[m]==n:
        return l1[m]
    elif n>m:
        return binary_search_recursive(n,h,m+1,l1)
        
    else:
        return binary_search_recursive(n,m,l,l1)
print(binary_search_recursive(32,9,0,l1))       
print('original_list:',number)
print('reverse_list:',l1)

        
        
