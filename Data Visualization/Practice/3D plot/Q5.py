import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111, projection='3d')

# Create grid
x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))  # same function as before

# Wireframe plot
ax.plot_wireframe(X, Y, Z, color='blue')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
