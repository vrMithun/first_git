import matplotlib.pyplot as plt
'''
Loop through temp_data and plot each city’s line on the same chart.
Use different line styles, markers, and colors (your choice).
Add a legend with city names.
Add a title: "Temperature Comparison Across Cities"
Label the x-axis: "Month" and y-axis: "Avg Temp (°F)"
Rotate x-axis labels if needed.
Show grid and use tight_layout().
'''

temp_data = {
    "City A": [30, 32, 45, 55, 65, 75, 80, 78, 70, 58, 45, 35],
    "City B": [25, 28, 38, 50, 60, 70, 75, 73, 65, 55, 40, 30],
    "City C": [40, 42, 50, 60, 70, 85, 90, 88, 78, 68, 50, 45]
}
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

colors = ['r', 'g', 'b']
linestyles = ['-', '--', '-.']
markers = ['o', 's', '^']

for (city,val),c,ls,markers in zip(temp_data.items(),colors,linestyles,markers):
    plt.plot(months,val,color=c,ls=ls,marker=markers,label=city)
plt.grid()
plt.show()