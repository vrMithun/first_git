test=open('recurtion-fibo.txt','w')
test.write('''def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
for i in range(10):
    print(fibo(i),end=' ')''')
test.close()
test=open('recurtion-fibo.txt','r')
print(test.read())
test=open('recurtion-sumdigits.py','r')
print(test.read)
    
