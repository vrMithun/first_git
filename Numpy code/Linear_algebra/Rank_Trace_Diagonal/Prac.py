import numpy as np

'''
Find the rank of:
[[2, 4],
 [1, 2]]
'''
A=np.array([[2, 4],[1, 2]])
rank=np.linalg.matrix_rank(A)
print(rank)

'''
What is the trace of this matrix?
[[3, 2, 1],
 [0, 5, 2],
 [1, 0, 7]]
'''
B=np.array([[3, 2, 1],
            [0, 5, 2],
            [1, 0, 7]])
trace=np.trace(B)
print(trace)

#Create a 4x4 diagonal matrix using the list: [1, 3, 5, 7]
mylist=np.array([1,3,5,7])
matrix=np.diag(mylist)
print(matrix)

'''
Extract the diagonal of the matrix:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
'''

matrix=np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

diagonal=np.diag(matrix)
print(diagonal)