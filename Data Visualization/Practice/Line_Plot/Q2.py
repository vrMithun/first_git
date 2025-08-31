'''
Use different line styles, colors, and markers for the two cities.
Add legend labels "City 1" and "City 2".
Add x-axis label: "Month", y-axis label: "Avg Temperature (°F)".
Add title: "Monthly Avg Temperature – City 1 vs City 2"
Rotate x-axis labels for better readability if needed.
'''
import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temp_city1 = np.array([30, 32, 45, 55, 65, 75, 80, 78, 70, 58, 45, 35])
temp_city2 = np.array([25, 28, 38, 50, 60, 70, 75, 73, 65, 55, 40, 30])
plt.plot(months,temp_city1,ls="-.",color="#0DFF00",label="City 1")
plt.plot(months,temp_city2,ls="--",color="#5100FF",label="City 2")
plt.xlabel("Month")
plt.ylabel("Avg Temperature (°F)")
plt.title("Monthly Avg Temperature – City 1 vs City 2")
plt.grid()
plt.xticks(rotation=45)
plt.show()

