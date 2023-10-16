import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_folium import folium_static
from deff.mapa import mapa
from deff.mapa import grafico
from deff.calculos import conta
import folium
import geopandas as gpd
import leafmap.foliumap as leafmap
import pandas as pd
import numpy as np


st.set_page_config(layout="wide", page_title="Contextualização - Mapa da Desigualdade")
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

#Selecionar a área [Radio horizontal]
st.markdown("<h3><font size='7'  color='red'>Contextualização</font></font></h3>", unsafe_allow_html=True)
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




if area == "Paraná":
  op = st.selectbox(
   "Selecione abaixo um indicador.",
   ("População residente", "Densidade demográfica", "Grau de urbanização", "População feminina", "População preta/parda", "Razão de dependência"),
   index=None,
   placeholder="Escolha um indicador",
   )
  
  if op == "População residente":
    colored_header(label="População residente",
                   description="População residente do Paraná",
                   color_name="red-70",)
    #mapa (area, arq, ind, scheme, k, cmap, fields, title)
    c1,c2 = st.columns([2,1])
    with c1:
      mapa('bnds','PR',contexto,'População','FisherJenks',5,'Oranges', ['Município','População'],'População residente')
      st.markdown("""**Ano-base:** 2021  
                  **Fonte(s):** IBGE  
                  **Fórmula:** População total por município  
                  **Observações:** Prévia da população por município do Censo Demográfico 2022 do IBGE.
                  """)   

    with c2:
      st.markdown("**População residente estimada pelo Instituto Brasileiro de Geografia e Estatística (IBGE) para o ano de 2021.**")  
      conta ('PR',contexto,'População',2021,'População total','soma','habitantes')
      grafico('PR',contexto,'População','Habitantes')
      
  elif op == "Densidade demográfica":
    colored_header(label="Densidade demográfica",
                   description="Número de pessoas por km² no Paraná",
                   color_name="red-70",)
  
    c1,c2 = st.columns([2,1])
    with c1:
      mapa('bnds','PR',contexto,'Densidade Demográfica (hab/km²)','FisherJenks',5,'PuRd', ['Município','Densidade Demográfica (hab/km²)'],'Densidade Demográfica (hab/km²)')
      st.markdown("""**Ano-base:** 2010 
                  **Fonte(s):** IBGE, 2010; IPARDES,2023  
                  **Fórmula:** (População censitária urbana*100)/População censitária total  
                  **Observações:** Dados do Censo Demográfico de 2010 do IBGE, obtidos no banco de dados do IPARDES.
                  """)
    with c2:
      conta ('PR',contexto,'Densidade Demográfica (hab/km²)',2021)
      grafico('PR',contexto,'Densidade Demográfica (hab/km²)','hab/km²')


  elif op == "Grau de urbanização":
    colored_header(label="Grau de urbanização",
                   description="Percentual da população residente em áreas urbanas no Paraná",
                   color_name="red-70",)
     
    c1,c2 = st.columns([2,1])
    with c1:
 
      mapa('bnds','PR',contexto,'Grau de Urbanização (%)','FisherJenks',4,'Greens', ['Município','Grau de Urbanização (%)'],'Grau de Urbanização (%)')
      st.markdown("""**Ano-base:** 2010 
                  **Fonte(s):** IBGE, 2010; IPARDES,2023  
                  **Fórmula:** (População censitária urbana*100)/População censitária total  
                  **Observações:** Dados do Censo Demográfico de 2010 do IBGE, obtidos no banco de dados do IPARDES.
                  """)
    with c2:
      st.markdown("**Percentual da população residente em áreas urbanas na população residente total segundo dados do Censo Demográfico de 2010**")  
      conta ('PR',contexto,'Grau de Urbanização (%)',2010,'Grau de Urbanização', None,'%')
      grafico('PR',contexto,'Grau de Urbanização (%)','%')


    
    elif op == "População feminina":
      colored_header(label="População feminina",
                     description="Percentual da população feminina no Paraná",
                     color_name="red-70",)
      c1,c2 = st.columns([2,1])
      with c1:
        mapa ('bnds','PR',contexto, 'População feminina (%)', 'FisherJenks',3,'Reds', ['Município','População feminina (%)'],'População feminina (%)')
        st.markdown("""**Ano-base:** 2010 
                    **Fonte(s):** IBGE, 2010; IPARDES,2023  
                    **Fórmula:** (População censitária feminina*100)/População censitária total  
                    **Observações:** Dados do Censo Demográfico de 2010 do IBGE, obtidos no banco de dados do IPARDES.
                    """)
  #      mx_mn ('PR',contexto,'População feminina (%)','%')
      with c2:
        st.markdown("**Participação percentual da população feminina na população total segundo dados do Censo Demográfico de 2010.**")  
        conta ('PR',contexto, 'População feminina (%)', 2010, None, None, None)
        grafico('PR',contexto,'População feminina (%)','%')


    elif op == "População preta/parda":
      colored_header(label="População preta ou parda",
                     description="Percentual da população preta ou parda no Paraná",
                     color_name="red-70",)
        
      c1,c2 = st.columns([2,1])
      with c1:
        mapa ('bnds','PR',contexto, 'População preta ou parda (%)', 'FisherJenks', 5, 'YlGnBu', ['Município','População preta ou parda (%)'],'População preta ou parda (%)')
        st.markdown("""**Ano-base:** 2010  
                    **Fonte(s):** IBGE, 2010; IPARDES,2023  
                    **Fórmula:** ([População censitária preta + população censitária parda]*100)/População censitária total    
                    **Observações:** Dados do Censo Demográfico de 2010 do IBGE, obtidos no banco de dados do IPARDES.
                    """)
                   
   #     mx_mn ('PR',contexto,'População preta ou parda (%)','%')
        conta ('PR',contexto, 'População preta ou parda (%)', 2010, None, None, None)

      with c2:
        st.markdown("**Participação percentual da população preta ou parda na população total segundo dados do Censo Demográfico de 2010.**")  
        conta ('PR',contexto, 'População preta ou parda (%)', 2010, None, None, None)
        grafico('PR',contexto,'População preta ou parda (%)','%')

    
  else: 
      op == "Razão de dependência"
      colored_header(label="Razão de dependência",
                     description="Percentual da população fora da idade de trabalhar em relação a população em idade de trabalhar no Paraná",
                     color_name="red-70",)
        
      c1,c2 = st.columns([2,1])
      with c1:
        mapa ('bnds','PR',contexto, 'Razão de Dependência (%)', 'FisherJenks', 3, 'Purples', ['Município','Razão de Dependência (%)'],'Razão de Dependência (%)')
    #    mx_mn ('PR',contexto,'Razão de Dependência (%)','%')
        st.markdown("""**Ano-base:** 2021 (projeção)  
                    **Fonte(s):** IPARDES,2023  
                    **Fórmula:** ([População projetada de até 14 anos + população projetada com mais de 65 anos]*100)/População projetada total   
                    **Observações:** População projetada para o ano de 2021 disponibilizada pelo IPARDES.
                    """)         
        st.caption('*População projetada para o ano de 2021') 

      with c2:
        st.markdown("**Indica o percentual da população fora da idade de trabalhar em relação a população em idade de trabalhar (de 15 a 64 anos de idade), estimado com base na população projetada pelo IPARDES para 2021.**")  
        conta ('PR',contexto, 'Razão de Dependência (%)', '2021*', None, None, None)
        grafico('PR',contexto,'Razão de Dependência (%)','%')

    
