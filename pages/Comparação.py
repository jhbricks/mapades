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
    form = st.form(key="mapa1")

    cat1 = form.selectbox("Escolha uma categoria:",("Contextualização","Renda","Riqueza"),key='mapa1',index=None,placeholder="Selecione uma categoria...")


    if cat1 == "Contextualização":
        ind1 = form.selectbox("Escolha um indicador de Contexto:",("População","Densidade demográfica","Grau de urbanização","População feminina","População preta/parda","Razão de dependência"),
                              index=None,placeholder="Selecione um indicador...")
    elif cat1 == "Renda":
        ind1 = form.selectbox("Escolha um indicador de Renda:",("Índice Gini","Renda média da população","Renda da população feminina","Renda dos declarantes do IRPF"),
                              index=None,placeholder="Selecione um indicador...")
    elif cat1 == "Riqueza":
        ind1 = form.selectbox("Escolha um indicador de Riqueza:",("Domicílios com bens duráveis","Número de veículos por pessoas","População declarante do IRPF","Patrimônio líquido médio da população","Patrimônio líquido médio dos declarantes do IRPF"),
                              index=None,placeholder="Selecione um indicador...")

    form.form_submit_button(label="Submit")

    if ind1 == 'População':
        mapa('PR',contexto,'População','FisherJenks',5,'copper_r', ['Município','População'],'População (hab)')



with a2:
    form = st.form(key="mapa2")

    cat1 = form.selectbox("Escolha uma categoria:",("Contextualização","Renda","Riqueza"),key='mapa2',index=None,placeholder="Selecione uma categoria...")
    #form.form_submit_button(label="Submit")

#form = st.form(key="form_settings1")

    if cat1 == "Contextualização":
        ind1 = form.selectbox("Escolha um indicador de Contexto:",("População","Densidade demográfica","Grau de urbanização","População feminina","População preta/parda","Razão de dependência"),
                              index=None,placeholder="Selecione um indicador...")
    elif cat1 == "Renda":
        ind1 = form.selectbox("Escolha um indicador de Renda:",("Índice de Gini","Renda média da população","Renda da população feminina","Renda dos declarantes do IRPF"),
                              index=None,placeholder="Selecione um indicador...")
    elif cat1 == "Riqueza":
        ind1 = form.selectbox("Escolha um indicador de Riqueza:",("Domicílios com bens duráveis","Número de veículos por pessoas","População declarante do IRPF","Patrimônio líquido médio da população","Patrimônio líquido médio dos declarantes do IRPF"),
                              index=None,placeholder="Selecione um indicador...")

    form.form_submit_button(label="Submit")
    if ind1 == 'Índice de Gini':
        mapa('PR',renda,'Índice de Gini','FisherJenks',3,'PuBuGn', ['Município','Índice de Gini'],'Índice de Gini')


form = st.form(key="mapa3")



