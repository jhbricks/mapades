import streamlit as st
import pandas as pd
import geopandas as gpd
from streamlit_extras.colored_header import colored_header

st.set_page_config(layout="wide",page_title='Classificação dos dados')
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

st.markdown("<h3><font size='8'  color='gray'>Classificação dos daos</font></font></h3>", unsafe_allow_html=True)
st.markdown(""" **Classificação de dados** explicação  
            explicação texto texto texto  
            texto texto texto  
            texto texto texto.
""")

#inserir os arquivos csv e geojson
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
