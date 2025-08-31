import matplotlib.pyplot as plt
import numpy as np

# Parameter t
t = np.linspace(0, 20, 100)

# Coordinates (helix curve)
x = np.sin(t)
y = np.cos(t)
z = t

# Create figure and 3D axes
fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111, projection='3d')

# Line plot
ax.plot(x, y,z, color="red", label="Helix curve")

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
ax.set_title("3D Line Plot")

plt.show()
