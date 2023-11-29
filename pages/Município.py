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
#geojson_filename = "./dados/geojson/PR.geojson"
#gdf_geojson = gpd.read_file(geojson_filename)

import streamlit as st
import pandas as pd
import plotly.express as px

# Read the CSV file
csv = "./dados/csv/contexto.csv"
df_csv = pd.read_csv(csv)

# Dropdown to select a municipality
mun = df_csv['Município'].tolist()
selected_mun = st.selectbox("Selecione um município:", mun, index=None, placeholder="Selecione ou digite o nome do município...")

# Filter the dataframe based on the selected municipality
selected_df = df_csv[df_csv['Município'] == selected_mun]

# List of indicators to plot
indicators = ['Grau de Urbanização (%)', 'Razão de Dependência (%)', 'Densidade Demográfica (hab/km²)',
              'População feminina (%)', 'População preta ou parda (%)']

# Create separate bar charts for each indicator
for indicator in indicators:
    # Create a bar chart using Plotly Express
    fig = px.bar(df_csv, x='Município', y=indicator, title=f'{indicator} for all cities')
    
    # Add lines for selected city's value, mean, min, and max
    fig.add_trace(
        go.Scatter(x=df_csv['Município'], y=[selected_df[indicator].values[0]]*len(df_csv['Município']),
                   mode='lines', line=dict(color='red', width=2), name=f'{selected_mun} Value')
    )
    fig.add_trace(
        go.Scatter(x=df_csv['Município'], y=[df_csv[indicator].mean()]*len(df_csv['Município']),
                   mode='lines', line=dict(color='green', width=2), name='Mean')
    )
    fig.add_trace(
        go.Scatter(x=df_csv['Município'], y=[df_csv[indicator].min()]*len(df_csv['Município']),
                   mode='lines', line=dict(color='blue', width=2), name='Min')
    )
    fig.add_trace(
        go.Scatter(x=df_csv['Município'], y=[df_csv[indicator].max()]*len(df_csv['Município']),
                   mode='lines', line=dict(color='orange', width=2), name='Max')
    )
    
    # Update layout for better visualization
    fig.update_layout(barmode='group', title=f'{indicator} Comparison')
    fig.update_xaxes(title_text='Municipality')
    fig.update_yaxes(title_text=indicator)
    
    # Show the chart
    st.plotly_chart(fig)
