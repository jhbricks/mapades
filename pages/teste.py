import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
from plotly.subplots import make_subplots

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
indicators = ['População','Grau de Urbanização (%)', 'Razão de Dependência (%)', 'Densidade Demográfica (hab/km²)',
              'População feminina (%)', 'População preta ou parda (%)']


import plotly.graph_objs as go
import pandas as pd

# Load the CSV file
df = pd.read_csv('https://raw.githubusercontent.com/jhbricks/mapades/main/dados/csv/contexto.csv')

# Filter the dataframe based on the selected city
selected_df = df[df['Município'] == selected_mun]

# Check if the selected city exists in the dataframe
if len(selected_df) == 0:
    st.warning("Cidade selecionada não encontrada no conjunto de dados.")
else:
    # Filtrar o DataFrame para incluir apenas as colunas dos indicadores desejados
    df_filtered = df[['Município'] + indicators]

    # Calcular média, valor mínimo e valor máximo para cada indicador
    mean_values = df_filtered.drop('Município', axis=1).mean()
    min_values = df_filtered.drop('Município', axis=1).min()
    max_values = df_filtered.drop('Município', axis=1).max()

    # Configurar a layout do gráfico para organizar em 3 colunas
    cols = 3
    rows = (len(indicators) // cols) + (len(indicators) % cols)
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=indicators, horizontal_spacing=0.2)

    for i, column in enumerate(indicators):
        if column == 'Município':
            continue

        row = i // cols + 1
        col = i % cols + 1

        # Adicionar barras para o valor do indicador da cidade selecionada (com a cor 'indianred')
        fig.add_trace(go.Bar(x=[selected_df['Município'].values[0]], y=[selected_df[column].values[0]],
                             name='City Indicator', marker_color='indianred'),
                      row=row, col=col, text=[selected_df[column].values[0]], textposition='auto')

        # Adicionar barras para o valor médio (com a cor cinza)
        fig.add_trace(go.Bar(x=['Mean'], y=[mean_values[column]],
                             name='Mean', marker_color='gray'),
                      row=row, col=col, text=[mean_values[column]], textposition='auto')

        # Adicionar barras de erro para os valores mínimo e máximo (com a cor cinza)
        fig.add_trace(go.Bar(x=['Min'], y=[min_values[column]],
                             name='Min', marker_color='lightgray'),
                      row=row, col=col, text=[min_values[column]], textposition='auto')
        fig.add_trace(go.Bar(x=['Max'], y=[max_values[column]],
                             name='Max', marker_color='darkgray'),
                      row=row, col=col, text=[max_values[column]], textposition='auto')

        # Definir rótulos dos eixos
        fig.update_xaxes(title_text='Município', row=row, col=col)
        fig.update_yaxes(title_text='Indicator Value', row=row, col=col)

    # Definir título geral
    fig.update_layout(title_text="Indicators for Selected Municipality", showlegend=False)

    # Mostrar o gráfico usando Streamlit
    st.plotly_chart(fig)