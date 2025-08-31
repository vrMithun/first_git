import numpy as np
import matplotlib.pyplot as plt
'''
Generate 5000 values with mean=50 and std=10. Plot a histogram.
Simulate 1000 students’ IQ scores with mean 100 and std 15. Find how many have IQ above 130.
Generate a 2D normal dataset (shape 3x3) with mean=10 and std=5.
'''

sample=np.random.normal(loc=50,scale=10,size=5000)


plt.hist(sample,bins=30,density=False)
plt.title("Normal distribution")
plt.xlabel("bins")
plt.ylabel("values")
plt.grid()
plt.show()

sample=np.random.normal(loc=100,scale=15,size=1000)
print(len(sample[sample>130]))

sample=np.random.normal(loc=10,scale=5,size=(3,3))
print(sample)