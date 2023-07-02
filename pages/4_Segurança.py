import streamlit as st
from streamlit_extras.colored_header import colored_header
from teste.teste import mapa
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import leafmap.foliumap as leafmap
import pandas as pd

contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"
renda = "./dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"

colored_header(label=":orange[Indicadores de Segurança: em breve ⌛]", description="   ", color_name="orange-70",)

mapa('PR', 'pop', 'População', 'FisherJenks', 5, 'Oranges', ['Municípios','População'], 'AAA')
