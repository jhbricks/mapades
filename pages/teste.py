import streamlit as st
from streamlit_extras.colored_header import colored_header
import folium
import leafmap
import leafmap.foliumap as leafmap
import geopandas as gpd
from deff.mapa import mapa
from deff.mapa import grafico
from deff.calculos import conta

op = st.radio("Selecione um indicador:",("A","B", "C", "D", "E", "F", "G"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"

if op == "A":
      mapa('PR',contexto,'População','FisherJenks',5,'Wistia', ['Município','População'],'População residente (hab)')
