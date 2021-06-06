import pandas as pd
from data import area_by_state
import json
from pandas.io.json import json_normalize

#trying to get the coordinates of the states
b_geo = '../../Data/brazil-states.geojson'
""" with open(b_geo) as f:
    geo_data=json.load(f) """

#print(geo_data.keys()) #returns: type and features

#try to turn the features key into a series?
df = pd.read_json(b_geo)

geo_series = df['features'].apply(pd.Series)
#print(type(geo_series))
#to be able to extract the json data, break these two down into their own dataframes, then concate them togther based on their index. 
geometry_df = geo_series['geometry'].apply(pd.Series)
properties_df = geo_series['properties'].apply(pd.Series)
frames = [properties_df, geometry_df]
geo_prop_df = pd.concat(frames, axis=1)

#now clean it, only want state and coordinates
geo_prop_df.drop(columns=['id', 'name', 'updated_at', 'type', 'regiao_id', 'codigo_ibg', 'cartodb_id', 'created_at'], inplace=True)

geo_prop_df.rename(columns={'sigla':'State'},inplace=True)
""" print(type(geo_prop_df)) """
#need to use the unique states in the df to go through the geojson file, to get the coordinates of the 9 states. coordinates located under geometry.coordinates. 
#properties.sigla where the state abbv. is
area_km_coordinates_df = pd.merge(geo_prop_df, area_by_state, on='State')
#print(area_km_coordinates_df
geo_coord_series = area_km_coordinates_df['coordinates'].apply(pd.Series)
""" print(geo_coord_series) """
