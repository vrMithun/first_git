import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print("Array:\n", a)
print("Shape:", a.shape)        # (2 rows, 3 columns)
print("Dimensions:", a.ndim)    # 2D array
print("Data Type:", a.dtype)    # int64 or int32
print("Total Elements:", a.size)
print("Element Size (bytes):", a.itemsize)
print("Total Memory (bytes):", a.nbytes)  # size * itemsize
