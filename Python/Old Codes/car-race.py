speed1=int(input('Enter the speed of car 1: '))
speed2=int(input('Enter the speed of car 2: '))
pos1=int(input("enter the position of car 1: "))
pos2=int(input("enter the position of car 2: "))
len=int(input("enter the length of the track: "))
def result1(w,l):
        c=0
        d=0
        print("car1",end=' ')
        while c<=a:
                print(a,end=' ')
                a=a+speed1
                c=c+1
        print(w)        
        print()
        print("car2",end=' ')  
        while d<=b:
                print(b,end=' ')
                b=b+speed2
                d+=1   
        print(l)      
def result():
    a=0
    b=0
    i=0
    j=0
    if speed1>speed2:
        for i in range(0,len):
             a=a+speed1
             b=b+speed2
             if a>b: 
                   result1('winner','runner-up')
                   break
             elif a<b:      
                  result1('runner-up','winner')
                  break
             elif a==b and a>=len:
                   result1('tie','tie')
                   break
    elif speed2>speed1:
           for i in range(0,len):
             a=a+speed1
             b=b+speed2
             if a>b: 
                   result1('winner','runner-up')
                   break
             elif a<b:      
                  result1('runner-up','winner')
                  break
             elif a==b and a>=len:
                   result1('tie','tie')
                   break
    else:
           for i in range(0,len):
             a=a+speed1
             b=b+speed2
             if a>b: 
                   result1('winner','runner-up')
                   break
             elif a<b:      
                  result1('runner-up','winner')
                  break   
print(result())                            
'''def result(w,l):
            a=pos1
            b=pos2
            c=0
            d=0
            print("car1",end=' ')
            while c<=len:
                    print(a,end=' ')
                    a=a+speed1
                    c=c+1
            print(w)        
            print()
            print("car2",end=' ')  
            while d<=len:
                print(b,end=' ')
                b=b+speed2
                d+=1
            print(l)                     
if speed1==speed2 and pos1==pos2:
        result("tie",'tie')    
elif speed1==speed2:
        if pos1>pos2:
                result('winner','looser')
        else: 
                result('looser','winner')
def result2(w,l):
        i=0
        a=pos1
        b=pos2
        while i<=len+speed1:
                a=a+speed1
                b=b+speed2
                if pos1==pos2:
                        break
        print('car1')        
        while j<pos1:
                a=a+speed1
                print(a,end=' ')
                j=j+1
        print(w) 
        print()     
        for i in range(0,pos2)  :
                b=b+speed2
                print(b,end=' ')
                i=i+1
        print(l)  '''     