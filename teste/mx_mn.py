import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import leafmap.foliumap as leafmap
import pandas as pd

def mx_mn (area,ind,tipo) :

    if area == 'PR':
       arq_g= "./dados/geojson/PR.geojson"
    else:
       arq_g = "./dados/geojson/NTC.geojson"

    arq_csv = pd.read_csv(arq)
    arq_geojson = gpd.read_file(arq_g)
    data = arq_geojson.merge(arq_csv, on="Município")
  
    max_value = data[ind].max()
    min_value = data[ind].min()
    max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
    min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]

    arrow_d = '\U0001F82B'  
    arrow_u = '\U0001F829'  
    min_str = f"{min_municipio}"
    max_str = f"{max_municipio}"
    ind_mn = f"{min_value}"
    ind_mx = f"{max_value}"
    column_name = ind
    
    if tipo == "inteiro":
      media = int(data[ind].mean())
    else:
      media = data[ind].mean().round(2)
            
    st.markdown("<h3><font size='+5'> Municípios com o <font size='+5' color='green'>maior</font> e <font size='+5' color='red'>menor</font> <font size='+5'> valor:</font></h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='line-height: 0.7;'><font size='+10' color='green'>{arrow_u}</font> <font size='+5'>{max_str} = {ind_mx}</font></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='line-height: 0.5;'><font size='+10' color='red'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn}</font></p>", unsafe_allow_html=True)
    st.markdown(f"<h3><font size='+5'> Média do {column_name} no Paraná:</font></h3>", unsafe_allow_html=True)
    if unidade:
      st.markdown(f"<p style='line-height: 0.2; font-weight: bold; font-size: 1.7em;'>{media} {unidade}</p>", unsafe_allow_html=True)
    else:
      st.markdown(f"<p style='line-height: 0.2; font-weight: bold; font-size: 1.7em;'>{media}</p>", unsafe_allow_html=True)
