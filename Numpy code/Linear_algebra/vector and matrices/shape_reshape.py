import numpy as np

vector=np.array([1,2,3,4,5,6])
matrix=np.array([[1,2],[2,4]])

print(vector.shape)
print(matrix.shape)

reshaped_vector=vector.reshape(2,3)
print(reshaped_vector)