import numpy as np

# find eigen value and vectors
A = np.array([[4, -2], [1, 1]])
value,vector=np.linalg.eig(A)
print(value)
print(vector)

# Verification
rhs=A@vector[:,0]
lhs=value[0]*vector[:,0]
print(rhs)
print(lhs)