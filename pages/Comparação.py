import streamlit as st
import pandas as pd
import geopandas as gpd
from deff.mapa import mapa

area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central de Curitiba"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

riqueza = "./dados/csv/riqueza.csv"
renda = "./dados/csv/renda.csv"
contexto = "./dados/csv/contexto.csv"

ind_p = {"População residente":('PR',contexto,'População','FisherJenks',5,'copper_r', ['Município','População'],'População (hab)'),
"Densidade demográfica":('PR',contexto,'Densidade Demográfica (hab/km²)','FisherJenks',5,'YlOrRd', ['Município','Densidade Demográfica (hab/km²)'],'Densidade Demográfica (hab/km²)'),
"Grau de urbanização":('PR',contexto,'Grau de Urbanização (%)','FisherJenks',4,'summer_r', ['Município','Grau de Urbanização (%)'],'Grau de Urbanização (%)'),
"População feminina":('PR',contexto, 'População feminina (%)', 'FisherJenks',3,'Reds', ['Município','População feminina (%)'],'População feminina (%)'),
"População preta/parda":('PR',contexto, 'População preta ou parda (%)', 'FisherJenks', 5, 'YlGnBu', ['Município','População preta ou parda (%)'],'População preta ou parda (%)'),
"Razão de dependência":('PR',contexto, 'Razão de Dependência (%)', 'FisherJenks', 3, 'Purples', ['Município','Razão de Dependência (%)'],'Razão de Dependência (%)'),
"Índice de Gini":mapa('PR',renda,'Índice de Gini','FisherJenks',3,'PuBuGn', ['Município','Índice de Gini'],'Índice de Gini'),
"Renda média da população":mapa('PR',renda,'Renda Média da População (R$ mil)','FisherJenks',5,'YlOrRd', ['Município','Renda Média da População (R$ mil)'],'Renda Média da População (R$ mil)'),
"Rendimento médio da população feminina":mapa('PR',renda,'Rendimento médio da população feminina/masculina (%)','FisherJenks',5,'RdPu', ['Município','Rendimento médio da população feminina/masculina (%)'],'Rendimento médio da população feminina (%)'),
"Renda dos declarantes do IRPF":mapa('PR',renda,'Renda Média dos Declarantes (R$ mil)','FisherJenks',5,'YlGn', ['Município','Renda Média dos Declarantes (R$ mil)'],'Renda Média dos Declarantes (R$ mil)'),
"Domicílios com bens duráveis":mapa('PR', riqueza, 'Domicílios com bens duráveis (%)','FisherJenks', 5, 'OrRd', ['Município','Domicílios com bens duráveis (%)'],'Domicílios com bens duráveis (%)'),
"Número de veículos por pessoas":mapa('PR', riqueza, 'Veículos por pessoa','FisherJenks', 4, 'BuGn', ['Município','Veículos por pessoa'],'Número de veículos por pessoas'),
"População declarante do IRPF":mapa('PR', riqueza, 'Declarantes do IRPF (%)','FisherJenks',5, 'BuPu', ['Município','Declarantes do IRPF (%)'],'População declarante do IRPF (%)'),
"Patrimônio Líquido Médio da População":mapa('PR', riqueza,'Patrimônio líquido médio da população (R$ milhões)','FisherJenks',4,'YlOrBr',['Município','Patrimônio líquido médio da população (R$ milhões)'],'Patrimônio líquido médio da população (R$ milhões)'),
"Patrimônio Líquido Médio dos declarantes do IRPF":mapa('PR', riqueza, 'Patrimônio líquido médio dos declarantes (R$ milhões)','FisherJenks', 5, 'GnBu', ['Município','Patrimônio líquido médio dos declarantes (R$ milhões)'],'Patrimônio líquido dos declarantes do IRPF (R$ milhões)'),
}


a1,a2 = st.columns(2)

with a1:
    form = st.form(key="mapa1")
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
    form = st.form(key="mapa2")
    cat2 = form.selectbox("Escolha uma categoria:", list(categoria_p.keys()), key='mapa2',
                           index=None, placeholder="Selecione uma categoria...")

    ind2 = form.selectbox("Escolha um indicador:", list(categoria_p[cat2].keys()),
                           index=None, placeholder="Selecione um indicador...")

    form.form_submit_button(label="Gerar mapas")

# Assuming your mapa function takes the selected category and indicator as arguments
with a1:
    for ind1 in form:
        prs1 = ind_p[ind1]
        mapa(*prs1) 
with a2:
    if ind2 in form2:
        prs2 = ind_p[ind2]
        mapa(*prs2)

#with a2:
 #   if cat2 in categoria_p and ind2 in categoria_p[cat2]:
  #      params2 = categoria_p[cat2][ind2]
   #     mapa(*params2)





