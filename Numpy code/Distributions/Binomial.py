import numpy as np

# Simulate 1000 experiments of 10 coin tosses each, probability of heads = 0.5
samples = np.random.binomial(n=10, p=0.5, size=1000)
print(samples[:10])

import matplotlib.pyplot as plt

plt.hist(samples, bins=range(0, 12),  edgecolor='black')
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of Successes")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
