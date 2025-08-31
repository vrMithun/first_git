import numpy as np

'''Simulate the number of customer arrivals per minute 
in a store (λ=4), for 5000 minutes. Plot the histogram.'''

sample=np.random.poisson(lam=4,size=5000)
print(sample[:10])

import matplotlib.pyplot as plt

plt.hist(sample,bins=range(0,max(sample)+1),density=True,edgecolor='b')
plt.grid()
plt.title("histogram")
plt.show()