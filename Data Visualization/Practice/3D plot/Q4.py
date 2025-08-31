import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Create meshgrid
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Function
Z = np.sin(np.sqrt(X**2 + Y**2))
surf=ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor='none')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Surface Plot")
fig.colorbar(surf, shrink=0.5, aspect=10) # color scale
plt.show()
import numpy as np

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Create meshgrid
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Function
Z = np.sin(np.sqrt(X**2 + Y**2))
surf=ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor='none')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Surface Plot")

fig.colorbar(surf, shrink=0.5, aspect=10) # color scale
plt.show()