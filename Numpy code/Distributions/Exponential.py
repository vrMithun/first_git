import numpy as np

# Generate 1000 exponential samples with scale=1.0
samples = np.random.exponential(scale=1.0, size=1000)
print(samples[:10])

import matplotlib.pyplot as plt

plt.hist(samples, bins=30, density=True, edgecolor='black')
plt.title("Exponential Distribution (scale=1.0)")
plt.xlabel("Time between events")
plt.ylabel("Density")
plt.grid(True)
plt.show()
