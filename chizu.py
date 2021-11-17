import folium 
import pandas 

locations = pandas.read_csv("Volcanoes.txt")
lat = list(locations["LAT"])
lon = list(locations["LON"])
el = list(locations["ELEV"])

chizu = folium.Map()
fg = folium.FeatureGroup(name="My Map")

def color_definer(el) :
     if el < 1000 :
          return "green"
     elif el< 2000 :
          return "purple"
     elif el < 3000 :
          return "orange"
     else :
          return "red"
     
for lt,ln,el in zip(lat,lon,el) :
     fg.add_child(folium.CircleMarker([lt, ln], radius =12, popup= "Hi I am volcano. My elevation is " + str(el) , fill_color = color_definer(el), color= "black", fill = True, fill_opacity=0.7 ))


chizu.add_child(fg)
chizu.save("chizu5.html")
