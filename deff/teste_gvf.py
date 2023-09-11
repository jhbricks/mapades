import streamlit as st

import geopandas as gpd

import leafmap
import pandas as pd
import numpy as np
import folium
import leafmap.foliumap as leafmap

#import libpysal
import geopandas
import mapclassify
#import matplotlib.pyplot as plt

########################ARQUIVOS CSV E GEOJSON
contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"
renda = "./dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"
PR = "./dados/geojson/PR.geojson"
NTC =  "./dados/geojson/NTC.geojson"




@st.cache_data
def create_map(area,arq, ind, scheme, k, cmap, fields, title):
    ######encaminha o geojson da area
    if area == 'PR':
        arq_g = "./dados/geojson/PR.geojson"
    else:
        area = 'NTC'
        arq_g = "./dados/geojson/NTC.geojson"

#######MERGE geojson e csv
    arq_csv = pd.read_csv(arq)
    arq_geojson = gpd.read_file(arq_g)
    data = arq_geojson.merge(arq_csv, on="Município")

#######LAT E LON CENTRAIS
    ponto_central = arq_geojson.geometry.centroid
    lat = ponto_central.iloc[0].y
    lon = ponto_central.iloc[0].x
    
    if not isinstance(data,gpd.GeoDataFrame):
        print("O arquivo não é um GeoDataFrame")
        exit()

#Lat e Lon Centrais
    ponto_central = data.geometry.centroid
    lat = ponto_central.iloc[0].y
    lon = ponto_central.iloc[0].x

    # Calculate GVF
    q10 = mapclassify.FisherJenks(data[ind], k=k)
    print(q10)  # excluir esse

    # chama os intervalos das classes
    class_intervals = q10.bins.tolist()

    # calculo da variancia da amostra do ind
    total_variance = np.var(data[ind])

    # Lista para as variancias das classes
    class_variances = []

    # Calculo das variancias de cada intervalo
    for i in range(len(class_intervals) - 1):
        inicio = class_intervals[i]
        final = class_intervals[i + 1]

        class_data = data[(data[ind] > inicio) & (data[ind] <= final)]

        variance = np.var(data[ind])

        class_variances.append(variance)

    # soma dos quadrados das variancias
    SSW = np.sum(class_variances)

    # soma do quadrado das variancias do total
    SST = total_variance * (len(data) - 1)  # variancia amostral

    # Calculo do GVF
    GVF = 100 - (SSW / SST * 100)

    if GVF < 80:
        print("Verifique o número de classes")
    else:
        # Create the map 'm'
        m = leafmap.Map(width=900, height=600, center=[lat, lon],
                        draw_control=False,
                        measure_control=False,
                        fullscreen_control=False,
                        attribution_control=True)

        # ZOOM 
        if area == PR:
          m.zoom_to_bounds((-47.98, -22.44, -54.67, -26.80))
        else:
          m.zoom_to_bounds((-47.87,-24.96,-48.54, -25.85))

        m.add_data(data=data,
                   column=ind,
                   scheme=scheme,
                   k=k,
                   cmap=cmap,
                   fields=fields,
                   legend_title=title,
                   legend_position='Bottomright',
                   layer_name=title,
                   )

        ########VALORES DE MX E MN DAS VARIAVEIS
        max_value = data[ind].max()
        min_value = data[ind].min()
        max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
        min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]

        #####ADICIONAR MX E MN NO MAPA
        folium.Marker([data.loc[data[ind] == max_value, "Y"].iloc[0],
                       data.loc[data[ind] == max_value, "X"].iloc[0]],
                       popup=f"Maior valor: {max_value}<br>{max_municipio}",
                       icon=folium.Icon(color="darkpurple", icon="arrow-up"),
                       ).add_to(m)
        folium.Marker([data.loc[data[ind] == min_value, "Y"].iloc[0],
                       data.loc[data[ind] == min_value, "X"].iloc[0]],
                       popup=f"Menor valor: {min_value}<br>{min_municipio}",
                       icon=folium.Icon(color="purple", icon="arrow-down"),
                       ).add_to(m)


        return m

# Call the create_map function to display the map
if __name__ == '__main__':
    m = create_map(area,arq, ind, scheme, k, cmap, fields, title)
    
    # Display the map in a Jupyter Notebook or IPython environment
    display(m)
