import streamlit as st
from streamlit_folium import folium_static
import folium
import leafmap
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
import numpy as np

########################ARQUIVOS CSV E GEOJSON
contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"
renda = "./dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"

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
##########define a área (geojson)    
    if area == 'PR':
        arq_g = "./dados/geojson/PR.geojson"
    else:
        area = 'NTC'
        arq_g = "./dados/geojson/NTC.geojson"

##########merge geojson + csv -> coluna em comum = 'Município'
    arq_csv = pd.read_csv(arq)
    arq_geojson = gpd.read_file(arq_g)
    data = arq_geojson.merge(arq_csv, on="Município")

##########Define as coordenadas centrais - LAT E LON CENTRAIS
    ponto_central = arq_geojson.geometry.centroid
    lat = ponto_central.iloc[0].y
    lon = ponto_central.iloc[0].x

##########Para não dar erro no mapa
    if not isinstance(data,gpd.GeoDataFrame):
        print("O arquivo não é um GeoDataFrame")
        exit()

##########MAPA
    m = leafmap.Map(center=[lat,lon],
                    draw_control=False,
                    measure_control=False,
                    fullscreen_control=False,
                    attribution_control=True)

####zoom
    bounds = leafmap.gdf_bounds(data)
    m.fit_bounds(bounds)

####adicionar o gdf (merge)
    m.add_data(data = data,
               column=ind,
               scheme=scheme,
               k=k,
               cmap=cmap,
               fields=fields,
               legend_title=title,
               legend_position='Bottomright',
               layer_name=title,
               style={"stroke": True, "color": "#000000", "weight": 1, "fillOpacity": 1}
               )
####define os valores mx e mn das variáveis
    max_value = data[ind].max()
    min_value = data[ind].min()
    max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
    min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]
####adiciona mx e mn no mapa
    folium.Marker([data.loc[data[ind] == max_value, "Y"].iloc[0],
                   data.loc[data[ind] == max_value, "X"].iloc[0]],
                   popup=f"Maior valor: {max_value}<br>{max_municipio}",
                   icon=folium.Icon(color="darkpurple", icon="arrow-up"),
                   ).add_to(m) 
    folium.Marker([data.loc[data[ind] == min_value, "Y"].iloc[0],
	              data.loc[data[ind] == min_value, "X"].iloc[0]],
                  popup=f"Menor valor: {min_value}<br>{min_municipio}",
                  icon=folium.Icon(color="purple", icon="arrow-down"),
                  ).add_to(m)

####mapa para o streamlit
    m.to_streamlit()


