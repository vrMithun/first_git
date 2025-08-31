import matplotlib.pyplot as plt

marks = [45, 55, 67, 72, 88, 90, 45, 53, 61, 77, 
         85, 92, 73, 68, 81, 76, 62, 59, 47, 66]

plt.hist(marks,bins=[40, 50, 60, 70, 80, 90, 100],color="#E60B0B",
         edgecolor='#000000',alpha=1,rwidth=0.9,orientation="horizontal")
plt.xlabel("marks")
plt.ylabel("number of studets")
plt.title("marks stat")
plt.grid()
plt.show()