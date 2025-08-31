import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y, marker='o', color='navy')

# Add text at the start and end
plt.text(0, 0, "Start", fontsize=10, color='blue')
plt.text(4, 16, "End", fontsize=10, color='red')

# Add a general comment with a background box
plt.text(1, 10, "This is a quadratic curve",
         fontsize=12, color='darkgreen',
         bbox=dict(facecolor='lightyellow', edgecolor='black'))

plt.title("Text Example on Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()
