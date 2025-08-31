import numpy as np


#solving equation in 3 variables
A = [[1, 2, 3],
     [2, 1, 1],
     [3, 4, 5]]

b = [14, 10, 28]
x=np.linalg.solve(A,b)
print(x)

'''
Solve:
x -  y = 1  
x +  y = 5
'''
A=np.array([[1,-1],[1,1]])
b=np.array([1,5])
x=np.linalg.solve(A,b)
print(x)