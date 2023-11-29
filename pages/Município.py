import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

#csv = "./dados/csv/contexto.csv"
#df_csv = pd.read_csv(csv)
#mun = df_csv['Município'].tolist()
#op = st.selectbox("Selecione um município:",mun,index=None,placeholder="Selecione ou digite o nome do município...",)

# Read data from GeoJSON file
#geojson_filename = "./dados/PR.geojson"
#gdf_geojson = gpd.read_file(geojson_filename)

import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

# Read data from GeoJSON file
geojson_filename = "./dados/geojson/PR.geojson"
gdf_geojson = gpd.read_file(geojson_filename)

mun = gdf_geojson['Município'].tolist()
op = st.selectbox("Selecione um município:", mun, index=None, placeholder="Selecione ou digite o nome do município...",)

# Filter GeoDataFrame based on selected municipality
selected_city = gdf_geojson[gdf_geojson['Município'] == op]

# Create a map centered on the selected city
fig = px.scatter_geo(selected_city,
                     lat='Y', lon='X',
                     hover_name='Município',
                     title=f"Map of {op}",
                     scope='south america')

# Add all cities in grey
fig.add_trace(px.scatter_geo(gdf_geojson,
                             lat='Y', lon='X',
                             hover_name='Município',
                             mode='markers',
                             marker=dict(color='grey'),
                             opacity=0.7).data[0])

# Highlight the selected city in red
fig.add_trace(px.scatter_geo(selected_city,
                             lat='Y', lon='X',
                             hover_name='Município',
                             mode='markers',
                             marker=dict(color='red'),
                             opacity=1).data[0])

# Show the map
st.plotly_chart(fig)
