import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data=np.random.normal(0,1,300)

sns.kdeplot(data,color='r',fill=True)
#plt.hist(data,bins=10,histtype="bar",color="#401AEA",alpha=0.5)
plt.title("Normal Distribution")
plt.grid()
plt.show()