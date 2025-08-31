import numpy as np

v = np.array([3, 4])
unit_v = v / np.linalg.norm(v)
print(unit_v)
# Output: [0.6 0.8] → magnitude = 1
