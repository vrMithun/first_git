import matplotlib.pyplot as plt

'''
Marker color: blue
Marker shape: circle ('o')
Marker size: 50
Title: "Basic Scatter Plot"
X-axis label: "X Values"
Y-axis label: "Y Values"
Show grid
'''

x = [5, 7, 8, 7, 6, 9, 5, 6, 7, 8]  
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

plt.scatter(x,y,marker="o",s=100)
plt.title("Basic Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid()
plt.show()