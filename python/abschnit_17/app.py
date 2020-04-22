import folium

map = folium.Map([50,8.6], zoom_start=10, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

map.add_child(folium.CircleMarker([50,8.6], 10))
map.add_child(folium.Marker([50, 8.7], popup="My Location", icon=folium.Icon(color='green')))
map.save("Map1.html")
