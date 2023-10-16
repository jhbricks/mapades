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
    


import folium
import pandas

state_geo = ('https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson')
state_data = pandas.read_csv(
    "./dados/csv/contexto.csv"
)

m = folium.Map(zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["Município", "População"],
    key_on="Município",
    color='black',
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
).add_to(m)

folium.LayerControl().add_to(m)

m
