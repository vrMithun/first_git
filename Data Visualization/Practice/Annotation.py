import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y, marker='o')
plt.annotate("Shrink 0.05", xy=(3, 9), xytext=(2, 15),
             arrowprops=dict(facecolor='blue', shrink=0.05))

plt.annotate("Shrink 0.3", xy=(4, 16), xytext=(3, 22),
             arrowprops=dict(facecolor='red', shrink=0.3))

plt.annotate("Shrink 0.7", xy=(2, 4), xytext=(1.5, 10),
             arrowprops=dict(facecolor='green', shrink=0.7))
plt.grid()
plt.show()
