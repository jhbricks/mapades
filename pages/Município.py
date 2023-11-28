import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

csv = "./dados/csv/contexto.csv"
df_csv = pd.read_csv(csv)
mun = df_csv['Município'].tolist()
op = st.selectbox("Selecione um município:",mun,index=None,placeholder="Selecione ou digite o nome do município...",)

# Read data from GeoJSON file
#geojson_filename = "./dados/PR.geojson"
#gdf_geojson = gpd.read_file(geojson_filename)

selected_municipality = df_csv[df_csv['Município'] == op]

selected_indicators = ['Grau de Urbanização (%)', 'Razão de Dependência (%)', 'Densidade Demográfica (hab/km²)',
                        'População feminina (%)', 'População preta ou parda (%)']

fig = px.bar(selected_municipality, x='Município', y=selected_indicators, title=f'Indicators for {op}')
st.plotly_chart(fig)



