import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.random.normal(0, 1, 300)
y = np.random.normal(0, 1, 300)

# Joint KDE with contour lines
sns.kdeplot(x=x, y=y, fill=True,cmap="winter_r",thresh=0.05)
plt.title("2D KDE with Contours")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()
