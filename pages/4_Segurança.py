#import streamlit as st
#from streamlit_extras.colored_header import colored_header

#colored_header(label=":orange[Indicadores de Segurança: em breve ⌛]", description="   ", color_name="orange-70",)

import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_folium import folium_static
from deff.mapa import mapa
from deff.map import mx_mn
from deff.calculos import conta
import folium
import geopandas as gpd
import leafmap.foliumap as leafmap
import pandas as pd
import numpy as np


st.set_page_config(layout="wide")

#Selecionar a área [Radio horizontal]
st.markdown("<h3><font size='8'  color='red'>Contextualização</font></font></h3>", unsafe_allow_html=True)
#area = st.selectbox("Selecione uma área:", ("Paraná", "Núcleo Territorial Central
area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#####Arquivos
PR = "./dados/geojson/PR.geojson"
NTC = "https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson"
contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"
renda = "./dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"
#area = 'PR' ou 'NTC'
#arq = arquivo csv, ex: contexto
#ind = indicador conforme está no arquivo csv
#unidade = unidade de medida do indicador, se tiver


c1, c2 = st.columns([3,1])

with c2:
  op = st.selectbox('Selecione...',('Contextualização', 'Renda', 'Riqueza'))

  if op == 'Contextualização':
    op2 = st.selectbox('Selecione...', ('População residente', 'Densidade demográfica','Grau de urbanização') )

with c1:
  
  mapa('bnds','PR',op,op2,'FisherJenks',7,'YlGnBu', ['Município','População'],'População residente')
  mx_mn ('PR',op,op2,'habitantes')
  conta ('PR',op,op2,2021,'População total','soma','habitantes')







if area == "Paraná":
  t1, t2, t3, t4, t5, t6 = st.tabs(["População residente", "Densidade demográfica", "Grau de urbanização", "População feminina", "População preta/parda", "Razão de dependência"])
  with t1:
    colored_header(label="População residente",
                   description="População residente do Paraná",
                   color_name="red-70",)
    #mapa (area, arq, ind, scheme, k, cmap, fields, title)
    mapa('bnds','PR',contexto,'População','FisherJenks',7,'YlGnBu', ['Município','População'],'População residente')
    
    c1,c2 = st.columns([1.5,1])
    with c1:
      mx_mn ('PR',contexto,'População','habitantes')
      conta ('PR',contexto,'População',2021,'População total','soma','habitantes')

    with c2:
      st.markdown("**População residente estimada pelo Instituto Brasileiro de Geografia e Estatística (IBGE) para o ano de 2021.**")  
      st.markdown("""**Ano-base:** 2021  
                  **Fonte(s):** IBGE  
                  **Fórmula:** População total por município  
                  **Observações:** Prévia da população por município do Censo Demográfico 2022 do IBGE.
                  """)      
