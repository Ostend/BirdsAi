import folium
import json
import pandas as pd
from data import area_by_state
#create a map object
#location will be the center focal point [lat, long]
#m.save() generates the html file that has all the leaflet dependencies to display the map
global tooltip 
tooltip = 'Click for more info'
m = folium.Map(location=[-3.117034, -60.025780], zoom_start=6) 
#create custome icons:
logoIcon = folium.features.CustomIcon('images/smartphone.png', icon_size=[50,50])
#Geojson Data
overlay = '../../Data/overlay.json'
brazil_map = '../../Data/brazil.json'
#create markers on the map
#takes position
""" folium.Marker(
    [-1.969946453104092, -58.971133], 
    popup='<i>Farm One</i>', 
    tooltip=tooltip,
    icon=folium.Icon(color='green')).add_to(m),
folium.Marker(
    [-1.5043429772981733, -55.991641546988774], 
    popup='<i>Farm two</i>', 
    tooltip=tooltip, 
    icon=folium.Icon(icon='leaf', color='green')).add_to(m),
folium.Marker(
[-3.9973642869202703, -55.68841861413597], 
popup='<i>Farm three</i>', 
tooltip=tooltip, 
icon=logoIcon).add_to(m) """


#using Geojson, folium has a method to use it!
#folium.GeoJson(brazil_map, name='Brazil').add_to(m) 

#choropleth
#setting up the Environment
#using the variable brazil_map for coordinates which is the json file
deforest_areakm = area_by_state #import the areakm deforested per state data


""" m.choropleth(
    geo_data=brazil_map, 
    name='choropleth', 
    data=deforest_areakm,
    columns=['State', 'Area_km'], 
    key_on='properties.sigla',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Areakm Deforested per State'

) """
folium.Choropleth(
    geo_data=brazil_map, 
    name='choropleth', 
    data=deforest_areakm,
    columns=['State', 'Area_km'], 
    key_on='properties.sigla',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Areakm Deforested per State',
    nan_fill_color="white",
    highlight=True

).add_to(m)

folium.LayerControl().add_to(m)
m.save('map.html')

