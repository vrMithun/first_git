from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Create figure
plt.figure(figsize=(8,6))

# Setup Basemap with Robinson projection
m = Basemap(projection="robin",lon_0=90)
# Draw basic map features
m.drawcoastlines()   # coastlines
m.drawcountries()    # country borders
m.fillcontinents(color='lightgreen', lake_color='lightblue')  # fill land/water
m.drawmapboundary(fill_color='lightblue')  # background for oceans

plt.title("Basic World Map with Basemap")
plt.show()
