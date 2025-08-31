import numpy as np

#Create a column vector of shape (4, 1) with values [10, 20, 30, 40]
vector=np.array([[10],[20],[30],[40]])

#Extract the second row from this matrix:
mat = np.array([[5, 10], [15, 20], [25, 30]])
print(mat[1])

#add two matrix:
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A+B)