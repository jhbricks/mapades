import streamlit as st
import pandas as pd
import geopandas as gpd

area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central de Curitiba"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

op = st.selectbox("Selecione um município:",("Email", "Home phone", "Mobile phone"),index=None)



# Read data from CSV file
csv = "./dados/csv/contexto.csv"
df_csv = pd.read_csv(csv)

# Read data from GeoJSON file
geojson_filename = "./dados/PR.geojson"
gdf_geojson = gpd.read_file(geojson_filename)

# Extract city names from CSV
cities_csv = df_csv['Município'].tolist()

# Extract city names from GeoJSON
cities_geojson = gdf_geojson['Município'].tolist()

# Streamlit code
option_csv = st.selectbox(
    "Selecione um município a partir do CSV",
    cities_csv,
    index=None,
)

option_geojson = st.selectbox(
    "Selecione um município a partir do GeoJSON",
    cities_geojson,
    index=None,
)
