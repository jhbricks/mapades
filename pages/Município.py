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
    available_indicators = indicators[category]
    
    # Allow the user to select up to two indicators for each category
    selected = st.multiselect(f"Select Indicators for {category}", available_indicators, key=category, default=[], max(2, len(available_indicators)))

    # Ensure that the total selected indicators do not exceed two
    selected_indicators.extend(selected[:2])

    if len(selected_indicators) >= 2:
        break

# Display the selected indicators
st.write("Selected Indicators:", selected_indicators)

