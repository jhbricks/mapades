import streamlit as st
from streamlit_extras.colored_header import colored_header
import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go
#from deff.mapa__ import mapa
from deff.calculos__ import mx_mn
from deff.calculos__ import conta
#from deff.map import zoom_to_bounds
from deff.map import mapa
from deff.map import grafico
from deff.teste_gvf import create_map
from deff.teste_gvf import mapagvf
from deff.mapa__ import mapa1
import leafmap

contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"
renda = "./dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"
PR = "./dados/geojson/PR.geojson"
NTC =  "./dados/geojson/NTC.geojson"

st.set_page_config(layout="wide")

# Remove whitespace from the top of the page and sidebar
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

colored_header(label="Renda média da população",
               description="Renda média da população no Paraná",
               color_name="red-70",)



#Arquivos
PR = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/PR.geojson'
NTC = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson'
renda = "./dados/csv/renda.csv"

#Selecionar a área [Radio horizontal]
#st.markdown("<h3><font size='8'  color='red'>Renda</font></font></h3>", unsafe_allow_html=True)
area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

if area == "Paraná":
     t1, t2, t3, t4 = st.tabs(["Coeficiente de Gini", "Renda média da população", "Renda da população feminina", "Renda dos declarantes do IRPF"])
     with t1:
          st.markdown('AHAHAJNJAZ')
          NTC = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson'
          m = leafmap.Map(center=[-51.8, -24.7])
          style = {"color": "#000000","fillOpacity": 0,"clickable": False}
          m.add_geojson(NTC, style = {"color": "#000000","fillOpacity": 0,"clickable": False})
          m.to_streamlit()
     with t2:
          colored_header(label="Renda média da população",
                         description="Renda média da população no Paraná",
                         color_name="red-70",)
          mapa1('PR',
               renda,
               'Renda Média da População (R$ mil)',
               'FisherJenks',
               7,
               'YlGnBu',
               ['Município','Renda Média da População (R$ mil)'],
               'Renda Média da População (R$ mil)')
          
          d1,d2 = st.columns([1.5,1])
          with d1:
               mx_mn ('PR',renda,'Renda Média da População (R$ mil)','R$')
               conta ('PR',renda,'Renda Média da População (R$ mil)',2020,'Renda Média da População','media','R$')
               grafico(renda,'Renda Média da População (R$ mil)')
          with d2:
               st.markdown("**Indica a renda média da população (R$) para o ano de 2020**")  
               st.markdown("""**Ano-base:** 2020
                              **Fonte(s):** Fundação Getúlio Vargas (FGV) 
                              **Fórmula:** (Renda Média da população R$/1000) 
                              **Observações:** Renda Média da População é disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV).
                              """)
     
     with t3:
          colored_header(label="Rendimento médio da população feminina",
                         description="Percentual do rendimento médio real mensal das mulheres em relação ao dos homens no Paraná",
                         color_name="red-70",)
          mapa1('PR',renda,'Rendimento médio da população feminina/masculina (%)','FisherJenks',5,'PuRd', ['Município','Rendimento médio da população feminina/masculina (%)'],'Rendimento médio da população feminina/masculina (%)')
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
               

#teste GVF
##################area,data, ind, scheme, k, cmap, fields, title
     with t4:
          colored_header(label="Rendimento médio da população feminina",
                         description="Percentual do rendimento médio real mensal das mulheres em relação ao dos homens no Paraná",
                         color_name="red-70",)
          mapagvf(PR,pop,'População','FisherJenks',5,'PuRd', ['Município','População'],'Rendimento médio da população feminina/masculina (%)')
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

else:
     t1, t2, t3, t4 = st.tabs(["Coeficiente de Gini", "Renda média da população", "Renda da população feminina", "Renda dos declarantes do IRPF"])
     with t1:
          mapagvf('PR',pop,'População','FisherJenks',5,'PuRd', ['Município','População'],'Rendimento médio da população feminina/masculina (%)')

     with t2:
          colored_header(label="Renda Média da População (R$ mil)",
                         description="Renda Média da População (R$ mil)",
                         color_name="red-70",)
          c3, c4 = st.columns(2)
          with c3:
               mapa('NTC',renda,'Renda Média da População (R$ mil)','FisherJenks',4,'RdPu', ['Município','Renda Média da População (R$ mil)'],'Renda Média da População (R$ mil)')
               mx_mn ('NTC',renda,'Renda Média da População (R$ mil)',None)
               conta ('NTC',renda,'Renda Média da População (R$ mil)',2010,'Renda Média da População (R$ mil)',0.47, unidade = None)
          with c4:
               conta ('NTC',renda,'Renda Média da População (R$ mil)',2010,'Renda Média da População (R$ mil)',0.47, unidade = None)

               # read the csv file
               df = pd.read_csv("./dados/csv/renda.csv")

# get the highest and lowest values for the average income column
               highest = df.nlargest(3, 'Renda Média da População (R$ mil)')
               lowest = df.nsmallest(3, 'Renda Média da População (R$ mil)')

# create the bar chart
               fig = go.Figure()
               fig.add_trace(go.Bar(
                              x=highest['Município'],
                              y=highest['Renda Média da População (R$ mil)'],
                              name='Maiores valores'
                              ))
               fig.add_trace(go.Bar(
                              x=lowest['Município'],
                              y=lowest['Renda Média da População (R$ mil)'],
                              name='Menores valores'
                              ))
               fig.show(config={'modeBarButtonsToRemove': ['zoom','pan','select','zoomIn','zoomOut', 'autoScale', 'resetScale']})
               st.plotly_chart(fig, use_container_width=True)


               st.markdown("**Indica a distribuição de renda em uma população. Quanto mais próximo de 0, menor é a concentração de renda no município; portanto, quanto mais próximo de 1 maior é a concentração.**")  
               st.markdown("""**Ano-base:** 2010
                              **Fonte(s):** IPARDES, IBGE  
                              **Fórmula:** Coeficiente de Gini da Renda Domiciliar per Capita  
                              **Observações:** Coeficiente de Gini da Renda Domiciliar per Capita do Censo Demográfico de 2010, obtido no banco de dados do IPARDES.
                              """)