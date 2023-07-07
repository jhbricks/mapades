import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import leafmap.foliumap as leafmap
import pandas as pd
from deff.mapa import mapa
from deff.map import mx_mn
from deff.calculos import conta
from deff.calculos import conta_renda

st.set_page_config(layout="wide")

#Selecionar a área [Radio horizontal]
st.markdown("<h3><font size='8'  color='red'>Renda</font></font></h3>", unsafe_allow_html=True)
area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#Arquivos
PR = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/PR.geojson'
NTC = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson'
renda = "./dados/csv/renda.csv"

if area == "Paraná":
  t1, t2, t3, t4 = st.tabs(["Coeficiente de Gini", "Renda da população feminina", "Renda média da população", "Renda dos declarantes do IRPF"])
  with t1:
    colored_header(label="Coeficiente de Gini",
                   description="Coeficiente de Gini renda domiciliar per capita no Paraná",
                   color_name="red-70",)
    mapa('bnds','PR',renda,'Coeficiente de Gini','FisherJenks',3,'RdPu', ['Município','Coeficiente de Gini'],'Coeficiente de Gini da Renda Domiciliar per Capita')
    
    d1,d2 = st.columns([1.5,1])
    with d1:
      mx_mn ('PR',renda,'Coeficiente de Gini')
      conta ('PR',renda,'Coeficiente de Gini',2010,'Coeficiente de Gini',0.54)
    with d2:
      st.markdown("**Indica a distribuição de renda em uma população. Quanto mais próximo de 0, menor é a concentração de renda no município; portanto, quanto mais próximo de 1 maior é a concentração.**)    
      st.markdown("""**Ano-base:** 2010  
                  **Fonte(s):** IPARDES, 2023; IBGE, 2010  
                  **Fórmula:** Coeficiente de Gini da Renda Domiciliar per Capita   
                  **Observações:** Coeficiente de Gini da Renda Domiciliar per Capita do Censo Demográfico de 2010, obtido no banco de dados do IPARDES.
                  """)
  with t2:
    colored_header(label="Rendimento médio da população feminina",
                   description="Percentual do rendimento médio real mensal das mulheres em relação ao dos homens no Paraná",
                   color_name="red-70",)
    mapa('bnds','PR',renda,'Rendimento médio da população feminina/masculina (%)','FisherJenks',5,'PuRd', ['Município','Rendimento médio da população feminina/masculina (%)'],'Rendimento médio da população feminina/masculina (%)')
    
    d1,d2 = st.columns([1.5,1])
    with d1:
      mx_mn ('PR',renda,'Rendimento médio da população feminina/masculina (%)',None)
      conta ('PR',renda,'Rendimento médio da população feminina/masculina (%)',2021,'Percentual do rendimento médio da população feminina em relação à masculina',None,None)
    with d2:
      st.markdown("**Indica o percentual do rendimento médio real mensal das mulheres em relação ao dos homens celetistas e estatutários.**")  
      st.markdown("""**Ano-base:** 2021
                  **Fonte(s):** IPARDES, RAIS  
                  **Fórmula:** (Rendimento médio da população feminina*100) /Rendimento média da população masculina   
                  **Observações:** Rendimento médio mensal é disponibilizado na RAIS (Relação Anual de Informações Sociais), obtido no banco de dados do IPARDES.
                  """)
  with t3:
    colored_header(label="Renda média da população",
                   description="Renda média da população no Paraná",
                   color_name="red-70",)
    mapa('bnds','PR',renda,'Renda Média da População (R$ mil)','FisherJenks',7,'YlGnBu', ['Município','Renda Média da População (R$ mil)'],'Renda Média da População (R$ mil)')
    
    d1,d2 = st.columns([1.5,1])
    with d1:
      mx_mn ('PR',renda,'Renda Média da População (R$ mil)','R$ mil')
      conta ('PR',renda,'Renda Média da População (R$ mil)',2020,'Renda Média da População','media','R$ mil')
    with d2:
      st.markdown("**Indica a renda média da população (R$) para o ano de 2020**")  
      st.markdown("""**Ano-base:** 2020
                  **Fonte(s):** Fundação Getúlio Vargas (FGV) 
                  **Fórmula:** (Renda Média da população R$/1000) 
                  **Observações:** Renda Média da População é disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV).
                  """)    
  with t4:
    colored_header(label="Renda dos declarantes do IRPF",
                   description="Renda média dos declarentes do IRPF no Paraná",
                   color_name="red-70",)
    mapa('bnds','PR',renda,'Renda Média dos Declarantes (R$ mil)','FisherJenks',5,'GnBu', ['Município','Renda Média dos Declarantes (R$ mil)'],'Renda Média dos Declarantes (R$ mil)')
    
    d1,d2 = st.columns([1.5,1])
    with d1:
      mx_mn ('PR',renda,'Renda Média dos Declarantes (R$ mil)','R$ mil')
      conta ('PR',renda,'Renda Média dos Declarantes (R$ mil)',2020,'Renda Média dos Declarantes','media','R$ mil')
    with d2:
      st.markdown("**Indica a renda média (R$) dos declarantes do Imposto de Renda Pessoa Física (IRPF) para o ano de 2020.**")  
      st.markdown("""**Ano-base:** 2020
                  **Fonte(s):** Fundação Getúlio Vargas (FGV) 
                  **Fórmula:** (Renda Média dos declarantes R$/1000) 
                  **Observações:** Renda Média dos declarantes do IRPF é disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV).
                  """)
   
if area == "Núcleo Territorial Central":
  NTC = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson'
  arq_g = NTC
  
  t1, t2, t3, t4 = st.tabs(["Coeficiente de Gini", "Renda da população feminina", "Renda média da população", "Renda dos declarantes do IRPF"])
  with t1:
    colored_header(label="Coeficiente de Gini",
                   description="Coeficiente de Gini renda domiciliar per capita no Núcleo Territorial Central",
                   color_name="red-70",)
    mapa('bnds','NTC',renda,'Coeficiente de Gini','FisherJenks',4,'RdPu', ['Município','Coeficiente de Gini'],'Coeficiente de Gini da Renda Domiciliar per Capita')
    
    c1,c2 = st.columns([1.5,1])
    with c1:
      mx_mn ('NTC',renda,'Coeficiente de Gini',None)
      conta ('NTC',renda,'Coeficiente de Gini',2010,'Coeficiente de Gini',0.47,None)

    with c2:
      st.markdown("**Indica a distribuição de renda em uma população. Quanto mais próximo de 0, menor é a concentração de renda no município; portanto, quanto mais próximo de 1 maior é a concentração.**")  
      st.markdown("""**Ano-base:** 2010
                  **Fonte(s):** IPARDES, IBGE  
                  **Fórmula:** Coeficiente de Gini da Renda Domiciliar per Capita  
                  **Observações:** Coeficiente de Gini da Renda Domiciliar per Capita do Censo Demográfico de 2010, obtido no banco de dados do IPARDES.
                  """)
  
  with t2:
    colored_header(label="Rendimento médio da população feminina",
                   description="Percentual do rendimento médio real mensal das mulheres em relação ao dos homens no Núcleo Territorial Central",
                   color_name="red-70",)
    mapa('bnds','NTC',renda,'Rendimento médio da população feminina/masculina (%)','FisherJenks',4,'PuRd', ['Município','Rendimento médio da população feminina/masculina (%)'],'Rendimento médio da população feminina/masculina (%)')
    
    c1,c2 = st.columns([1.5,1])
    with c1:
      mx_mn ('NTC',renda,'Rendimento médio da população feminina/masculina (%)',None)
      conta ('NTC',renda,'Rendimento médio da população feminina/masculina (%)',2021,'Percentual do rendimento médio da população feminina em relação à masculina',None,None)

    with c2:
      st.markdown("**Indica o percentual do rendimento médio real mensal das mulheres em relação ao dos homens celetistas e estatutários.**")  
      st.markdown("""**Ano-base:** 2021
                  **Fonte(s):** IPARDES, RAIS  
                  **Fórmula:** (Rendimento médio da população feminina*100) /Rendimento média da população masculina   
                  **Observações:** Rendimento médio mensal é disponibilizado na RAIS (Relação Anual de Informações Sociais), obtido no banco de dados do IPARDES.
                  """)
  with t3:
    colored_header(label="Renda média da população",
                   description="Renda média da população no Núcleo Territorial Central",
                   color_name="red-70",)
    mapa('bnds','NTC',renda,'Renda Média da População (R$ mil)','FisherJenks',4,'YlGnBu', ['Município','Renda Média da População (R$ mil)'],'Renda Média da População (R$ mil)')
    
    c1,c2 = st.columns([1.5,1])
    with c1:
      mx_mn ('NTC',renda,'Renda Média da População (R$ mil)','R$ mil')
      conta ('NTC',renda,'Renda Média da População (R$ mil)',2020,'Renda Média da População','media','R$ mil')

    with c2:
      st.markdown("**Indica a renda média da população (R$) para o ano de 2020**")  
      st.markdown("""**Ano-base:** 2020
                  **Fonte(s):** Fundação Getúlio Vargas (FGV) 
                  **Fórmula:** (Renda Média da população R$/1000) 
                  **Observações:** Renda Média da População é disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV).
                  """) 

  with t4:
    colored_header(label="Renda dos declarantes do IRPF",
                   description="Renda média dos declarentes do IRPF no Núcleo Territorial Central",
                   color_name="red-70",)
    mapa('bnds','NTC',renda,'Renda Média dos Declarantes (R$ mil)','FisherJenks',4,'GnBu', ['Município','Renda Média dos Declarantes (R$ mil)'],'Renda Média dos Declarantes (R$ mil)')
    
    c1,c2 = st.columns([1.5,1])
    with c1:
      mx_mn ('NTC',renda,'Renda Média dos Declarantes (R$ mil)','R$ mil')
      conta ('NTC',renda,'Renda Média dos Declarantes (R$ mil)',2020,'Renda Média dos Declarantes','media','R$ mil')

    with c2:
      st.markdown("**Indica a renda média (R$) dos declarantes do Imposto de Renda Pessoa Física (IRPF) para o ano de 2020.**")  
      st.markdown("""**Ano-base:** 2020
                  **Fonte(s):** Fundação Getúlio Vargas (FGV) 
                  **Fórmula:** (Renda Média dos declarantes R$/1000) 
                  **Observações:** Renda Média dos declarantes do IRPF é disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV).
                  """)
