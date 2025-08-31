import numpy as np

A = [[1, 2, 3],
     [2, 1, 1],
     [3, 4, 5]]

b = [14, 10, 28]
x=np.linalg.solve(A,b)
print(x)