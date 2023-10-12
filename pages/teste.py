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
     