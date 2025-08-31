'''Simulate 5000 dice throws where success is 
rolling a 6 (i.e., p = 1/6) and count number of 6s in each batch of 10 rolls.'''

import numpy as np
#np.random.seed(42)

sample=np.random.binomial(n=10,p=1/6,size=5000)
print(len(sample[sample>6]))