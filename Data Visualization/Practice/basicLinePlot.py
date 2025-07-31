import matplotlib.pyplot as plt
import numpy as np

x_axis=np.array([0, 1, 2, 3, 4, 5])
y_axis=np.array([0, 1, 4, 9, 16, 25])

plt.plot(x_axis,y_axis,'o:r',mfc="b",lw=2.5)
plt.grid()
plt.title("Basic Line Plot")
plt.xlabel("X values")
plt.ylabel("Squared Values")
plt.show()