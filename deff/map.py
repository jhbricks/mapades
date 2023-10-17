import streamlit as st
from streamlit_folium import folium_static
import folium
import leafmap
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
import numpy as np
import os
import fiona
import plotly.graph_objects as go


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
  data = arq_geojson.merge(arq_csv, on="Município")

#######LAT E LON CENTRAIS
  #ponto_central = arq_geojson.geometry.centroid
  #lat = ponto_central.iloc[0].y
  #lon = ponto_central.iloc[0].x
    
  lon, lat = leafmap.gdf_centroid(data)

  #if not isinstance(data,gpd.GeoDataFrame):
  #  print("O arquivo não é um GeoDataFrame")
  #  exit()

  
##########################MAPA
########MAPA INICIAL
#  m = leafmap.Map(center=(lat,lon), 
#                  draw_control=False,
#                  measure_control=False,
#                  fullscreen_control=False,
#                  attribution_control=True)
  

#  m.add_data(data = data,
#	           column=ind,
#             scheme=scheme,
#             k=k,
#             cmap=cmap,
#             fields=fields,
#             legend_title=title,
#             legend_position='Bottomright',
#             layer_name=title,
#             style={"stroke": True,
#                    "color": "#000000"})
  
  

  
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
#########ADICIONAR NO 
  #width = 950
  #height = 600

  m = leafmap.Map(center=(lat, lon))
  m.add_gdf(data, layer_name=title)
  # m.add_vector(file_path, layer_name=layer_name)


  st.pydeck_chart(m)
  #m.to_streamlit()



def grafico (arq,ind):
  df = pd.read_csv(arq)
  highest = df.nlargest(3, 'Renda Média da População (R$ mil)')
  lowest = df.nsmallest(3, 'Renda Média da População (R$ mil)')
  fig = go.Figure()
  colors = {'Maiores valores': '#5a386a', 'Menores valores': '#cd50b5'}

  fig.add_trace(go.Bar(x=highest['Município'],
                       y=highest[ind],
                       name='Maiores valores',
                       marker=dict(color=colors['Maiores valores'])
                       ))
  fig.add_trace(go.Bar(x=lowest['Município'],
                        y=lowest[ind],
                        name='Menores valores',
                        marker=dict(color=colors['Menores valores']) 
                        ))
  st.plotly_chart(fig, use_container_width=True)


