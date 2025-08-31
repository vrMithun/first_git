import matplotlib.pyplot as plt
year       = [2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024]
avg_temp   = [0.45, 0.50, 0.55, 0.65, 0.70, 0.75, 0.85, 0.95, 1.05, 1.10, 1.20, 1.25, 1.30]  # °C anomaly
co2_ppm    = [370, 374, 378, 384, 389, 395, 400, 405, 410, 416, 420, 425, 430]               # ppm
sea_level  = [0, 8, 16, 28, 38, 50, 63, 77, 91, 100, 107, 114, 120]                         # mm rise

plt.style.use("ggplot")
plt.subplot(2,2,1)
plt.plot(year,avg_temp,'r--o',lw=0.5,label="avg_temp")
plt.xlabel("year")
plt.ylabel("avg_temp")
plt.title("avg-temp vs year")
plt.xlim((2000,2025))
plt.annotate("max temperature",xy=(2024,1.3),xytext=(2022,1.25),color='b',arrowprops=dict(facecolor="k",shrink=0.5))
plt.grid()
plt.legend()

plt.subplot(2,2,2)
plt.plot(year,co2_ppm,':^',color="#4C13E7",lw=0.7,label="co2")
plt.xlabel("year")
plt.ylabel("co2_ppm")
plt.title("co2-ppm vs year")
plt.xlim((2000,2025))
plt.grid()
plt.legend()

plt.subplot(2,2,3)
plt.plot(year,sea_level,"b:p",lw=0.8,label="sea_level")
plt.xlabel("year")
plt.ylabel("sea_level")
plt.title("sea_level vs year")
plt.xlim((2000,2025))
plt.grid()

plt.legend()
plt.suptitle("climate analysis")
plt.tight_layout()
plt.show()

