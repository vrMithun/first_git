import numpy as np

# Simulate 1000 events with average rate λ = 3
samples = np.random.poisson(lam=3, size=1000)
print(samples[:10])

import matplotlib.pyplot as plt

plt.hist(samples, bins=range(0, max(samples)+1), align='left', edgecolor='black')
plt.title("Poisson Distribution (λ=3)")
plt.xlabel("Number of Events (k)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
