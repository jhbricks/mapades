import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import leafmap.foliumap as leafmap
import pandas as pd

contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"
renda = "./dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"

def mapa (area, arq, ind, scheme, k, cmap, fields, title):

  if area == 'PR':
       arq_g= "./dados/geojson/PR.geojson"
       min_zoom= 7
       max_zoom=13
  else:
       arq_g = "./dados/geojson/NTC.geojson"
  
  arq_csv = pd.read_csv(arq)
  arq_geojson = gpd.read_file(arq_g)
  data = arq_geojson.merge(arq_csv, on="Município")

  #Lat, Lon centrais
  ponto_central = arq_geojson.geometry.centroid
  lat = ponto_central.iloc[0].y
  lon = ponto_central.iloc[0].x
  
  if not isinstance(data, gpd.GeoDataFrame):
    print("O arquivo não é um GeoDataFrame")
    exit()
                #Mapa
  m = leafmap.Map(center=[lat, lon],
                  min_zoom=7,
                  max_zoom=13,
                  width=800,
                  height=500,
                  draw_control=False,
                  measure_control=False,
                  fullscreen_control=False,
                  attribution_control=True)
                
  m.add_data(data=data,
             column=ind,
             scheme=scheme,
             k=k,
             cmap=cmap,
             fields=fields,
             legend_title=title,
             legend_position= 'Bottomright',
             layer_name=title,
             style={"stroke": True, "color": "#000000", "weight": 1, "fillOpacity": 1})
    
  max_value = data[ind].max()
  min_value = data[ind].min()
  max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
  min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]

  folium.Marker([data.loc[data[ind] == max_value, "Y"].iloc[0],
                 data.loc[data[ind] == max_value, "X"].iloc[0]],
                popup=f"Maior valor: {max_value}<br>{max_municipio}",
                icon=folium.Icon(color="green", icon="arrow-up"),
               ).add_to(m) 
  folium.Marker([data.loc[data[ind] == min_value, "Y"].iloc[0],
                 data.loc[data[ind] == min_value, "X"].iloc[0]],
                popup=f"Menor valor: {min_value}<br>{min_municipio}",
                icon=folium.Icon(color="red", icon="arrow-down"),
               ).add_to(m)
  m.to_streamlit()
  
  return m 


def mx_mn (area,arq,ind,tipo,unidade=None) :

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
    
    if tipo == "md_int":
      media = int(data[ind].mean())
    elif tipo == "soma":
      media = data[ind].sum()
    else:
      media = data[ind].mean().round(2)
            
    st.markdown("<h3><font size='+5'> Municípios com o <font size='+5' color='green'>maior</font> e <font size='+5' color='red'>menor</font> <font size='+5'> valor:</font></h3>", unsafe_allow_html=True)
    #st.markdown(f"<p style='line-height: 0.7;'><font size='+10' color='green'>{arrow_u}</font> <font size='+5'>{max_str} = {ind_mx}</font></p>", unsafe_allow_html=True)
    #st.markdown(f"<p style='line-height: 0.5;'><font size='+10' color='red'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn}</font></p>", unsafe_allow_html=True)
    #st.markdown(f"<h3><font size='+5'> Média do {column_name} no Paraná:</font></h3>", unsafe_allow_html=True)
    if unidade:
      st.markdown(f"""<p style='line-height: 0.7;'><font size='+10' color='green'>{arrow_u}</font> <font size='+5'>{max_str} = {ind_mx} {unidade}</font>  
      <font size='+10' color='red'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn} {unidade}</font></p>""", unsafe_allow_html=True)
      #st.markdown(f"<p style='line-height: 0.5;'><font size='+10' color='red'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn} {unidade}</font></p>", unsafe_allow_html=True)
      st.markdown(f"<h3><font size='+5'> Média do {column_name} no Paraná:</font></h3>", unsafe_allow_html=True)  
      st.markdown(f"<p style='line-height: 0.2; font-weight: bold; font-size: 1.7em;'>{media} {unidade}</p>", unsafe_allow_html=True)
    else:
      st.markdown(f"<p style='line-height: 0.7;'><font size='+10' color='green'>{arrow_u}</font> <font size='+5'>{max_str} = {ind_mx}</font></p>", unsafe_allow_html=True)
      st.markdown(f"<p style='line-height: 0.5;'><font size='+10' color='red'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn}</font></p>", unsafe_allow_html=True)
      st.markdown(f"<h3><font size='+5'> Média do {column_name} no Paraná:</font></h3>", unsafe_allow_html=True)  
      st.markdown(f"<p style='line-height: 0.2; font-weight: bold; font-size: 1.7em;'>{media}</p>", unsafe_allow_html=True)
