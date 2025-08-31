import matplotlib.pyplot as plt

# Sample data
x = [5, 7, 8, 7, 6, 9, 4, 3, 8, 5]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]
sizes = [100,200,300,400,500,600,700,800,900,1000]

# Coloring depends on 'y' values
plt.scatter(x, y, c=y, s=sizes, cmap='viridis')  
plt.colorbar(label="Y value")   # shows color scale

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter with Colormap")
plt.show()
