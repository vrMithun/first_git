import numpy as np

'''
Project a = [2, 3] onto b = [5, 0].
Also compute the orthogonal component.
'''
a=np.array([2,3])
b=np.array([5,0])

adotb=np.dot(a,b)
bdotb=np.dot(b,b)

projection=(adotb/bdotb)*b

ortho=a-projection

print(projection)
print(ortho)