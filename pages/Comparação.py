import streamlit as st
import pandas as pd
import geopandas as gpd
from deff.mapa import mapa

area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central de Curitiba"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

a1,a2 = st.columns(2)

with a1:
    form = st.form("mapas")
    cat1 = form.selectbox("Escolha uma categoria:",("Contextualização","Renda","Riqueza"),key='mapa1',index=None,placeholder="Selecione uma categoria...")
    if cat1 == "Contextualização":
        ind1 = form.selectbox("Escolha um indicador de Contexto:",("População residente","Densidade demográfica","Grau de urbanização","População feminina","População preta/parda","Razão de dependência"),
                              index=None,placeholder="Selecione um indicador...")
    elif cat1 == "Renda":
        ind1 = form.selectbox("Escolha um indicador de Renda:",("Índice Gini","Renda média da população","Renda da população feminina","Renda dos declarantes do IRPF"),
                              index=None,placeholder="Selecione um indicador...")
    elif cat1 == "Riqueza":
        ind1 = form.selectbox("Escolha um indicador de Riqueza:",("Domicílios com bens duráveis","Número de veículos por pessoas","População declarante do IRPF","Patrimônio líquido médio da população","Patrimônio líquido médio dos declarantes do IRPF"),
                              index=None,placeholder="Selecione um indicador...")

with a2:
    cat2 = form.selectbox("Escolha uma categoria:",("Contextualização","Renda","Riqueza"),key='mapa2',index=None,placeholder="Selecione uma categoria...")
    if cat2 == "Contextualização":
        ind2 = form.selectbox("Escolha um indicador de Contexto:",("População","Densidade demográfica","Grau de urbanização","População feminina","População preta/parda","Razão de dependência"),
                              index=None,placeholder="Selecione um indicador...")
    elif cat2 == "Renda":
        ind2 = form.selectbox("Escolha um indicador de Renda:",("Índice de Gini","Renda média da população","Renda da população feminina","Renda dos declarantes do IRPF"),
                              index=None,placeholder="Selecione um indicador...")
    elif cat2 == "Riqueza":
        ind2 = form.selectbox("Escolha um indicador de Riqueza:",("Domicílios com bens duráveis","Número de veículos por pessoas","População declarante do IRPF","Patrimônio líquido médio da população","Patrimônio líquido médio dos declarantes do IRPF"),
                              index=None,placeholder="Selecione um indicador...")

    form.form_submit_button(label="Gerar mapas")

riqueza = "./dados/csv/riqueza.csv"
renda = "./dados/csv/renda.csv"
contexto = "./dados/csv/contexto.csv"

ind_p = {"População residente":('PR',contexto,'População','FisherJenks',5,'copper_r', ['Município','População'],'População (hab)'),
"Densidade demográfica":('PR',contexto,'Densidade Demográfica (hab/km²)','FisherJenks',5,'YlOrRd', ['Município','Densidade Demográfica (hab/km²)'],'Densidade Demográfica (hab/km²)'),
"Grau de urbanização":('PR',contexto,'Grau de Urbanização (%)','FisherJenks',4,'summer_r', ['Município','Grau de Urbanização (%)'],'Grau de Urbanização (%)'),
"População feminina":('PR',contexto, 'População feminina (%)', 'FisherJenks',3,'Reds', ['Município','População feminina (%)'],'População feminina (%)'),
"População preta/parda":('PR',contexto, 'População preta ou parda (%)', 'FisherJenks', 5, 'YlGnBu', ['Município','População preta ou parda (%)'],'População preta ou parda (%)'),
"Razão de dependência":('PR',contexto, 'Razão de Dependência (%)', 'FisherJenks', 3, 'Purples', ['Município','Razão de Dependência (%)'],'Razão de Dependência (%)'),
"Índice de Gini":('PR',renda,'Índice de Gini','FisherJenks',3,'PuBuGn', ['Município','Índice de Gini'],'Índice de Gini'),
"Renda média da população":('PR',renda,'Renda Média da População (R$ mil)','FisherJenks',5,'YlOrRd', ['Município','Renda Média da População (R$ mil)'],'Renda Média da População (R$ mil)'),
"Rendimento médio da população feminina":('PR',renda,'Rendimento médio da população feminina/masculina (%)','FisherJenks',5,'RdPu', ['Município','Rendimento médio da população feminina/masculina (%)'],'Rendimento médio da população feminina (%)'),
"Renda dos declarantes do IRPF":('PR',renda,'Renda Média dos Declarantes (R$ mil)','FisherJenks',5,'YlGn', ['Município','Renda Média dos Declarantes (R$ mil)'],'Renda Média dos Declarantes (R$ mil)'),
"Domicílios com bens duráveis":('PR', riqueza, 'Domicílios com bens duráveis (%)','FisherJenks', 5, 'OrRd', ['Município','Domicílios com bens duráveis (%)'],'Domicílios com bens duráveis (%)'),
"Número de veículos por pessoas":('PR', riqueza, 'Veículos por pessoa','FisherJenks', 4, 'BuGn', ['Município','Veículos por pessoa'],'Número de veículos por pessoas'),
"População declarante do IRPF":('PR', riqueza, 'Declarantes do IRPF (%)','FisherJenks',5, 'BuPu', ['Município','Declarantes do IRPF (%)'],'População declarante do IRPF (%)'),
"Patrimônio Líquido Médio da População":('PR', riqueza,'Patrimônio líquido médio da população (R$ milhões)','FisherJenks',4,'YlOrBr',['Município','Patrimônio líquido médio da população (R$ milhões)'],'Patrimônio líquido médio da população (R$ milhões)'),
"Patrimônio Líquido Médio dos declarantes do IRPF":('PR', riqueza, 'Patrimônio líquido médio dos declarantes (R$ milhões)','FisherJenks', 5, 'GnBu', ['Município','Patrimônio líquido médio dos declarantes (R$ milhões)'],'Patrimônio líquido dos declarantes do IRPF (R$ milhões)'),
}

if form.form_submit_button("Gerar mapas"):
    with a1:
    # Get the parameters for the first indicator
    area1, arq1, ind1_label, scheme1, k1, cmap1, fields1, title1 = ind_p[ind1]

    # Call the mapa function for the first indicator
    mapa(area1, arq1, ind1_label, scheme1, k1, cmap1, fields1, title1)

    with a2:
    # Get the parameters for the second indicator
    area2, arq2, ind2_label, scheme2, k2, cmap2, fields2, title2 = ind_p[ind2]

    # Call the mapa function for the second indicator
    mapa(area2, arq2, ind2_label, scheme2, k2, cmap2, fields2, title2)