import time

print("Counting down:")
for i in range(10, 0, -1):
    print(i, end=' ')
    print(end='\r')
    time.sleep(1)
print("Blast off!")