import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)

fig=plt.figure(figsize=(7,5))
ax=fig.add_subplot(111,projection='3d')

ax.scatter(x,y,z,s=80,c=y,cmap="binary")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()