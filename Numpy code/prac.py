import numpy as np
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)  # In-place shuffle
print(arr)

# Random sampling
print(np.random.choice(arr, size=3, replace=False))


