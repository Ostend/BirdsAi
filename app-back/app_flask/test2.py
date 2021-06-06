import pandas as pd 
import json
import geopandas as gpd
from data import area_by_state
#todo: test space, for the goal of extracting the json coordinates for each state, so I can use the folium method for a pop up to appear on the chorotheum map. 
#? first I will attempt to extract the data using json loads
#? JSON -> Python conversions = object - dict, array - list, string - str, number - int, numer - float, true - True, flase - False, null - None. 


b_geo = '../../Data/brazil-states.geojson'

amz = gpd.read_file(b_geo)
#print(amz.columns)
#? columns = ['id', 'name', 'sigla', 'regiao_id', 'codigo_ibg', 'cartodb_id','created_at', 'updated_at', 'geometry']
#? Do not need: regiao_id', 'codigo_ibg', 'cartodb_id','created_at', 'updated_at'
amz = amz[['sigla', 'geometry']]
#print(amz.head())
#print(len(amz))
#? Now merge the dataframes together on 'State'
#?rename the 'sigla' column to 'State' to make sure merging is successful
amz.rename(columns={'sigla':'State'},inplace=True)
amz_state = amz.merge(area_by_state, on='State')



print(amz_state)

# *this is my main methid
# ! problems
#  ? what should 
#  todo: to do!
