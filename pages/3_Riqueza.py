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

#Arquivos
PR = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/PR.geojson'
NTC = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson'
renda = "./dados/csv/renda.csv"
contexto = "./dados/csv/contexto.csv"
renda = "./dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"

st.set_page_config(layout="wide")

#Selecionar a área [Radio horizontal]
st.markdown("<h3><font size='8'  color='red'>Renda</font></font></h3>", unsafe_allow_html=True)
area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


if area == "Paraná":
  t1, t2, t3, t4, t5 = st.tabs(["Domicílios com bens duráveis", "Número de veículos por pessoas", "População declarante do IRPF", "Patrimônio Líquido Médio da População", "Patrimônio Líquido Médio dos declarantes do IRPF"])
  
  with t1:
    colored_header(label="Domicílios com bens duráveis",
                   description="Percentual de domicílios com bens duráveis no Paraná",
                   color_name="red-70",)
    mapa('bnds','PR', riqueza, 'Domicílios com bens duráveis (%)',
         'FisherJenks', 5, 'Oranges', ['Município','Domicílios com bens duráveis (%)'],
         'Percentual de domicílios com bens duráveis (%)')
    
    d1,d2 = st.columns([1.5,1])
    with d1:
      mx_mn ('PR',riqueza,'Domicílios com bens duráveis (%)','%')
      conta ('PR',riqueza,'Domicílios com bens duráveis (%)',2010,
             'Percentual de domicílios com bens duráveis','media', '%')
    with d2:
      st.markdown("**Indica o percentual de domicílios com bens duráveis¹ em relação ao total de domicílios disponibilizado no Censo Demográfico de 2010.**") 
      st.caption("¹ Rádio, TV, máquina de lavar, geladeira, celular, telefone fixo, computador, motocicleta e automóvel")
      st.markdown("""**Ano-base:** 2010  
                  **Fonte(s):** IPARDES, 2023; IBGE, 2010  
                  **Fórmula:** Percentual de domicílios com bens duráveis   
                  **Observações:** Dados do Censo Demográfico de 2010, obtido no banco de dados do IPARDES.
                  """)
 
  with t2:
    colored_header(label="Número de veículos por pessoas",
                   description="Número de veículos automotores por pessoa no Paraná",
                   color_name="red-70",)
    mapa('bnds','PR', riqueza, 'Veículos por pessoa',
         'FisherJenks', 4, 'RdPu', ['Município','Veículos por pessoa'],
         'Número de veículos por pessoas')
    
    d1,d2 = st.columns([1.5,1])
    with d1:
      mx_mn ('PR',riqueza,'Veículos por pessoa')
      conta ('PR',riqueza,'Veículos por pessoa',2021,
             'Número de veículos por pessoas','media', 'veículo/hab')
    with d2:
      st.markdown("**Indica o número de veículos automotores por pessoa disponibilizado pelo Instituto Paranaense de Desenvolvimento Econômico e Social (Ipardes) para o ano de 2021**") 
      st.markdown("""**Ano-base:** 2021 
                  **Fonte(s):** IPARDES, 2023  
                  **Fórmula:** Número de veículos por pessoas  
                  **Observações:**Dados disponibilizados pelo IPARDES
                  """)
    
  with t3:
    colored_header(label="População declarante do IRPF",
                   description="Percentual de declarantes do Imposto de Renda Pessoa Física (IRPF) na população municipal no Paraná",
                   color_name="red-70",)
    mapa('bnds','PR', riqueza, 'Declarantes do IRPF (%)',
         'FisherJenks', 7, 'OrRd', ['Município','Declarantes do IRPF (%)'],
         'Percentual de declarantes do IRPF na população (%)')
    
    d1,d2 = st.columns([1.5,1])
    with d1:
      mx_mn ('PR',riqueza,'Declarantes do IRPF (%)','%')
      conta ('PR',riqueza,'Declarantes do IRPF (%)',2020,
             'Percentual de declarantes do IRPF na população','18.05', '%')
    with d2:
      st.markdown("**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)**") 
      st.markdown("""**Ano-base:** 2020 
                  **Fonte(s):** FGV  
                  **Fórmula:** Declarantes na População  
                  **Observações:**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)
                  """)
    
  with t4:
    colored_header(label="Patrimônio Líquido Médio da População",
                   description="Patrimônio Líquido Médio da população no Paraná",
                   color_name="red-70",)
   mapa('bnds','PR', riqueza, 'Patrimônio líquido médio da população (R$ milhões',
         'FisherJenks', 5, 'YlGn', ['Município','Patrimônio líquido médio da população (R$ milhões)'],
         'Patrimônio líquido médio da população (R$ milhões)')
    
    d1,d2 = st.columns([1.5,1])
    with d1:
      mx_mn ('PR',riqueza,'Patrimônio líquido médio da população (R$ milhões)','R$ milhões')
      conta ('PR',riqueza,'Patrimônio líquido médio da população (R$ milhões)',2020,
             'Patrimônio líquido médio da população','soma', 'R$ milhões')
    with d2:
      st.markdown("**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)**") 
      st.markdown("""**Ano-base:** 2020 
                  **Fonte(s):** FGV  
                  **Fórmula:** Patrimônio líquido médio da população/ 1000000 
                  **Observações:**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)
                  """)

  with t5:
    colored_header(label="Patrimônio Líquido Médio dos declarantes do IRPF",
                   description="Patrimônio Líquido Médio dos declarantes do IRPF no Paraná",
                   color_name="red-70",)
    mapa('bnds','PR', riqueza, 'Patrimônio líquido médio dos declarantes (R$ milhões)',
         'FisherJenks', 5, 'YlOrRd', ['Município','Patrimônio líquido médio dos declarantes (R$ milhões)'],
         'Patrimônio líquido médio dos declarantes do IRPF (R$ milhões)')
    
    d1,d2 = st.columns([1.5,1])
    with d1:
      mx_mn ('PR',riqueza,'Patrimônio líquido médio dos declarantes (R$ milhões)','R$ milhões')
      conta ('PR',riqueza,'Patrimônio líquido médio dos declarantes (R$ milhões)',2020,
             'Patrimônio líquido médio dos declarantes do IRPF','soma', 'R$ milhões')
    with d2:
      st.markdown("**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)**") 
      st.markdown("""**Ano-base:** 2020 
                  **Fonte(s):** FGV  
                  **Fórmula:** Patrimônio líquido médio dos declarantes do IRPF/ 1000000 
                  **Observações:**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)
                  """)
