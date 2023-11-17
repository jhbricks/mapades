import streamlit as st
from streamlit_folium import folium_static
from streamlit_extras.colored_header import colored_header
import folium
import leafmap
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from deff.mapa import mapa
from deff.mapa import grafico
from deff.calculos import conta

#Selecionar a área 
st.markdown("<h3><font size='7'  color='red'>Contextualização</font></font></h3>", unsafe_allow_html=True)
#Selecionar a área [Radio horizontal]
area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central de Curitiba"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#####Arquivos 
contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"
PR = "./dados/geojson/PR.geojson"
NTC = "./dados/geojson/NTC.geojson"

if area == "Paraná":
  op = st.radio("Selecione um indicador:",
                ("População residente", "Densidade demográfica", "Grau de urbanização", "População feminina", "População preta/parda", "Razão de dependência"))
  st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

  if op == "População residente":
    colored_header(label="População residente",
                   description="População residente do Paraná",
                   color_name="red-70",)
    #mapa (area, arq, ind, scheme, k, cmap, fields, title)
    c1,c2 = st.columns([2,0.7])
    with c1:

      arq_csv = pd.read_csv(contexto)
      arq_geojson = gpd.read_file(PR)
      data = arq_geojson.merge(arq_csv, on="Município")

#######LAT E LON CENTRAIS
      ponto_central = arq_geojson.geometry.centroid
      lat = ponto_central.iloc[0].y
      lon = ponto_central.iloc[0].x
    
      if not isinstance(data,gpd.GeoDataFrame):
        print("O arquivo não é um GeoDataFrame")
        exit()

      style = {"color":"#000000","weight":1, "fillOpacity":0}
##########################MAPA
########MAPA INICIAL
      m = leafmap.Map(center=[lat,lon],draw_control=False,measure_control=False,fullscreen_control=False,attribution_control=True)
      m.add_basemap("CartoDB.DarkMatter")  

      m.add_data(data = data,column='Grau de Urbanização (%)',scheme='FisherJenks',k=4,cmap='winter_r',fields=['Município','Grau de Urbanização (%)'],legend_title='Grau de urbanização %',layer_name='Grau de urbanização')
      folium.GeoJson(data,name = 'Paraná - urb',style_function=lambda feature: style,tooltip=folium.GeoJsonTooltip(fields=['Município','Grau de Urbanização (%)'])).add_to(m)
  
      m.add_data(data = data,column= 'Densidade Demográfica (hab/km²)',scheme='FisherJenks',k=5,cmap='inferno_r',fields=['Município', 'Densidade Demográfica (hab/km²)'],legend_title='Densidade demográfica',layer_name='Densidade demográfica')
      folium.GeoJson(data,name = 'Paraná - hab/km²',style_function=lambda feature: style,tooltip=folium.GeoJsonTooltip(fields=['Município', 'Densidade Demográfica (hab/km²)'])).add_to(m)

      m.add_data(data = data,column='População',scheme='FisherJenks',k=5,cmap='copper_r',fields=['Município','População'],legend_title='População residente (hab)',layer_name='População residente')
      folium.GeoJson(data,name = 'Paraná',style_function=lambda feature: style,tooltip=folium.GeoJsonTooltip(fields=['Município','População'])).add_to(m)


########VALORES DE MX E MN DAS VARIAVEIS
      max_value = data['População'].max()
      min_value = data['População'].min()
      max_municipio = data.loc[data['População'] == max_value, "Município"].iloc[0]
      min_municipio = data.loc[data['População'] == min_value, "Município"].iloc[0]
#####ADICIONAR MX E MN NO MAPA
      folium.Marker([data.loc[data['População'] == max_value, "Y"].iloc[0],
                     data.loc[data['População'] == max_value, "X"].iloc[0]],
                    popup=f"Maior valor: {max_value}<br>{max_municipio}",
                    icon=folium.Icon(color="darkpurple", icon="arrow-up"),
                   ).add_to(m) 
      folium.Marker([data.loc[data['População'] == min_value, "Y"].iloc[0],
        	         data.loc[data['População'] == min_value, "X"].iloc[0]],
                     popup=f"Menor valor: {min_value}<br>{min_municipio}",
                     icon=folium.Icon(color="purple", icon="arrow-down"),
                    ).add_to(m)
#########ADICIONAR NO STREAMLIT
      m.to_streamlit()
      st.markdown("""**Ano-base:** 2021  
                  **Fonte(s):** IBGE  
                  **Fórmula:** População total por município  
                  **Observações:** Prévia da população por município do Censo Demográfico 2022 do IBGE.
                  """)   

    with c2:
      st.markdown("**População residente estimada pelo Instituto Brasileiro de Geografia e Estatística (IBGE) para o ano de 2021.**")  
      conta ('PR',contexto,'População',2021,'População total','soma','habitantes')
      grafico('PR',contexto,'População','Habitantes')
      
  