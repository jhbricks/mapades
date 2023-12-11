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

# Criar gráfico de dispersão com Plotly Express
fig = px.scatter_mapbox(gdf, lat='Y', lon='X', hover_name='Município', zoom=8)
fig.update_layout(mapbox_style="carto-positron")

# Adicionar camada do GeoJSON para tornar os municípios clicáveis
fig.add_trace(px.choropleth_mapbox(gdf, geojson=gdf.geometry, locations=gdf.index,
                                   color_discrete_sequence=['blue'], opacity=0.5).data[0])

st.plotly_chart(fig)

# Selecionar município
selected_municipality = st.selectbox('Selecione um município:', gdf['Município'])

# Filtrar dados para o município selecionado
selected_data = df[df['Município'] == selected_municipality]

# Mostrar gráficos
st.subheader(f'Indicadores para {selected_municipality}')
st.write(selected_data)

# Adicione gráficos adicionais usando o Plotly Express
fig_indicadores = px.bar(selected_data, x='indicador', y='valor', title=f'Indicadores para {selected_municipality}')
st.plotly_chart(fig_indicadores)
