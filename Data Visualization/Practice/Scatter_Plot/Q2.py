import matplotlib.pyplot as plt

'''
Plot both classes on the same scatter plot.
Class A:
Marker color: red
Marker shape: triangle ('^')
Marker size: 80
Class B:
Marker color: green
Marker shape: square ('s')
Marker size: 80
Add legend: "Class A" and "Class B".
Add title: "Height vs Weight Comparison"
X-axis label: "Height (cm)"
Y-axis label: "Weight (kg)"
Add grid and use tight_layout().
'''

heights_a = [150, 152, 160, 165, 170, 172, 175]
weights_a = [50, 52, 55, 60, 65, 68, 70]

heights_b = [155, 158, 162, 168, 173, 178, 180]
weights_b = [54, 56, 58, 63, 67, 72, 75]

sct=plt.scatter(heights_a,weights_a,s=80,c=weights_a,marker='^',label="Class A",cmap="viridis")
plt.colorbar(sct)
plt.scatter(heights_b,weights_b,color="g",marker='s',s=80,label="Class B")
plt.legend()
plt.title("Height vs Weight Comparison")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid()
plt.show()
