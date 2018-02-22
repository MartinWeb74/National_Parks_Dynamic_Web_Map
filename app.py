import folium
import pandas

# initiate a map, set location and zoom level
map = folium.Map(location=[39.002,-97.503], zoom_start=4)

# read data from file
data = pandas.read_csv("parks.txt")
# print(data.columns)
name = list(data["place"])
lat = list(data["lat"])
lon = list(data["lon"])

# create a feature group
fg = folium.FeatureGroup(name="markers")
# add markers to the feature group
# locations = [[35,-116],[34,-117],[36,-115]]

# iterating trhu 2 list simultaneosly
for lt, ln, nm in zip(lat, lon, name):
    fg.add_child(folium.Marker(location=[lt, ln], popup=nm, icon=folium.Icon(color="blue")))


# fg.add_child( folium.Marker( location=[35,-116], popup="Im a marker on a map", icon=folium.Icon(color="green") ) )
# fg.add_child( folium.Marker( location=[34,-117], popup="Im a marker on a map too", icon=folium.Icon(color="blue") ) )
# add the feature group to the map
map.add_child(fg)

# save the map
map.save("map1.html")
