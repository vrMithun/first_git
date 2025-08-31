import numpy as np

# Define vectors a and b
a = np.array([3, 4])
b = np.array([1, 2])

# Step 1: Dot product of a and b
dot_product = np.dot(a, b)

# Step 2: Magnitude squared of b
b_norm_sq = np.dot(b, b)

# Step 3: Projection formula
projection = (dot_product / b_norm_sq) * b

# Result
print("Vector a:", a)
print("Vector b:", b)
print("Projection of a onto b:", projection)
