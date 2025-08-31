import numpy as np

# Transpose the matrix
A = np.array([[1, 3, 5], [2, 4, 6]])
print(A.T)

#Create a 4×4 identity matrix.
identit=np.eye(4)
print(identit)

#Check if the following matrix is invertible, and find its inverse if it is:
A = np.array([[2, 1], [7, 4]])
isinverse=np.linalg.det(A)==0
if not isinverse:
    print(np.linalg.inv(A))