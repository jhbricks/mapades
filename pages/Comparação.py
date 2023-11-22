import streamlit as st
import pandas as pd
import geopandas as gpd

area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central de Curitiba"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

a1,a2 = st.columns(2)

with a1:
    cat1 = st.selectbox("Escolha uma categoria:",("Contextualização","Renda","Riqueza"),index=None,placeholder="Selecione uma categoria...")
    if cat1 == "Contextualização":
        ind1 = st.selectbox("Escolha um indicador de contexto:",("População","Densidade demográfica","Grau de urbanização","População feminina","População preta/parda","Razão de dependência"),
                          index=None,placeholder="Selecione um indicador...")
    elif cat1 == "Renda":
        ind1 = st.selectbox("Escolha um indicador de renda:",("Índice Gini","Renda média da população","Renda da população feminina","Renda dos declarantes do IRPF"),
                           index=None,placeholder="Selecione um indicador...")
    elif cat1 == "Riqueza":
        ind1 = st.selectbox("Escolha um indicador de riqueza:",("Domicílios com bens duráveis","Número de veículos por pessoas","População declarante do IRPF","Patrimônio líquido médio da população","Patrimônio líquido médio dos declarantes do IRPF"),
                           index=None,placeholder="Selecione um indicador...")
with a2:
    cat2 = st.selectbox("Escolha uma categoria:",("Contextualização","Renda","Riqueza"),index=None,placeholder="Selecione uma categoria...")
    if cat2 == "Contextualização":
        ind2 = st.selectbox("Escolha um indicador de contexto:",("População","Densidade demográfica","Grau de urbanização","População feminina","População preta/parda","Razão de dependência"),
                          index=None,placeholder="Selecione um indicador...")
    elif cat2 == "Renda":
        ind2 = st.selectbox("Escolha um indicador de renda:",("Índice Gini","Renda média da população","Renda da população feminina","Renda dos declarantes do IRPF"),
                           index=None,placeholder="Selecione um indicador...")
    elif cat2 == "Riqueza":
        ind2 = st.selectbox("Escolha um indicador de riqueza:",("Domicílios com bens duráveis","Número de veículos por pessoas","População declarante do IRPF","Patrimônio líquido médio da população","Patrimônio líquido médio dos declarantes do IRPF"),
                           index=None,placeholder="Selecione um indicador...")    

