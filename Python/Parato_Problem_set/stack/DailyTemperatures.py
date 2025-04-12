stack=[]
lst=[73,74,75,71,69,72,76,73]
result=[0]*len(lst)
for i in range(len(lst)):
    if len(stack)==0:   
        stack.append(i)
    else:
        stack.append(i)
        for j in range(len(stack)-1,0,-1):
            if lst[stack[j]]>lst[stack[j-1]]:
                print(result)
                result[stack[j-1]]=stack[j]-stack[j-1]
                stack.pop(j-1)
print(result)                        
        