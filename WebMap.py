import folium

myMap = folium.Map(location = [34.651834, 73.050557], zoom_start = 20)

myFG = folium.FeatureGroup(name = "Points")
myFG.add_child(folium.Marker(location = [34.651810, 73.050738], popup = "This is my house.", icon = folium.Icon(color = 'blue')))
myMap.add_child(myFG)

myMap.save("home.html")

