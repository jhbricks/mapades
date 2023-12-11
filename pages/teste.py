import streamlit as st
import folium
import geopandas as gpd
import pandas as pd

PR = "./dados/geojson/PR.geojson"
csv = "./dados/csv/contexto.csv"
# Carregar o arquivo GeoJSON com os limites dos municípios
municipios = gpd.read_file(PR)

# Carregar o arquivo CSV com os dados dos municípios
municipio_data = pd.read_csv(csv)

# Exibir o mapa do estado
m = folium.Map(zoom_start=5)

# Adicionar camadas de municípios e divisórias ao mapa
m.add_geos(municipios.geometry, crs=municipios.crs, alpha=0.5, color='gray')
m.add_geos(municipios.boundary, crs=municipios.crs, alpha=0.5, color='black')

# Função para exibir os gráficos dos municípios
def show_municipio_graphs(municipio):
    # Selecionar os dadosunicípio
    municipio_data_filtered = municipio_data[municipio_data['Município'] == municipio]
    
    # Exibir os gráficos
    st.write(municipio_data_filtered.head())
    st.plotly_chart(municipio_data_filtered['População'].plot)

# Adicionarão para cada município
for municipality in municipios.values():
    st.write(f'{municipio["Município"]}')
    st.markdown(f'{municipio["Município"]}', callback= lambda: show_municipio_graphs(municipio["Município"]))

# Exibir o mapa
st.write(m)
