import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(1,10,100)
y=np.linspace(1,10,100)

X,Y=np.meshgrid(x,y)

fig=plt.figure(figsize=(5,7))
ax=fig.add_subplot(111,projection="3d")

Z=np.sin(X)*np.cos(Y)+0.5*np.sin(2*X)*np.cos(2*Y)

surf=ax.plot_surface(X,Y,Z,cmap="viridis")
ax.plot_wireframe(X,Y,Z,color='k',lw=0.3)
ax.contour(X,Y,Z,zdir='x',offset=0,cmap="viridis")
ax.contour(X,Y,Z,zdir="y",offset=10.7)
ax.contour(X,Y,Z,zdir='z',offset=-2)
ax.set_title("some function")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

fig.colorbar(surf,shrink=0.5)
plt.show()