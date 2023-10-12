import streamlit as st
from streamlit_extras.colored_header import colored_header
import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go
#from deff.mapa__ import mapa
from deff.calculos__ import mx_mn
from deff.calculos__ import conta
#from deff.map import zoom_to_bounds
from deff.map import mapa
from deff.map import grafico
from deff.teste_gvf import create_map
from deff.teste_gvf import mapagvf
from deff.mapa__ import mapa1
import leafmap

contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"
renda = "./dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"
PR = "./dados/geojson/PR.geojson"
NTC =  "./dados/geojson/NTC.geojson"

st.set_page_config(layout="wide")


NTC = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson'
m = leafmap.Map(center=[-51.8, -24.7])
style = {"color": "#000000","fillOpacity": 0,"clickable": False}
m.add_geojson(NTC, style = {"color": "#000000","fillOpacity": 0,"clickable": False})
m.to_streamlit()

########################ARQUIVOS CSV E GEOJSON
contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"
renda = "./dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"

arq_g = "./dados/geojson/PR.geojson"

arq_csv = pd.read_csv(pop)
arq_geojson = gpd.read_file(arq_g)
data = arq_geojson.merge(arq_csv, on="Município")


ponto_central = arq_geojson.geometry.centroid
lat = ponto_central.iloc[0].y
lon = ponto_central.iloc[0].x
    
if not isinstance(data,gpd.GeoDataFrame):
    print("O arquivo não é um GeoDataFrame")
    exit()

##########################MAPA
########MAPA INICIAL
m = leafmap.Map(center=[lat,lon],
                draw_control=False,
                measure_control=False,
                fullscreen_control=False,
                attribution_control=True)
  
m.add_data(data = data,
           column='População',
           scheme='FisherJenks',
           k=4,
           cmap='Reds',
           fields=['Município','População'],
           legend_position='bottomleft',
           layer_name='A',
           )
m.add_geojson(NTC, style = {"color": "#000000","fillOpacity": 0,"clickable": False})

########VALORES DE MX E MN DAS VARIAVEIS
#max_value = data[ind].max()
#min_value = data[ind].min()
#max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
#min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]
#####ADICIONAR MX E MN NO MAPA
#folium.Marker([data.loc[data[ind] == max_value, "Y"].iloc[0],
#               data.loc[data[ind] == max_value, "X"].iloc[0]],
#               popup=f"Maior valor: {max_value}<br>{max_municipio}",
#               icon=folium.Icon(color="darkpurple", icon="arrow-up"),
#              ).add_to(m) 
#folium.Marker([data.loc[data[ind] == min_value, "Y"].iloc[0],
#               data.loc[data[ind] == min_value, "X"].iloc[0]],
#               popup=f"Menor valor: {min_value}<br>{min_municipio}",
#               icon=folium.Icon(color="purple", icon="arrow-down"),
#              ).add_to(m)
#########ADICIONAR NO STREAMLIT


m.to_streamlit()