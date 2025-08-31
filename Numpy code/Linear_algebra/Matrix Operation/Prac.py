import numpy as np

#Multiply the matrix A = [[2, 3], [4, 5]] by scalar 10.
A=np.array([[2, 3], [4, 5]])
print(10*A)

#Matrix multiplication.
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2], [3, 4], [5, 6]])
print(A@B)

#Show element-wise multiplication of two 2x3 matrices:
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[6, 5, 4], [3, 2, 1]])

print(A*B)
