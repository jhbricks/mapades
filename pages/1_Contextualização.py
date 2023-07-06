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
NTC = "./dados/geojson/NTC.geojson"
contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"
renda = "./dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"


if area == "Paraná":
  t1, t2, t3, t4, t5, t6 = st.tabs(["População residente", "Densidade demográfica", "Grau de urbanização", "População feminina", "População preta/parda", "Razão de dependência"])
  with t1:
    colored_header(label="População residente",
                   description="População residente do Paraná",
                   color_name="red-70",)
    #mapa (area, arq, ind, scheme, k, cmap, fields, title)
    mapa(13,'PR',contexto,'População','FisherJenks',7,'YlGnBu', ['Município','População'],'População residente')
    
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

  with t2:
    colored_header(label="Densidade demográfica",
                   description="Número de pessoas por km² no Paraná",
                   color_name="red-70",)
    mapa(13,'PR',contexto,'Densidade Demográfica (hab/km²)','FisherJenks',9,'PuRd', ['Município','Densidade Demográfica (hab/km²)'],'Densidade Demográfica (hab/km²)')
    
    c1,c2 = st.columns([1.5,0.5])
    with c1:
      mapa(13,'PR',contexto,'Densidade Demográfica (hab/km²)','FisherJenks',9,'PuRd', ['Município','Densidade Demográfica (hab/km²)'],'Densidade Demográfica (hab/km²)')

    with c2:
      mx_mn ('PR',contexto,'Densidade Demográfica (hab/km²)','hab/km²')
      conta ('PR',contexto,'Densidade Demográfica (hab/km²)',2021)
      st.markdown("""**Ano-base:** 2021  
                  **Fonte(s):** IBGE  
                  **Fórmula:** (População total/Área total) 
                  **Observações:** Prévia da população por município do Censo Demográfico 2022 do IBGE.
                  """)
    with t3:
      colored_header(label="Grau de urbanização",
                     description="Percentual da população residente em áreas urbanas no Paraná",
                     color_name="red-70",)
      mapa(13,'PR',contexto,'Grau de Urbanização (%)','FisherJenks',5,'PuBuGn', ['Município','Grau de Urbanização (%)'],'Grau de Urbanização (%)')
     
      c1,c2 = st.columns([1.5,1])
      with c1:
        mx_mn ('PR',contexto,'Grau de Urbanização (%)','%')
        conta ('PR',contexto,'Grau de Urbanização (%)',2010,'Grau de Urbanização', None,'%')
      with c2:
        st.markdown("**Percentual da população residente em áreas urbanas na população residente total segundo dados do Censo Demográfico de 2010**")  
        st.markdown("""**Ano-base:** 2010 
                    **Fonte(s):** IBGE, 2010; IPARDES,2023  
                    **Fórmula:** (População censitária urbana*100)/População censitária total  
                    **Observações:** Dados do Censo Demográfico de 2010 do IBGE, obtidos no banco de dados do IPARDES.
                    """)
    
    with t4:
      colored_header(label="População feminina",
                     description="Percentual da população feminina no Paraná",
                     color_name="red-70",)
    
      mapa (13,'PR',contexto, 'População feminina (%)', 'EqualInterval',3,'Reds', ['Município','População feminina (%)'],'População feminina (%)')
        
      c1,c2 = st.columns([1.5,1])
      with c1:
        mx_mn ('PR',contexto,'População feminina (%)',unidade=None)
        conta ('PR',contexto, 'População feminina (%)', 2010, None, None, None)

      with c2:
        st.markdown("**Participação percentual da população feminina na população total segundo dados do Censo Demográfico de 2010.**")  
        st.markdown("""**Ano-base:** 2010 
                    **Fonte(s):** IBGE, 2010; IPARDES,2023  
                    **Fórmula:** (População censitária feminina*100)/População censitária total  
                    **Observações:** Dados do Censo Demográfico de 2010 do IBGE, obtidos no banco de dados do IPARDES.
                    """)

    with t5:
      colored_header(label="População preta ou parda",
                     description="Percentual da população preta ou parda no Paraná",
                     color_name="red-70",)
      mapa (13,'PR',contexto, 'População preta ou parda (%)', 'FisherJenks', 5, 'YlGn', ['Município','População preta ou parda (%)'],'População preta ou parda (%)')
        
      c1,c2 = st.columns([1.5,1])
      with c1:
        mx_mn ('PR',contexto,'População preta ou parda (%)',unidade=None)
        conta ('PR',contexto, 'População preta ou parda (%)', 2010, None, None, None)

      with c2:
        st.markdown("**Participação percentual da população preta ou parda na população total segundo dados do Censo Demográfico de 2010.**")  
        st.markdown("""**Ano-base:** 2010 
                    **Fonte(s):** IBGE, 2010; IPARDES,2023  
                    **Fórmula:** ([População censitária preta + população censitária parda]*100)/População censitária total    
                    **Observações:** Dados do Censo Demográfico de 2010 do IBGE, obtidos no banco de dados do IPARDES.
                    """)
                   
    
    with t6:
      colored_header(label="Razão de dependência",
                     description="Percentual da população fora da idade de trabalhar em relação a população em idade de trabalhar no Paraná",
                     color_name="red-70",)
      mapa (13,'PR',contexto, 'Razão de Dependência (%)', 'FisherJenks', 3, 'Purples', ['Município','Razão de Dependência (%)'],'Razão de Dependência (%)')
        
      c1,c2 = st.columns([1.5,1])
      with c1:
        mx_mn ('PR',contexto,'Razão de Dependência (%)','%')
        conta ('PR',contexto, 'Razão de Dependência (%)', '2021*', None, None, None)
        st.text('*População projetada para o ano de 2021') 

      with c2:
        st.markdown("**Indica o percentual da população fora da idade de trabalhar em relação a população em idade de trabalhar (de 15 a 64 anos de idade), estimado com base na população projetada pelo IPARDES para 2021.**")  
        st.markdown("""**Ano-base:** 2021 (projeção)
                    **Fonte(s):** IPARDES,2023  
                    **Fórmula:** ([População projetada de até 14 anos + população projetada com mais de 65 anos]*100)/População projetada total   
                    **Observações:** População projetada para o ano de 2021 disponibilizada pelo IPARDES.
                    """)
    
