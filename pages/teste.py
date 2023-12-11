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


import plotly.graph_objs as go
import pandas as pd

# Load the CSV file
df = pd.read_csv('https://raw.githubusercontent.com/jhbricks/mapades/main/dados/csv/contexto.csv')

# Filter the dataframe based on the selected city
selected_df = df[df['Município'] == selected_mun]

if len(selected_df) == 0:
    st.warning("Cidade selecionada não encontrada no conjunto de dados.")
else:
    # Calculate mean, minimum, and maximum values for each indicator (excluding 'Município' column)
    mean_values = df.drop('Município', axis=1).mean()
    min_values = df.drop('Município', axis=1).min()
    max_values = df.drop('Município', axis=1).max()

    for column in mean_values.index:
        if column == 'Município':
            continue

        # Create a bar chart using Plotly
        fig = go.Figure()

        # Add a bar for the selected city's indicator value
        fig.add_trace(go.Bar(x=['City Indicator'], y=[selected_df[column].values[0]], name='City Indicator'))

        # Add a bar for the mean value
        fig.add_trace(go.Bar(x=['Mean'], y=[mean_values[column]], name='Mean'))

        # Add error bars for minimum and maximum values
        fig.add_trace(go.Bar(x=['Min'], y=[min_values[column]], name='Min'))
        fig.add_trace(go.Bar(x=['Max'], y=[max_values[column]], name='Max'))

        # Set chart title and axis labels
        fig.update_layout(title=f"Indicator: {column}", xaxis_title="Statistic", yaxis_title="Indicator Value")

        # Show the chart using Streamlit
        st.plotly_chart(fig)

