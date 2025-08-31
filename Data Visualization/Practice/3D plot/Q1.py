import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(7,5))
ax=fig.add_subplot(111,projection='3d')
ax.set_title("3D axes — setup test")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()