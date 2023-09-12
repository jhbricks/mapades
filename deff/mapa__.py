import streamlit as st
from streamlit_folium import folium_static
import folium
import leafmap
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
import numpy as np
import os
import streamlit.components.v1 as components

########################ARQUIVOS CSV E GEOJSON
contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"
renda = "./dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"
PR = "./dados/geojson/PR.geojson"
NTC =  "./dados/geojson/NTC.geojson"

#######################DICIONÁRIO DEF MAPA
#area = 'PR' ou 'NTC'
#arq = arquivo csv, ex: contexto
#ind = indicador conforme está no arquivo csv, ex: 'População'
#scheme = classificação, lista no leafmap, ex: 'FisherJenks'
#k = número de classes
#cmap = paleta de cores, lista no leafmap, ex: 'Oranges'
#fields = variaveis que aparecem no popup, ex: ['Município','População']
#title = título do mapa e da legenda

@st.cache_data
def mapa1 (area,arq,ind,scheme,k,cmap,fields,title):
######encaminha o geojson da area
  if area == 'PR':
    arq_g = "./dados/geojson/PR.geojson"
  else:
    area = 'NTC'
    arq_g = "./dados/geojson/NTC.geojson"

#######MERGE geojson e csv
  arq_csv = pd.read_csv(arq)
  arq_geojson = gpd.read_file(arq_g)
  gdf = arq_geojson.merge(arq_csv, on="Município")
  

#######LAT E LON CENTRAIS
  ponto_central = arq_geojson.geometry.centroid
  lat = ponto_central.iloc[0].y
  lon = ponto_central.iloc[0].x
    
  if not isinstance(gdf,gpd.GeoDataFrame):
    print("O arquivo não é um GeoDataFrame")
    exit()
##########################MAPA
########MAPA INICIAL
  m = leafmap.Map(center=[lat,lon], 
                  #height="400px", width="800px",
                  draw_control=False,
                  measure_control=False,
                  fullscreen_control=False,
                  attribution_control=True)
  
#######ADICIONAR O MERGE GDF
  #if area == PR:
  #m.zoom_to_bounds([-47.98, -22.44, -54.67, -26.80))
  #else:
  #  m.zoom_to_bounds((-47.87,-24.96,-48.54, -25.85))

  style = {
      "stroke": True,
      "color": "#000000",
      "weight": 2,
      "opacity": 1}
  hover_style = {"fillOpacity": 0.7}



  m.add_data(gdf,
	           column=ind,
             scheme=scheme,
             k=k,
             cmap=cmap,
             fields=fields,
             legend_title=title,
             legend_position='Bottomright',
             layer_name=title,
	     zoom_to_layer=True,
             style=style,
             hover_style=hover_style)
########VALORES DE MX E MN DAS VARIAVEIS
#  max_value = data[ind].max()
#  min_value = data[ind].min()
#  max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
#  min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]
#####ADICIONAR MX E MN NO MAPA
#  folium.Marker([data.loc[data[ind] == max_value, "Y"].iloc[0],
#                 data.loc[data[ind] == max_value, "X"].iloc[0]],
#                popup=f"Maior valor: {max_value}<br>{max_municipio}",
#                icon=folium.Icon(color="darkpurple", icon="arrow-up"),
#               ).add_to(m) 
#  folium.Marker([data.loc[data[ind] == min_value, "Y"].iloc[0],
#	         data.loc[data[ind] == min_value, "X"].iloc[0]],
#                popup=f"Menor valor: {min_value}<br>{min_municipio}",
#                icon=folium.Icon(color="purple", icon="arrow-down"),
#               ).add_to(m)
#########ADICIONAR NO STREAMLIT
 # m.zoom_to_bounds()


#D
#N
#E
#S
  #m.zoom_to_bounds([[-26.80, -54.67],[ -22.44, -47.98]])
  
 

  #bounds = [[-26.80, -54.67], [-22.44,-47.98]]
  #st_map_bounds(m, bounds)
  bounds = gdf.total_bounds
  m.zoom_to_bounds(bounds)
  m.to_streamlit()


