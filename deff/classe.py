import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np
import libpysal
import mapclassify
import folium
import leafmap
import leafmap.foliumap as leafmap

@st.cache_data
def gvf (area,arq,comum,ind,scheme,k,cmap):
    fields = [comum,ind]
    method = scheme

    #merge
    arq_csv = pd.read_csv(arq)
    arq_geojson = gpd.read_file(area)
    gdf = arq_geojson.merge(arq_csv, on="Município")


    methods = {'FisherJenks': mapclassify.FisherJenks,
               'Quantiles': mapclassify.Quantiles,
               'EqualInterval': mapclassify.EqualInterval,
               'BoxPlot': mapclassify.BoxPlot,
               'FisherJenksSampled': mapclassify.FisherJenksSampled,
               'HeadTailBreaks': mapclassify.HeadTailBreaks,
               'JenksCaspall': mapclassify.JenksCaspall,
               'JenksCaspallForced': mapclassify.JenksCaspallForced,
               'JenksCaspallSampled': mapclassify.JenksCaspallSampled,
               'MaxP': mapclassify.MaxP,
               'MaximumBreaks': mapclassify.MaximumBreaks,
               'NaturalBreaks': mapclassify.NaturalBreaks,
               'Percentiles': lambda data, bins: mapclassify.Percentiles(data, bins=[]),
               'StdMean': mapclassify.StdMean,
               'UserDefined': lambda data, bins: mapclassify.UserDefined(data, bins=[]),
               }

# valores das classes
    if method in methods:
        data = gdf[ind]
        q = methods[method](data, k=k)  # classificação
        medias = []  # lista das médias das classes
        Z = []  # lista da soma dos quadrados Z
        intervalos = q.bins.tolist()  # chama os intervalos das classes
        for i in range(len(intervalos)):
            if i == 0:
                dados_classe = data[data <= intervalos[i]]
            elif i == len(intervalos) - 1:
                dados_classe = data[(data > intervalos[i - 1]) & (data <= intervalos[i])]
            else:
                dados_classe = data[(data > intervalos[i - 1]) & (data <= intervalos[i])]

            media_classe = np.mean(dados_classe)  # média das classes
            medias.append(media_classe)

            sq = (dados_classe - media_classe) ** 2  # cálculo o quadrado da diferença de cada classe

            Z.append(np.sum(sq))  # calcula e guarda a soma do quadrado da diferença por essa classe

        SDCM = np.sum(Z)  # Soma de Z

        media_total = np.mean(data)

        SDAM = np.sum((data - media_total) ** 2)  # Soma de xi-X

        GVF = (100 - ((SDCM / SDAM) * 100)).round(2)

        if GVF < 80:
            st.markdown(f"<p> <font style = 'font-weight: bold'><font color='red'><font size='+5'> GVF = {GVF} </font></p>",unsafe_allow_html=True)
        else:
            st.markdown(f"<p> <font style = 'font-weight: bold'><font size='+5'> GVF = {GVF} </font></p>",unsafe_allow_html=True)

    st.markdown(f"<p> <font style = 'font-weight: bold'><font size='+3'> {q} </font></p>",unsafe_allow_html=True)
  
    
#####LAT E LON CENTRAIS
    ponto_central = arq_geojson.geometry.centroid
    lat = ponto_central.iloc[0].y
    lon = ponto_central.iloc[0].x
    
    if not isinstance(gdf,gpd.GeoDataFrame):
        print("O arquivo não é um GeoDataFrame")
        exit()

    style = {"color":"#000000","weight":1, "fillOpacity":0}
##########################MAPA
########MAPA INICIAL
    m = leafmap.Map(
        center=[lat,lon],
    	draw_control=False,
        measure_control=False,
        fullscreen_control=False,
        attribution_control=True)
    
    m.add_basemap("CartoDB.Positron")
    m.add_basemap("CartoDB.DarkMatter")  
    m.add_basemap("Esri.WorldGrayCanvas")

   
    m.add_data(data = gdf,
               column=ind,
               scheme=scheme,
               k=k,
               cmap=cmap,
               fields=fields,
               legend_position='topright',
               )
    geojson_layer = folium.GeoJson(gdf,name = 'Classificação: {k} classes {scheme}',style_function=lambda feature: style,tooltip=folium.GeoJsonTooltip(fields=fields)).add_to(m)

#########ADICIONAR NO STREAMLIT
    m.to_streamlit()


