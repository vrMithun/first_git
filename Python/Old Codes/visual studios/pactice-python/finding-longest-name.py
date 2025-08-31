n=int(input("Enter number of inputs: "))#gettin number of inputs.
l=[]#list of names.
i=0
ch=''
j=0
for i in range(0,n):
    s=str(input("Enter any word: "))#getting words as input.
    l.append(s)#adding the words to list.

while j<len(l)-1:
    if len(l[j])>len(l[j+1]):
        ch=l[j]
    elif len(l[j])<len(l[j+1]):
        ch=l[j+1]
    else:
        ch=(l[j],l[j+1])
    j=j+1       
print(ch)        


