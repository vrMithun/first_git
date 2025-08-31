import numpy as np
import matplotlib.pyplot as plt
#Generate 5000 exponential samples with average waiting time = 2 units. Plot the histogram.

sample=np.random.exponential(scale=2,size=5000)
print(sample[:10])

plt.hist(sample, bins=30, density=True, edgecolor='black')
plt.title("Exponential Distribution (scale=1.0)")
plt.xlabel("Time between events")
plt.ylabel("Density")
plt.grid(True)
plt.show()