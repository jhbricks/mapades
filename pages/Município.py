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

s_mun = df_csv[df_csv['Município'] == op]



s_ind = df_csv[df_csv['População residente'] == op]



fig = px.bar(s_mun, x=s_mun, y=s_ind, title=f'Indicators for {op}')
st.plotly_chart(fig)





