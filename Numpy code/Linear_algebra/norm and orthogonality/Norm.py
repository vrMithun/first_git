import numpy as np

# L2 Norm (Euclidean norm)
v = np.array([3, 4])
norm = np.linalg.norm(v)
print(norm)  # Output: 5.0

#L1 Norm (Manhattan norm)
l1_norm = np.linalg.norm(v, ord=1)
print(l1_norm)  # 7

#Infinity Norm
inf_norm = np.linalg.norm(v, ord=np.inf)
print(inf_norm)  # 4
