'''i=0
j=0
while i<100:
    while j<100:
        if j+(i**(1/2))==7 and (j**(1/2))+i==11:
            print(i,j)
            break
        j=j+1
    j=0    
    i=i+1  '''
i=0
while i<1000:
    if i**(i**7)==196:
        print(i)
        break
    else:
        print('none')
    i=i+1    

       