import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_folium import folium_static
from deff.mapa import mapa, mx_mn
from deff.calculos_contexto import conta
#from deff.mapa import conta
import folium
import geopandas as gpd
import leafmap.foliumap as leafmap
import pandas as pd

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
    mapa('PR',contexto,'População','FisherJenks',7,'YlGnBu', ['Município','População'],'População residente')
    #mx_mn (area,arq,ind,calc,tipo=None,unidade=None)
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
      mapa('PR',contexto,'Densidade Demográfica (hab/km²)','FisherJenks',9,'PuRd', ['Município','Densidade Demográfica (hab/km²)'],'Densidade Demográfica (hab/km²)')
    #mx_mn (area,arq,ind,tipo,unidade=None)
      c1,c2 = st.columns([1.5,0.5])
      with c1:
        mapa('PR',contexto,'Densidade Demográfica (hab/km²)','FisherJenks',9,'PuRd', ['Município','Densidade Demográfica (hab/km²)'],'Densidade Demográfica (hab/km²)')

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

  
  
  with t4:
    colored_header(label="População feminina",
                   description="Percentual da população feminina no Paraná",
                   color_name="red-70",)
    
  with t5:
    colored_header(label="População preta ou parda",
                   description="Percentual da população preta ou parda no Paraná",
                   color_name="red-70",)
    
  with t6:
    colored_header(label="Razão de dependência",
                   description="Percentual da população fora da idade de trabalhar em relação a população em idade de trabalhar no Paraná",
                   color_name="red-70",)
    
    

if area == "Núcleo Territorial Central":
  t1, t2, t3, t4, t5, t6 = st.tabs(["População residente", "Densidade demográfica",  "Grau de urbanização", "População feminina", "População preta/parda", "Razão de dependência"])
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
    
    


