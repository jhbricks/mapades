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
def mapa (area,arq,ind,scheme,k,cmap,fields,title):
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
                  draw_control=False,
                  measure_control=False,
                  fullscreen_control=False,
                  attribution_control=True)
  
  m.add_data(gdf,
	           column=ind,
             scheme=scheme,
             k=k,
             cmap=cmap,
             fields=fields,
             legend_title=title,
             legend_position='Bottomright',
             layer_name=title,
	           zoom_to_layer=True)

  m.to_streamlit()


