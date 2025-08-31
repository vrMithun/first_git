'''
Plot the following data using matplotlib's line plot:
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]
Add:
A title: "Square Numbers"
X-axis label: "Input"
Y-axis label: "Output"
'''
'''
Plot the same data (x, y) but now:
Change the line color to red.
Make the line dashed.
Use circle markers ('o') on each data point.
Set line width to 2.
Add a legend labeled "y = x²".
'''

import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,2,3,4,5])
y=np.array([0,1,4,9,16,25])
plt.plot(x,y,color="r",ls="--",marker='o',lw=2,label="y=x^2")
plt.title("Square numbers")
plt.legend()
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.show()