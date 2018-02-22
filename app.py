import folium
import pandas

# initiate a map, set location and zoom level
map = folium.Map(location=[39.002,-97.503], zoom_start=4)

# read data from file
data = pandas.read_csv("parks.txt")

# split columns into Python lists
name = list(data["place"])
lat = list(data["lat"])
lon = list(data["lon"])

# create a feature group
fg = folium.FeatureGroup(name="markers")

# iterating trhu 3 list simultaneously
for lt, ln, nm in zip(lat, lon, name):
    fg.add_child(folium.Marker(location=[lt, ln], popup=nm, icon=folium.Icon(color="blue")))

# add the feature group to the map
map.add_child(fg)

# save the map to an html file, if file exist, it will be overridden
map.save("map1.html")
