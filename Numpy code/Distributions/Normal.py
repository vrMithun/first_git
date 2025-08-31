import numpy as np

# Generate 1000 samples from a normal distribution with mean=0, std=1
samples = np.random.normal(loc=0.0, scale=1.0, size=1000)
print(samples[:10])

import matplotlib.pyplot as plt

plt.hist(samples, bins=30, edgecolor='black', density=True)
plt.title("Normal Distribution (μ=0, σ=1)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True)
plt.show()
