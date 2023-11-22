import streamlit as st
import pandas as pd
import geopandas as gpd

csv = "./dados/csv/contexto.csv"
df_csv = pd.read_csv(csv)
mun = df_csv['Município'].tolist()
op = st.selectbox("Selecione um município:",mun,index=None,placeholder="Selecione ou digite o nome do município...",)

# Read data from GeoJSON file
#geojson_filename = "./dados/PR.geojson"
#gdf_geojson = gpd.read_file(geojson_filename)


