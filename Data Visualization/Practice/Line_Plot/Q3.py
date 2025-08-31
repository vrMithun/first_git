'''
Create two subplots side by side (1 row, 2 columns).
First subplot: line plot for City 1
Use red dashed line with square markers.
Second subplot: line plot for City 2
Use blue dotted line with triangle markers.
Set individual titles for each subplot: "City 1 Temperature" and "City 2 Temperature".
Add common x-label: "Month" and y-label: "Avg Temp (°F)" for each.
Add plt.tight_layout() to prevent overlapping.
'''
import matplotlib.pyplot as plt


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temp_city1 = [30, 32, 45, 55, 65, 75, 80, 78, 70, 58, 45, 35]
temp_city2 = [25, 28, 38, 50, 60, 70, 75, 73, 65, 55, 40, 30]

plt.subplot(1,2,1)
plt.plot(months,temp_city1,color="r",ls="--",marker="s",label="City 1 Temperature")
plt.xlabel("Month")
plt.ylabel("Avg Temp (°F)")
plt.xticks(rotation=45)
plt.grid()

plt.subplot(1,2,2)
plt.plot(months,temp_city2,color="b",ls=":",marker="^",label="City 2 Temperature")
plt.xlabel("Month")
plt.ylabel("Avg Temp (°F)")
plt.xticks(rotation=45)
plt.grid()

plt.tight_layout()
plt.show()
