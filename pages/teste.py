import streamlit as st
import folium
import geopandas as gpd
import pandas as pd
import plotly.express as px

PR = "./dados/geojson/PR.geojson"
csv = "./dados/csv/contexto.csv"

# Carregar dados do GeoJSON
geojson_path = PR
gdf = gpd.read_file(geojson_path)

# Carregar dados do CSV
csv_path = csv
df = pd.read_csv(csv_path)

# Interface do Streamlit
st.title('Mapa e Indicadores Municipais')

# Mostrar o mapa
st.subheader('Mapa do Estado com Divisões Municipais')
st.map(gdf)

# Selecionar município
selected_municipality = st.selectbox('Selecione um município:', gdf['Município'])

# Filtrar dados para o município selecionado
selected_data = df[df['Município'] == selected_municipality]

# Mostrar gráficos
st.subheader(f'Indicadores para {selected_municipality}')
st.write(selected_data)

# Adicione gráficos adicionais usando o Plotly Express
fig = px.bar(selected_data, x='População', y='valor', title=f'Indicadores para {selected_municipality}')
st.plotly_chart(fig)

