import streamlit as st
from streamlit_folium import folium_static
import folium
import leafmap
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
import numpy as np
import plotly.graph_objects as go



########################ARQUIVOS CSV E GEOJSON
#contexto = "./dados/csv/contexto.csv"
#pop = "./dados/csv/pop_2021.csv"
#renda = "./dados/csv/renda.csv"
#riqueza = "./dados/csv/riqueza.csv"

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
def mapa3(area):
    if area == 'PR':
        arq_g = "./dados/geojson/PR.geojson"
    elif area == 'NTC':
        arq_g = "./dados/geojson/NTC.geojson"
    else:
        arq_g = area

    style = {"color": "#000000", "weight": 1, "fillOpacity": 0}

    arq_csv = pd.read_csv(arq_g)
    arq_geojson = gpd.read_file(arq_g)

    ponto_central = arq_geojson.geometry.centroid
    lat = ponto_central.iloc[0].y
    lon = ponto_central.iloc[0].x

    m = leafmap.Map(center=[lat, lon],
                   draw_control=False,
                   measure_control=False,
                   fullscreen_control=False,
                   attribution_control=True)

    m.add_basemap("CartoDB.DarkMatter")

    def add_map(area, arq, ind, scheme, k, cmap, fields, title, legend_position):
        data = arq_geojson.merge(arq_csv, on="Município")

        if not isinstance(data, gpd.GeoDataFrame):
            print("O arquivo não é um GeoDataFrame")
            exit()

        m.add_data(data=data,
                   column=ind,
                   scheme=scheme,
                   k=k,
                   cmap=cmap,
                   fields=fields,
                   legend_title=title,
                   legend_position=legend_position,
                   layer_name=title)

        geojson_layer = folium.GeoJson(data, name=title,
                                       style_function=lambda feature: style,
                                       tooltip=folium.GeoJsonTooltip(fields=fields)).add_to(m)
    m.to_streamlit()







    form = st.form(key="mapa3")
a1,a2 = form.columns(2)

with a1:


    cat1 = form.selectbox("Escolha uma categoria:",("Contextualização","Renda","Riqueza"),key='mapa3',index=None,placeholder="Selecione uma categoria...")


    if cat1 == "Contextualização":
        ind1 = form.selectbox("Escolha um indicador de Contexto:",("População","Densidade demográfica","Grau de urbanização","População feminina","População preta/parda","Razão de dependência"),
                              index=None,placeholder="Selecione um indicador...")
    elif cat1 == "Renda":
        ind1 = form.selectbox("Escolha um indicador de Renda:",("Índice Gini","Renda média da população","Renda da população feminina","Renda dos declarantes do IRPF"),
                              index=None,placeholder="Selecione um indicador...")
    elif cat1 == "Riqueza":
        ind1 = form.selectbox("Escolha um indicador de Riqueza:",("Domicílios com bens duráveis","Número de veículos por pessoas","População declarante do IRPF","Patrimônio líquido médio da população","Patrimônio líquido médio dos declarantes do IRPF"),
                              index=None,placeholder="Selecione um indicador...")

    form.form_submit_button(label="Submit")




with a2:
    cat2 = form.selectbox("Escolha uma categoria:",("Contextualização","Renda","Riqueza"),key='mapa4',index=None,placeholder="Selecione uma categoria...")
    #form.form_submit_button(label="Submit")

#form = st.form(key="form_settings1")

    if cat2 == "Contextualização":
        ind2 = form.selectbox("Escolha um indicador de Contexto:",("População","Densidade demográfica","Grau de urbanização","População feminina","População preta/parda","Razão de dependência"),
                              index=None,placeholder="Selecione um indicador...")
    elif cat2 == "Renda":
        ind2 = form.selectbox("Escolha um indicador de Renda:",("Índice de Gini","Renda média da população","Renda da população feminina","Renda dos declarantes do IRPF"),
                              index=None,placeholder="Selecione um indicador...")
    elif cat2 == "Riqueza":
        ind2 = form.selectbox("Escolha um indicador de Riqueza:",("Domicílios com bens duráveis","Número de veículos por pessoas","População declarante do IRPF","Patrimônio líquido médio da população","Patrimônio líquido médio dos declarantes do IRPF"),
                              index=None,placeholder="Selecione um indicador...")

    form.form_submit_button(label="Submit")
