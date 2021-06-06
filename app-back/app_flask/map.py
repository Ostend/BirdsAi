import folium
import json
import pandas as pd
from data import area_by_state, amz_state
#create a map object
#location will be the center focal point [lat, long]
#m.save() generates the html file that has all the leaflet dependencies to display the map
global tooltip 
tooltip = 'Click for more info'
m = folium.Map(location=[-3.117034, -60.025780], zoom_start=5) 
#create custome icons:
logoIcon = folium.features.CustomIcon('images/smartphone.png', icon_size=[50,50])
#Geojson Data
b_geo = '../../Data/brazil-states.geojson'
brazil_map = '../../Data/brazil.json'
prodes_map = '../../Data/prodes.geojson'
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

#? Interactive Cholorpleth Map 

choropleth = folium.Choropleth(
    geo_data=b_geo, 
    name='choropleth', 
    data=amz_state,
    columns=['State', 'Area_km'], 
    key_on='properties.sigla',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Areakm Deforested per State',
    nan_fill_color="white",
    highlight=True
    ).add_to(m)

""" choropleth.geojson.add_child(
    folium.features.GeoJson(['State'])
)
 """
style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1}
#Have to get the polygone of each state and add it to the dataframe geometry.coordinates

popup_style = folium.features.GeoJson(
    amz_state,
    style_function=style_function,
    control=False,
    highlight_function=highlight_function,
    tooltip = folium.features.GeoJsonTooltip(
        fields=['State', 'Area_km'],
        aliases=['State: ', 'Total Area_km deforested: '],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
    )
)
m.add_child(popup_style) 
folium.LayerControl().add_to(m)

m.save('templates/map.html')

#* Starting a new map with the Prodes data
# todo: prodes data format the map!

#mprodes = folium.Map(location=[-3.117034, -60.025780], zoom_start=5) 
#* another way of making a map
#* using this website to pick out template: https://leaflet-extras.github.io/leaflet-providers/preview/
prodes_m = folium.Map(location=[-3.117034, -60.025780],
                zoom_start=2.5,
                tiles='https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}',
                attr='My Data Attribution')

prodes_url = 'https://services2.arcgis.com/g8WusZB13b9OegfU/arcgis/rest/services/PRODES_Deforestation_in_Amazonia/FeatureServer/0/query?where=1+%3D+1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=true&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token='

mining_url='http://gis-gfw.wri.org/arcgis/rest/services/country_data/south_america/MapServer/2/query?where=1+%3D+1&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&having=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&queryByDistance=&returnExtentOnly=false&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&f=geojson'
style1 = {'fillColor': '#228B22', 'color': '#228B22'}
folium.GeoJson(
    prodes_url,
    name='prodes_map'
).add_to(prodes_m) 
""" folium.GeoJson(
    mining_url,
    name='mining_url'
).add_to(prodes_m)
prodes_m.save('templates/prodesmap.html') """