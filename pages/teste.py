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
indicators = ['População','Grau de Urbanização (%)', 'Razão de Dependência (%)', 'Densidade Demográfica (hab/km²)',
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
    # Filtrar o DataFrame para incluir apenas as colunas dos indicadores desejados
    df_filtered = df[['Município'] + indicators]

    # Calcular média, valor mínimo e valor máximo para cada indicador
    mean_values = df_filtered.drop('Município', axis=1).mean()
    min_values = df_filtered.drop('Município', axis=1).min()
    max_values = df_filtered.drop('Município', axis=1).max()

    for column in mean_values.index:
        if column == 'Município':
            continue

        # Criar um gráfico de barras usando Plotly
        fig = go.Figure()

        # Adicionar uma barra para o valor do indicador da cidade selecionada
        fig.add_trace(go.Bar(x=[column], y=[selected_df[column].values[0]], name='City Indicator'))

        # Adicionar uma barra para o valor médio
        fig.add_trace(go.Bar(x=[column], y=[mean_values[column]], name='Média do Paraná'))

        # Adicionar barras de erro para os valores mínimo e máximo
        fig.add_trace(go.Bar(x=[column], y=[min_values[column]], name='Menor valor do Paraná'))
        fig.add_trace(go.Bar(x=[column], y=[max_values[column]], name='Maior valor do Paraná'))

        # Definir título do gráfico e rótulos dos eixos
        fig.update_layout(title=f"Indicator: {column}", xaxis_title="Statistic", yaxis_title="Indicator Value")

        # Mostrar o gráfico usando Streamlit
        st.plotly_chart(fig)