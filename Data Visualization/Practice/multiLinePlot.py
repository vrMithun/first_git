import matplotlib.pyplot as plt
import numpy as np

x1=np.array([0, 1, 2, 3, 4])
y1=np.array([0, 1, 4, 9, 16])
y2=np.array([0, 2, 8, 18, 32])
y3=np.array([0, 3, 12, 27, 48])
y4=np.array([0, 4, 16, 36, 64])

plt.plot(x1,y1,marker='o',color='b',lw=2,ls="--")
plt.plot(x1,y2,marker='*',color='g',lw=2.5,ls="-.")
plt.plot(x1,y3,marker='s',color='#FF5733',lw=1.5,ls=":")
plt.plot(x1,y4,marker='^',color=(0,0.5,1,0.7),lw=3)
plt.legend(["Dashed", "Dash-dot", "Dotted", "Solid"],loc="best")
plt.grid()
plt.title("Multiple plot")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()