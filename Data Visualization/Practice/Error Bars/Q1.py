import matplotlib.pyplot as plt

monthly_sales=[20, 25, 22, 30, 28, 27]
standard_deviation=[2, 3, 2, 4, 3, 2]

plt.errorbar([i for i in range(1,7)],monthly_sales,yerr=standard_deviation,fmt='o',ecolor="#F60B0B")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly sales")
plt.grid()
plt.show()