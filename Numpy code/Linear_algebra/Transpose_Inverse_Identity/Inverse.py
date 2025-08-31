import numpy as np

A = np.array([[4, 7], [2, 6]])
A_inv = np.linalg.inv(A)
print(A_inv)

# Verify: A @ A_inv ≈ Identity
print(np.round(A @ A_inv, 2))

