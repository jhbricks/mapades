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

#arq_csv = pd.read_csv(pop)
#arq_geojson = gpd.read_file(arq_g)
#data = arq_geojson.merge(arq_csv, on="Município")


#ponto_central = arq_geojson.geometry.centroid
#lat = ponto_central.iloc[0].y
#lon = ponto_central.iloc[0].x
    
import pandas as pd
import geopandas as gpd
import mapclassify
import folium


csva = pd.read_csv("./dados/csv/contexto.csv")
geoa = gpd.read_file("./dados/geojson/PR.geojson")

mergeda = geoa.merge(csva, on="Município")

#Cálculo
#data["Densidade Demográfica"] = (data["População"] / data["AREA"]).round().astype(int)

#Limites e Centralização da camada
boundss = popa.geometry.bounds
latitude_centrals = (boundss.miny.mean() + boundss.maxy.mean()) / 2
longitude_centrals = (boundss.minx.mean() + boundss.maxx.mean()) / 2

m = folium.Map(location=[latitude_centrals, longitude_centrals])


#População
folium.Choropleth(
    geo_data= popa,
    name='População',
    data=popa,
    columns=['Municípios', 'População'],
    key_on='feature.properties.Municípios',
    fill_color= 'YlOrRd',
    legend_name='Legenda',
).add_to(m)

#'BuGn', 'BuPu', 'GnBu', 'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 'RdPu','YlGn', 'YlGnBu', 'YlOrBr', and 'YlOrRd'

#Hover
folium.GeoJson(
    popa,
    style_function=lambda x: {'fillColor': 'transparent', 'color': 'transparent'},
    tooltip=folium.features.GeoJsonTooltip(
        fields=["Municípios", "População"],
        aliases=["Município", "População"],
        labels=True,
        sticky=False
    ),
    name='Legenda'
).add_to(m)

# Adicionar controle de camadas ao mapa
folium.LayerControl().add_to(m)

# Ajustar o zoom e a localização para preencher a tela
m.fit_bounds([[boundss.miny.min(), boundss.minx.min()], [boundss.maxy.max(), boundss.maxx.max()]])

m.to_streamlit()

