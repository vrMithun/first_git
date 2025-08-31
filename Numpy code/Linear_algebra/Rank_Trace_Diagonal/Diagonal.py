import numpy as np


B = np.array([[1, 2],
              [3, 4]])
diag = np.diag(B)
print("Diagonal of B:", diag)


#create diagonal matrix from list
values = [10, 20, 30]
D = np.diag(values)
print("Diagonal matrix:\n", D)
