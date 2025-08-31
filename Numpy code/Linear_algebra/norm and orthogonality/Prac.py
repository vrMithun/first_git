import numpy as np

#Compute the L2 norm of: v = np.array([6, 8])
v=np.array([6,8])
norm=np.linalg.norm(v)

#Check if the vectors a = [1, -1] and b = [1, 1] are orthogonal
a=np.array([1,-1])
b=np.array([1,1])
dotPro=np.dot(a,b)==0
print(dotPro)

#Normalize the vector v = [9, 12] to a unit vector
a=np.array([9,12])
norm=np.linalg.norm(a)
result=a/norm
print(result)