if area == "Núcleo Territorial Central":
  t1, t2, t3, t4, t5 = st.tabs(["Domicílios com bens duráveis", "Número de veículos por pessoas", "População declarante do IRPF", "Patrimônio Líquido Médio da População", "Patrimônio Líquido Médio dos declarantes do IRPF"])
  
  with t1:
    colored_header(label="Domicílios com bens duráveis",
                   description="Percentual de domicílios com bens duráveis no Núcleo Territorial Central",
                   color_name="red-70",)
        
    mapa('bnds','NTC', riqueza, 'Domicílios com bens duráveis (%)',
         'FisherJenks', 5, 'Oranges', ['Município','Domicílios com bens duráveis (%)'],
         'Percentual de domicílios com bens duráveis (%)')
    
    d1,d2 = st.columns([1.5,1])
    with d1:
      mx_mn ('NTC',riqueza,'Domicílios com bens duráveis (%)','%')
      conta ('NTC',riqueza,'Domicílios com bens duráveis (%)',2010,
             'Percentual de domicílios com bens duráveis','media', '%')
    with d2:
      st.markdown("**Indica o percentual de domicílios com bens duráveis¹ em relação ao total de domicílios disponibilizado no Censo Demográfico de 2010.**") 
      st.caption("¹ Rádio, TV, máquina de lavar, geladeira, celular, telefone fixo, computador, motocicleta e automóvel")
      st.markdown("""**Ano-base:** 2010  
                  **Fonte(s):** IPARDES, 2023; IBGE, 2010  
                  **Fórmula:** Percentual de domicílios com bens duráveis   
                  **Observações:** Dados do Censo Demográfico de 2010, obtido no banco de dados do IPARDES.
                  """)

  
  with t2:
    colored_header(label="Número de veículos por pessoas",
                   description="Número de veículos automotores por pessoa no Núcleo Territorial Central",
                   color_name="red-70",)
    mapa('bnds','NTC', riqueza, 'Veículos por pessoa',
         'FisherJenks', 4, 'RdPu', ['Município','Veículos por pessoa'],
         'Número de veículos por pessoas')
    
    d1,d2 = st.columns([1.5,1])
    with d1:
      mx_mn ('NTC',riqueza,'Veículos por pessoa')
      conta ('NTC',riqueza,'Veículos por pessoa',2021,
             'Número de veículos por pessoas','media', 'veículo/hab')
    with d2:
      st.markdown("**Indica o número de veículos automotores por pessoa disponibilizado pelo Instituto Paranaense de Desenvolvimento Econômico e Social (Ipardes) para o ano de 2021**") 
      st.markdown("""**Ano-base:** 2021 
                  **Fonte(s):** IPARDES, 2023  
                  **Fórmula:** Número de veículos por pessoas  
                  **Observações:**Dados disponibilizados pelo IPARDES
                  """)


  
  with t3:
    colored_header(label="População declarante do IRPF",
                   description="Percentual de declarantes do Imposto de Renda Pessoa Física (IRPF) na população municipal no Núcleo Territorial Central",
                   color_name="red-70",)
    mapa('bnds','NTC', riqueza, 'Declarantes do IRPF (%)',
         'FisherJenks', 7, 'OrRd', ['Município','Declarantes do IRPF (%)'],
         'Percentual de declarantes do IRPF na população (%)')
    
    d1,d2 = st.columns([1.5,1])
    with d1:
      mx_mn ('NTC',riqueza,'Declarantes do IRPF (%)','%')
      conta ('NTC',riqueza,'Declarantes do IRPF (%)',2020,
             'Percentual de declarantes do IRPF na população','17', '%')
    with d2:
      st.markdown("**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)**") 
      st.markdown("""**Ano-base:** 2020 
                  **Fonte(s):** FGV  
                  **Fórmula:** Declarantes na População  
                  **Observações:**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)
                  """)


  with t4:
    colored_header(label="Patrimônio Líquido Médio da População",
                   description="Patrimônio Líquido Médio da população no Núcleo Territorial Central",
                   color_name="red-70",)
    mapa('bnds','NTC', riqueza, 'Patrimônio líquido médio da população (R$ milhões',
         'FisherJenks', 5, 'YlGn', ['Município','Patrimônio líquido médio da população (R$ milhões)'],
         'Patrimônio líquido médio da população (R$ milhões)')
    
    d1,d2 = st.columns([1.5,1])
    with d1:
      mx_mn ('NTC',riqueza,'Patrimônio líquido médio da população (R$ milhões)','R$ milhões')
      conta ('NTC',riqueza,'Patrimônio líquido médio da população (R$ milhões)',2020,
             'Patrimônio líquido médio da população','soma', 'R$ milhões')
    with d2:
      st.markdown("**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)**") 
      st.markdown("""**Ano-base:** 2020 
                  **Fonte(s):** FGV  
                  **Fórmula:** Patrimônio líquido médio da população/ 1000000 
                  **Observações:**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)
                  """)


  with t5:
    colored_header(label="Patrimônio Líquido Médio dos declarantes do IRPF",
                   description="Patrimônio Líquido Médio dos declarantes do IRPF no Núcleo Territorial Central",
                   color_name="red-70",)
    mapa('bnds','NTC', riqueza, 'Patrimônio líquido médio dos declarantes (R$ milhões)',
         'FisherJenks', 5, 'YlOrRd', ['Município','Patrimônio líquido médio dos declarantes (R$ milhões)'],
         'Patrimônio líquido médio dos declarantes do IRPF (R$ milhões)')
    
    d1,d2 = st.columns([1.5,1])
    with d1:
      mx_mn ('NTC',riqueza,'Patrimônio líquido médio dos declarantes (R$ milhões)','R$ milhões')
      conta ('NTC',riqueza,'Patrimônio líquido médio dos declarantes (R$ milhões)',2020,
             'Patrimônio líquido médio dos declarantes do IRPF','soma', 'R$ milhões')
    with d2:
      st.markdown("**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)**") 
      st.markdown("""**Ano-base:** 2020 
                  **Fonte(s):** FGV  
                  **Fórmula:** Patrimônio líquido médio dos declarantes do IRPF/ 1000000 
                  **Observações:**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)
                  """)
