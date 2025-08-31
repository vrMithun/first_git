import matplotlib.pyplot as plt

weeks = [1, 2, 3, 4, 5, 6, 7, 8]
revenue = [42, 47, 45, 53, 51, 56, 54, 60]
err_low = [3, 2, 4, 3, 2, 5, 3, 4]
err_high = [5, 4, 3, 6, 5, 4, 6, 5]

plt.errorbar(weeks,revenue,yerr=[err_low,err_high],fmt='o',capsize=5,mfc="#FA0404")
plt.xlabel("weeks")
plt.ylabel("revenue")
plt.grid()
plt.title("weekly revenue")
plt.show()