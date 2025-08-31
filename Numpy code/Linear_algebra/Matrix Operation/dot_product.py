import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
print(A @ B)
# Output: [[19 22]
#          [43 50]]

# Equivalent:
print(np.dot(A, B))