else:
    t1, t2, t3, t4, t5, t6 = st.tabs(["População residente", "Densidade demográfica", "Grau de urbanização", "População feminina", "População preta/parda", "Razão de dependência"])
    with t1:
      colored_header(label="População residente",
                     description="População residente do Núcleo Territorial Central",
                     color_name="red-70",)
      mapa('NTC',pop,'População','FisherJenks',7,'YlGnBu', ['Município','População'],'População residente')
      c1,c2 = st.columns([1.5,1])
      with c1:
        mx_mn ('NTC',pop,'População','Soma da','soma','habitantes')

      with c2:
        st.markdown("""**População residente estimada pelo Instituto Brasileiro de Geografia e Estatística (IBGE) para o ano de 2021.**  
          A população residente no Núcleo Territorial Central era de XXX habitantes em 2021,
          variando de X e X.
          """)
        st.markdown("""**Ano-base:** 2021  
                    **Fonte(s):** IBGE  
                    **Fórmula:** População total por município  
                    **Observações:** Prévia da população por município do Censo Demográfico 2022 do IBGE.
                    """) 


    with t2:
      colored_header(label="Densidade demográfica",
                     description="Número de pessoas por km² no Núcleo Territorial Central",
                     color_name="red-70",)
    with t3:
      colored_header(label="Grau de urbanização",
                     description="Percentual da população residente em áreas urbanas no Núcleo Territorial Central",
                     color_name="red-70",)
  
    with t4:
      colored_header(label="População feminina",
                     description="Percentual da população feminina no Núcleo Territorial Central",
                     color_name="red-70",)
    
    with t5:
      colored_header(label="População preta ou parda",
                     description="Percentual da população preta ou parda no Núcleo Territorial Central",
                     color_name="red-70",)
    
    with t6:
      colored_header(label="Razão de dependência",
                     description="Percentual da população fora da idade de trabalhar em relação a população em idade de trabalhar no Núcleo Territorial Central",
                     color_name="red-70",)
    
    


