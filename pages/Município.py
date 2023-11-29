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



s_ind = ['População residente','Grau de Urbanização (%)', 'Razão de Dependência (%)', 'Densidade Demográfica (hab/km²)','População feminina (%)', 'População preta ou parda (%)']



fig = px.bar(s_mun, x='Município', y=s_ind, title=f'Indicators for {op}')
st.plotly_chart(fig)


import plotly.graph_objects as go

s_mun = df_csv[df_csv['Município'] == op]

fig = go.Figure()

fig.add_trace(go.Bar(
    x=s_mun,
    y=s_ind['Grau de Urbanização (%)'],
    name='Primary Product',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=s_mun,
    y=s_ind['População feminina (%)'],
    name='Secondary Product',
    marker_color='lightsalmon'
))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig.update_layout(barmode='group', xaxis_tickangle=-45)
st.plotly_chart(fig)


