import numpy as np

# Generate 1000 values from a uniform distribution between 0 and 10
samples = np.random.uniform(low=0.0, high=10.0, size=1000)
print(samples[:10])  # Print first 10 samples


import matplotlib.pyplot as plt

plt.hist(samples, bins=20, edgecolor='black', density=True)
plt.title("Uniform Distribution (0 to 10)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True)
plt.show()
