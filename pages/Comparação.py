import streamlit as st
import pandas as pd
import geopandas as gpd
from deff.mapa import mapa

area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central de Curitiba"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

renda = "./dados/csv/renda.csv"
contexto = "./dados/csv/contexto.csv"

a1,a2 = st.columns(2)

with a1:
    cat1 = st.multiselect("Escolha uma categoria:",["Contextualização","Renda","Riqueza"],placeholder="Selecione uma categoria...")
    if cat1 == "Contextualização":
        ind1 = st.multiselect("Escolha um indicador de Contexto:",("População","Densidade demográfica","Grau de urbanização","População feminina","População preta/parda","Razão de dependência"),
                              placeholder="Selecione um indicador...")
    elif cat1 == "Renda":
        ind1 = st.multiselect("Escolha um indicador de Renda:",("Índice Gini","Renda média da população","Renda da população feminina","Renda dos declarantes do IRPF"),
                              placeholder="Selecione um indicador...")
    elif cat1 == "Riqueza":
        ind1 = st.multiselect("Escolha um indicador de Riqueza:",("Domicílios com bens duráveis","Número de veículos por pessoas","População declarante do IRPF","Patrimônio líquido médio da população","Patrimônio líquido médio dos declarantes do IRPF"),
                              placeholder="Selecione um indicador...")