else:
  area = 'NTC'
  NTC = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson'
  t1, t2, t3, t4, t5, t6 = st.tabs(["População residente", "Densidade demográfica", "Grau de urbanização", "População feminina", "População preta/parda", "Razão de dependência"])
  with t1:
    colored_header(label="População residente",
                   description="População residente do Núcleo Territorial Central",
                   color_name="red-70",)
    c1,c2 = st.columns([2,1])
    with c1:
      mapa('bnds','NTC',contexto,'População','FisherJenks',4,'Oranges', ['Município','População'],'População residente')
      st.markdown("""**Ano-base:** 2021  
                  **Fonte(s):** IBGE  
                  **Fórmula:** População total por município  
                  **Observações:** Prévia da população por município do Censo Demográfico 2022 do IBGE.
                  """)    
     # mx_mn ('NTC',contexto,'População','habitantes')
    with c2:
      st.markdown("**População residente estimada pelo Instituto Brasileiro de Geografia e Estatística (IBGE) para o ano de 2021.**")  
      conta ('NTC',contexto,'População',2021,'População total','soma','habitantes')
      grafico('NTC',contexto,'População','habitantes')
  
  with t2:
    colored_header(label="Densidade demográfica",
                   description="Número de pessoas por km² no Núcleo Territorial Central",
                   color_name="red-70",)
    c1,c2 = st.columns([2,1])
    with c1:
      mapa('bnds','NTC',contexto,'Densidade Demográfica (hab/km²)','FisherJenks',4,'PuRd', ['Município','Densidade Demográfica (hab/km²)'],'Densidade Demográfica (hab/km²)')
      st.markdown("""**Ano-base:** 2021  
                  **Fonte(s):** IBGE  
                  **Fórmula:** (População total/Área total) 
                  **Observações:** Prévia da população por município do Censo Demográfico 2022 do IBGE.
                  """)    
    with c2:
      #mx_mn ('NTC',contexto,'Densidade Demográfica (hab/km²)','hab/km²')
      conta ('NTC',contexto,'Densidade Demográfica (hab/km²)',2021)
      grafico('NTC',contexto,'Densidade Demográfica (hab/km²)','hab/km²')


  with t3:
    colored_header(label="Grau de urbanização",
                   description="Percentual da população residente em áreas urbanas no Núcleo Territorial Central",
                   color_name="red-70",)
    c1,c2 = st.columns([2,1])
    with c1:
      mapa('bnds','NTC',contexto,'Grau de Urbanização (%)','FisherJenks',3,'Greens', ['Município','Grau de Urbanização (%)'],'Grau de Urbanização (%)')
      st.markdown("""**Ano-base:** 2010 
                  **Fonte(s):** IBGE, 2010; IPARDES,2023  
                  **Fórmula:** (População censitária urbana*100)/População censitária total  
                  **Observações:** Dados do Censo Demográfico de 2010 do IBGE, obtidos no banco de dados do IPARDES.
                  """)
      #mx_mn ('NTC',contexto,'Grau de Urbanização (%)','%')
    with c2:
      st.markdown("**Percentual da população residente em áreas urbanas na população residente total segundo dados do Censo Demográfico de 2010**")  
      conta ('NTC',contexto,'Grau de Urbanização (%)',2010,'Grau de Urbanização', None,'%')
      grafico('NTC',contexto,'Grau de Urbanização (%)','%')

  with t4: #########################
    colored_header(label="População feminina",
                   description="Percentual da população feminina no Núcleo Territorial Central",
                   color_name="red-70",)
    c1,c2 = st.columns([2,1])
    with c1:
      mapa ('bnds','NTC',contexto, 'População feminina (%)', 'FisherJenks',3,'Reds', ['Município','População feminina (%)'],'População feminina (%)')
      st.markdown("""**Ano-base:** 2010 
                  **Fonte(s):** IBGE, 2010; IPARDES,2023  
                  **Fórmula:** (População censitária feminina*100)/População censitária total  
                  **Observações:** Dados do Censo Demográfico de 2010 do IBGE, obtidos no banco de dados do IPARDES.
                  """)
      #mx_mn ('NTC',contexto,'População feminina (%)','%')
    with c2:
      st.markdown("**Participação percentual da população feminina na população total segundo dados do Censo Demográfico de 2010.**")  
      conta ('NTC',contexto, 'População feminina (%)', 2010, None, None, None)
      grafico('NTC',contexto,'População feminina (%)','%')

  with t5:
    colored_header(label="População preta ou parda",
                   description="Percentual da população preta ou parda no Núcleo Territorial Central",
                   color_name="red-70",)
    c1,c2 = st.columns([2,1])
    with c1:
      mapa ('bnds','NTC',contexto, 'População preta ou parda (%)', 'FisherJenks', 4, 'YlGnBu', ['Município','População preta ou parda (%)'],'População preta ou parda (%)')
      st.markdown("""**Ano-base:** 2010 
                  **Fonte(s):** IBGE, 2010; IPARDES,2023  
                  **Fórmula:** ([População censitária preta + população censitária parda]*100)/População censitária total    
                  **Observações:** Dados do Censo Demográfico de 2010 do IBGE, obtidos no banco de dados do IPARDES.
                  """)
      #mx_mn ('NTC',contexto,'População preta ou parda (%)','%')
    with c2:
      st.markdown("**Participação percentual da população preta ou parda na população total segundo dados do Censo Demográfico de 2010.**")  
      conta ('NTC',contexto, 'População preta ou parda (%)', 2010, None, None, None)
      grafico('NTC',contexto,'População preta ou parda (%)','%')

  with t6:
    colored_header(label="Razão de dependência",
                   description="Percentual da população fora da idade de trabalhar em relação a população em idade de trabalhar no Núcleo Territorial Central",
                   color_name="red-70",)
    c1,c2 = st.columns([2,1])
    with c1:
      mapa ('bnds','NTC',contexto, 'Razão de Dependência (%)', 'FisherJenks', 4, 'Purples', ['Município','Razão de Dependência (%)'],'Razão de Dependência (%)')
      st.markdown("""**Ano-base:** 2021 (projeção)
                  **Fonte(s):** IPARDES,2023  
                  **Fórmula:** ([População projetada de até 14 anos + população projetada com mais de 65 anos]*100)/População projetada total   
                  **Observações:** População projetada para o ano de 2021 disponibilizada pelo IPARDES.
                  """)
    #  mx_mn ('NTC',contexto,'Razão de Dependência (%)','%')
      st.caption('*População projetada para o ano de 2021') 
    with c2:
      st.markdown("**Indica o percentual da população fora da idade de trabalhar em relação a população em idade de trabalhar (de 15 a 64 anos de idade), estimado com base na população projetada pelo IPARDES para 2021.**")  
      conta ('NTC',contexto, 'Razão de Dependência (%)', '2021*', None, None, None)
      grafico('NTC',contexto,'Razão de Dependência (%)','%')


