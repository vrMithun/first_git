from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
m = Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=80,
            llcrnrlon=-180, urcrnrlon=180, resolution='c')

# Draw map
m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='lightyellow', lake_color='lightblue')
m.drawmapboundary(fill_color='lightblue')

# Plot cities (Delhi, Mumbai, Chennai)
lats = [28.61, 19.07, 13.08]
lons = [77.23, 72.87, 80.27]
x, y = m(lons, lats)   # convert lat/lon to map projection
m.scatter(x, y, color='red', s=100, marker='o')

plt.title("Indian Cities on Map (Basemap)")
plt.show()
