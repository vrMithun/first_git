import matplotlib.pyplot as plt

classA = [45, 55, 67, 72, 88, 90, 45, 53, 61, 77, 
          85, 92, 73, 68, 81, 76, 62, 59, 47, 66]

classB = [50, 60, 70, 82, 89, 95, 48, 52, 63, 75,
          84, 91, 71, 69, 79, 73, 65, 58, 49, 67]

bins = [40, 50, 60, 70, 80, 90, 100]

plt.hist([classA,classB],bins=bins,color=["#F20B0B","#0B13E3"],edgecolor="#000000",
         alpha=0.7,label=["Class A","Class B"],histtype="bar",stacked=False)
plt.legend()
plt.xlabel("Marks")
plt.ylabel("count")
plt.title("Multi hist")
plt.grid()
plt.show()

