# %%
import json
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point, Polygon, LineString
import geodatasets

# %matplotlib inline

# %%
f = open('Records.json')
data = json.load(f)

# %%
locat = []

for i in data['locations']:
    locat.append(i)

f.close()

# %%
df = pd.DataFrame.from_dict(locat)


# %%
list(df.columns)

# %%
df['timestamp']

# %%
df['timestamp'] = pd.to_datetime(df['timestamp'], format='ISO8601')
df['serverTimestamp'] = pd.to_datetime(df['serverTimestamp'], format='ISO8601')
df['deviceTimestamp'] = pd.to_datetime(df['deviceTimestamp'], format='ISO8601')

# %%
latlong_factor = float(1e7)

df['longitude'] = df['longitudeE7'].astype('float64') / latlong_factor
df['latitude'] = df['latitudeE7'].astype('float64') / latlong_factor

df.to_csv('Records.csv')

df

# %%
source = list(df['source'].unique())
deviceTag = list(df['deviceTag'].unique())
platformType = list(df['platformType'].unique())
batteryCharging = list(df['batteryCharging'].unique())
formFactor = list(df['formFactor'].unique())
heading = list(df['heading'].unique())

print(source)
print(deviceTag)
print(platformType)
print(batteryCharging)
print(formFactor)
print(heading)


# %%
df["coordinates"] = list(zip(df.longitude, df.latitude))
df["coordinates"] = df["coordinates"].apply(Point)

df

# %%
gdf = gpd.GeoDataFrame(df, geometry="coordinates")
gdf

# %%
# state_df = gpd.read_file("https://datascience.quantecon.org/assets/data/cb_2016_us_state_5m.zip")
# state_df.head()

# %%
# fig, gax = plt.subplots(figsize=(10, 10))
# state_df.query("NAME == 'Wisconsin'").plot(ax=gax, edgecolor="black", color="white")
# plt.show()

# %%
# geodatasets.data

# %%
# print(geodatasets.get_url("naturalearth.land"))
# print(geodatasets.get_path("naturalearth.land"))

# naturalearth = gpd.read_file(geodatasets.get_path("naturalearth.land"))
# naturalearth

# %%
# gpd.datasets.available

# %%
# naturalearth.plot()
# from mpl_toolkits.axes_grid1 import make_axes_locatable
# fig, ax = plt.subplots(1, 1)
# divider = make_axes_locatable(ax)
# cax = divider.append_axes("bottom", size="5%", pad=0.1)

# fig, ax = plt.subplots()
# naturalearth.plot(ax=ax, color='white', edgecolor='black')

# %%
