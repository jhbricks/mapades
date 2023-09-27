import streamlit as st
import pandas as pd
import geopandas as gpd
from streamlit_extras.colored_header import colored_header

st.set_page_config(layout="wide")
colored_header(label="Sobre",description="   ",color_name="blue-green-70",)
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.markdown(""" **Classificação de dados** explicação  
            explicação texto texto texto  
            texto texto texto  
            texto texto texto.
""")

#inserir os arquivos csv e geojson
option = st.selectbox('Escolha os arquivos que irá adicionar:',('CSV', 'GeoJSON e CSV', 'GeoDataFrame (gdf)'))
if option == 'GeoJSON E CSV':
    arq = st.file_uploader("Carregue os arquivos", type={"csv", "geojson"},accept_multiple_files=True)
    if arq is not None:
        csv_arq = None
        geo_arq = None
        for arquivo in arq:
            if arquivo.type == 'application/vnd.geo+json':
                geo_arq = arquivo
            elif arquivo.type == 'text/csv':
                csv_arq = arquivo
    # Verifica se ambos os arquivos foram carregados
    if csv_arq is not None and geo_arq is not None:
        arq_gpd = gpd.read_file(geo_arq)
        arq_pd = pd.read_csv(csv_arq)
        data = arq_gpd.merge(arq_pd, on="Município")
    else:
        st.warning("Por favor, carregue um arquivo CSV e um arquivo GeoJSON.")
elif option == 'CSV':
    arq = st.file_uploader("Carregue os arquivos", type={"csv"})
    if arq is not None:
        csv_arq = None
        for arquivo in arq:
            arquivo.type == 'text/csv'
            csv_arq = arquivo
    if csv_arq is not None:
        data = pd.read_csv(csv_arq)
    else:
        st.warning("Por favor, carregue um arquivo CSV e um arquivo GeoJSON.")
else:
    arq = st.file_uploader("Carregue os arquivos", type={"gdf"})
    if arq is not None:
        gdf_arq = None
        for arquivo in arq:
            arquivo.type == 'application/vnd.gdf':
            
            csv_arq = arquivo
    if csv_arq is not None:
        data = pd.read_csv(csv_arq)
    else:
        st.warning("Por favor, carregue um arquivo CSV e um arquivo GeoJSON.")




if option == 'GEOJSON E CSV':
    arq_geojson = gpd.read_file(geo_arq)
    arq_csv = pd.read_csv(csv_arq)
    data = geojson_pr.merge(pdpop, on="Município")


