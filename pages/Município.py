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



import streamlit as st
import pages.1_Contextualização

# Define categories and indicators
categories = ["One", "Two", "Three"]
indicators = {
    "One": ["A", "B", "C"],
    "Two": ["D", "E", "F", "G"],
    "Three": ["H", "I", "J"]
}

# Allow the user to select categories
selected_categories = st.multiselect("Select Categories", categories)

# Allow the user to select indicators based on the selected categories
selected_indicators = []
for category in selected_categories:
    selected_indicators.extend(st.multiselect(f"Select Indicators for {category}", indicators[category]))

# Display the selected indicators
if selected_indicators == "A":
    a

