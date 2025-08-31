'''n=(input("Enter any word: "))'''
s='xxxyyyzzz' # input
i = 0 # index
c = 1 # counter
for ch in str(s): # string traversal
    # print(i)
    i = i+1 # increment the index pos
    if i == len(s):
        print(c,end='') # print char count 
        print(ch,end='') # print char
        break
    if ch == s[i]:
        c = c+1 # increment the counter for current char
    else:
        print(c,end='') # print char count 
        print(ch,end='') # print char
        c = 1 # reset the counter for next char


   


               
            
               

'''print(l)
s=set(l)
for k in range(0,len(s)):
    for j in range(0,len(l)):
        if s[k]==l[j]:'''

     

            