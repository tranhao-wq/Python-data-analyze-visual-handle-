import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

# Absolute path to the Natural Earth shapefile
shapefile_path = r"D:\Download-D\Natural_Earth_quick_start\packages\Natural_Earth_quick_start\10m_cultural\ne_10m_admin_0_countries.shp"

# Load the shapefile
df = gpd.read_file(shapefile_path)

# Example: fake population and area for demonstration
np.random.seed(0)
df['pop_est'] = np.random.randint(1_000_000, 200_000_000, len(df))
df['area'] = np.random.randint(10_000, 10_000_000, len(df))
df['pop_density'] = df['pop_est'] / df['area']

fig, ax = plt.subplots(figsize=(10, 6))
df.plot(column='pop_density', ax=ax, legend=True, cmap='YlOrRd', edgecolor='black')
ax.set_title('World Population Density by Country')
ax.set_axis_off()
plt.tight_layout()
plt.show() 