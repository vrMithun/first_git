'''
1)Generate 5000 samples between -5 and 5. Plot the histogram.
2)Generate a 2D array (5x5) of uniform random numbers between 100 and 200.
3)Simulate 10,000 lottery draws from uniform(1, 50) and find the average drawn number.
'''

import numpy as np

sample=np.random.uniform(low=-5,high=5,size=5000)
print(sample[:10])

array_2d = np.random.uniform(low=100, high=200, size=(5, 5))
print("5x5 Uniform Random Array between 100 and 200:\n", array_2d)

lottery=np.random.uniform(low=1,high=50,size=10000)
print(np.mean(lottery))
