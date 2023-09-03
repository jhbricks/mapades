import streamlit as st
from streamlit_extras.colored_header import colored_header

colored_header(label=":violet[Indicadores de Educação: em breve ⌛]",
               description="   ",
               color_name="violet-70",)


from streamlit_folium import folium_static
import folium
import leafmap
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
import numpy as np
import pyproj


########################ARQUIVOS CSV E GEOJSON
contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"
renda = "https://raw.githubusercontent.com/jhbricks/mapades/main/dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"
PR = "./dados/geojson/PR.geojson"
NTC =  "https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson"



          #@st.cache_data
#######MERGE geojson e csv

csv = pd.read_csv("https://raw.githubusercontent.com/jhbricks/mapades/main/dados/csv/renda.csv")
arq_geojson = gpd.read_file("https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson")
data = arq_geojson.merge(csv, on="Município")
data = data.set_crs(epsg=4326)


#######LAT E LON CENTRAIS
ponto_central = arq_geojson.geometry.centroid
lat = ponto_central.iloc[0].y
lon = ponto_central.iloc[0].x

if not isinstance(data,gpd.GeoDataFrame):
    print("O arquivo não é um GeoDataFrame")
    exit()

##########################MAPA
########MAPA INICIAL
m = leafmap.Map(center=[lat,lon],
                draw_control=False,
                measure_control=False,
                fullscreen_control=False,
                attribution_control=True)
  
#######ADICIONAR O MERGE GDF
bnds = leafmap.gdf_bounds(data)
m.zoom_to_bounds(bnds)

m.add_data(data = renda,
           column='Renda Média da População (R$ mil)',
           scheme='FisherJenks',
           k=2,
           cmap='Oranges',
           fields=['Município','Renda Média da População (R$ mil)'],
           legend_title='Renda Média da População (R$ mil)',
           legend_position='Bottomright',
           layer_name='Renda Média da População (R$ mil)',
           style={"stroke": True, "color": "#000000", "weight": 1, "fillOpacity": 1}
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
#########ADICIONAR NO STREAMLIT
m.to_streamlit()

c1,c2 = st.columns(2)
with c1:
    conta ('PR',renda,'Rendimento médio da população feminina/masculina (%)',2021,'Percentual do rendimento médio da população feminina em relação à masculina',None,None)

    highest = df.nlargest(3, 'Rendimento médio da população feminina/masculina (%)')
    lowest = df.nsmallest(3, 'Rendimento médio da população feminina/masculina (%)')

# create the bar chart
    fig = go.Figure()
    fig.add_trace(go.Bar(
            x=highest['Município'],
            y=highest['Rendimento médio da população feminina/masculina (%)'],
            name='Maiores valores'
            ))
    fig.add_trace(go.Bar(
            x=lowest['Município'],
            y=lowest['Rendimento médio da população feminina/masculina (%)'],
            name='Menores valores'
            ))
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.markdown("**Indica o percentual do rendimento médio real mensal das mulheres em relação ao dos homens celetistas e estatutários.**")  
    st.markdown("""**Ano-base:** 2021
                **Fonte(s):** IPARDES, RAIS  
                **Fórmula:** (Rendimento médio da população feminina*100) /Rendimento média da população masculina   
                **Observações:** Rendimento médio mensal é disponibilizado na RAIS (Relação Anual de Informações Sociais), obtido no banco de dados do IPARDES.
                """)





  
  

