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
     with t2:
          colored_header(label="Renda média da população",
                         description="Renda média da população no Paraná",
                         color_name="red-70",)
          mapa('PR',
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
          mapa('PR',renda,'Rendimento médio da população feminina/masculina (%)','FisherJenks',5,'PuRd', ['Município','Rendimento médio da população feminina/masculina (%)'],'Rendimento médio da população feminina/masculina (%)')
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
               st.plotly_chart(fig, use_container_width=True)

               st.markdown("**Indica a distribuição de renda em uma população. Quanto mais próximo de 0, menor é a concentração de renda no município; portanto, quanto mais próximo de 1 maior é a concentração.**")  
               st.markdown("""**Ano-base:** 2010
                              **Fonte(s):** IPARDES, IBGE  
                              **Fórmula:** Coeficiente de Gini da Renda Domiciliar per Capita  
                              **Observações:** Coeficiente de Gini da Renda Domiciliar per Capita do Censo Demográfico de 2010, obtido no banco de dados do IPARDES.
                              """)

     with t3:
          import streamlit as st
          from streamlit_folium import folium_static
          import folium
          import leafmap
          import leafmap.foliumap as leafmap
          import geopandas as gpd
          import pandas as pd
          import numpy as np

########################ARQUIVOS CSV E GEOJSON
          
#######MERGE geojson e csv

          csv = pd.read_csv("./dados/csv/renda.csv")
          arq_geojson = gpd.read_file("./dados/geojson/NTC.geojson")
          data = arq_geojson.merge(csv, on="Município")
          if not isinstance(data,gpd.GeoDataFrame):
               print("O arquivo não é um GeoDataFrame")
               exit()


#######LAT E LON CENTRAIS
          ponto_central = arq_geojson.geometry.centroid
          lat = ponto_central.iloc[0].y
          lon = ponto_central.iloc[0].x

##########################MAPA
########MAPA INICIAL
          m = leafmap.Map(center=[lat,lon],
                          draw_control=False,
                          measure_control=False,
                          fullscreen_control=False,
                          attribution_control=True)
  
#######ADICIONAR O MERGE GDF


          m.add_data(data = renda, column='Renda Média da População (R$ mil)',
                     scheme='FisherJenks',
                     k=2,
                     cmap='Oranges',
                     fields=['Município','Renda Média da População (R$ mil)'],
                     legend_title='Renda Média da População (R$ mil)',
                     legend_position='Bottomright',
                     layer_name='Renda Média da População (R$ mil)',
                     style={"stroke": True, "color": "#000000", "weight": 1, "fillOpacity": 1}
                     )
########VALORES DE MX E MN DAS VARIAVEIS
          max_value = data[ind].max()
          min_value = data[ind].min()
          max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
          min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]
#####ADICIONAR MX E MN NO MAPA
          folium.Marker([data.loc[data[ind] == max_value, "Y"].iloc[0],
                         data.loc[data[ind] == max_value, "X"].iloc[0]],
                         popup=f"Maior valor: {max_value}<br>{max_municipio}",
                         icon=folium.Icon(color="darkpurple", icon="arrow-up"),
                         ).add_to(m) 
          folium.Marker([data.loc[data[ind] == min_value, "Y"].iloc[0],
	                    data.loc[data[ind] == min_value, "X"].iloc[0]],
                         popup=f"Menor valor: {min_value}<br>{min_municipio}",
                         icon=folium.Icon(color="purple", icon="arrow-down"),
                         ).add_to(m)
#########ADICIONAR NO STREAMLIT
          m.to_streamlit()

          c1,c2 = st.columns(2)
          with c1:
               conta ('PR',renda,'Rendimento médio da população feminina/masculina (%)',2021,'Percentual do rendimento médio da população feminina em relação à masculina',None,None)

               highest = df.nlargest(3, 'Rendimento médio da população feminina/masculina (%)')
               lowest = df.nsmallest(3, 'Rendimento médio da população feminina/masculina (%)')

# create the bar chart
               fig = go.Figure()
               fig.add_trace(go.Bar(
                              x=highest['Município'],
                              y=highest['Rendimento médio da população feminina/masculina (%)'],
                              name='Maiores valores'
                              ))
               fig.add_trace(go.Bar(
                              x=lowest['Município'],
                              y=lowest['Rendimento médio da população feminina/masculina (%)'],
                              name='Menores valores'
                              ))
               st.plotly_chart(fig, use_container_width=True)

          with c2:
               st.markdown("**Indica o percentual do rendimento médio real mensal das mulheres em relação ao dos homens celetistas e estatutários.**")  
               st.markdown("""**Ano-base:** 2021
                              **Fonte(s):** IPARDES, RAIS  
                              **Fórmula:** (Rendimento médio da população feminina*100) /Rendimento média da população masculina   
                              **Observações:** Rendimento médio mensal é disponibilizado na RAIS (Relação Anual de Informações Sociais), obtido no banco de dados do IPARDES.
                              """)





  
  
