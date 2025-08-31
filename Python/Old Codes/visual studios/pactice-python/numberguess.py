print("is the number between 1 and 50?")
n=str(input())
if n=="yes":
    print("is the number is between 1 and 25")
else:
    print("is the number is between 50 and 75") 
m=str(input())

if n=='no' and m=="yes":
    print("is the number between 50 and 68")
elif n=='no' and m=='no':
    print("is the number between 75 and 88")
l=str(input())    
if m=="yes" and n=='yes' and l=="yes":
    for i in range(1,16):
        print(i)
        k=str(input("yes or no:"))
        if k=="yes":
            break
elif m=="yes" and n=='yes' and l=="no": 
    for i in range(17,25):
        print(i)
        k=str(input("yes or no:"))
        if k=="yes":
            break
if m=='no' and n=='yes' and l=='yes':
     for i in range(25,38):
        print(i)
        k=str(input("yes or no:"))
        if k=="yes":
            break   
elif m=='no' and n=='yes' and l=='no':
     for i in range(38,50):
        print(i)
        k=str(input("yes or no:"))
        if k=="yes":
            break  
if m=='yes' and n=='no' and l=='yes' :
     for i in range(50,68):
        print(i)
        k=str(input("yes or no:"))
        if k=="yes":
            break
elif m=='yes' and n=='no' and l=='no':
     for i in range(68,75):
        print(i)
        k=str(input("yes or no:"))
        if k=="yes":
            break   
if m=="no" and n=="no" and l=="yes" :
     for i in range(75,88):
        print(i)
        k=str(input("yes or no:"))
        if k=="yes":
            break  
elif m=="no" and n=="no" and l=="no":
     for i in range(88,101):
        print(i)
        k=str(input("yes or no:"))
        if k=="yes":
            break 
print("i found it!!!")                                        
        
     


