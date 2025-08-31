import numpy as np

A = np.array([[2, 1], 
              [5, 3]])
b = np.array([[8], [18]])

x = np.linalg.solve(A, b)
print(x)   # [2. 4.] → So x = 2, y = 4
