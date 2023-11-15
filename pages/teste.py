import streamlit as st
from streamlit_extras.colored_header import colored_header
import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go
from deff.mapa import mapa
#from deff.calculos__ import mx_mn
#from deff.calculos__ import conta
#from deff.map import zoom_to_bounds
from deff.mapa import grafico
from deff.calculos import conta
from deff.map import map
#from deff.map import grafico
#from deff.teste_gvf import create_map
#from deff.teste_gvf import mapagvf
#from deff.mapa__ import mapa1

from deff.teste_local import local_2
from deff.teste_local import local_3
from deff.teste_local import estado

from streamlit_folium import folium_static
import folium
import leafmap
import leafmap.foliumap as leafmap

contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"
renda = "./dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"
PR = "./dados/geojson/PR.geojson"
NTC =  "./dados/geojson/NTC.geojson"




st.set_page_config(layout="wide")

st.markdown("<h3><font size='8'  color='red'>Renda</font></font></h3>", unsafe_allow_html=True)
area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#Arquivos
PR = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/PR.geojson'
NTC = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson'
renda = "./dados/csv/renda.csv"
contexto = "./dados/csv/contexto.csv"

if area == "Paraná":
  A,t1, t2, t3, t4, t5 = st.tabs(['B','A',"Coeficiente de Gini", "Renda média da população", "Renda da população feminina", "Renda dos declarantes do IRPF"])
  arq_g = PR
  with B:
       
    c1,c2 = st.columns([2,1])
    with c1:
      mapa ('PR',contexto, 'População preta ou parda (%)', 'FisherJenks', 5, 'Wistia', ['Município','População preta ou parda (%)'],'População preta ou parda (%)')
      st.markdown("""**Ano-base:** 2010  
                    **Fonte(s):** IBGE, 2010; IPARDES,2023  
                    **Fórmula:** ([População censitária preta + população censitária parda]*100)/População censitária total  
                    **Observações:** Dados do Censo Demográfico de 2010 do IBGE, obtidos no banco de dados do IPARDES.
                    """)

    with c2:
      st.markdown("**Participação percentual da população preta ou parda na população total segundo dados do Censo Demográfico de 2010.**")  
      conta ('PR',contexto, 'População preta ou parda (%)', 2010, None, None, None)
      grafico('PR',contexto,'População preta ou parda (%)','%')
  with A:
      map('PR',contexto,'População','FisherJenks',5,'Oranges', ['Município','População'],'População residente (hab)')
  with t1:
    colored_header(label="Coeficiente de Gini",
                   description="Coeficiente de Gini renda domiciliar per capita no Paraná",
                   color_name="red-70",)
    #area,arq,ind,scheme,k,cmap,fields,title
    d1,d2 = st.columns([2,0.7])
    with d1:
      arq = renda
      ind = 'Coeficiente de Gini'
      scheme = 'FisherJenks'
      k=3
      cmap='PuBuGn'
      fields=['Município','Coeficiente de Gini']
      title='Coeficiente de Gini da Renda Domiciliar per Capita'
      #######MERGE geojson e csv
      arq_csv = pd.read_csv(arq)
      arq_geojson = gpd.read_file(arq_g)
      data = arq_geojson.merge(arq_csv, on="Município")
#######LAT E LON CENTRAIS
      lon, lat = leafmap.gdf_centroid(data)
##########################MAPA
      style = {'Color': '#000000'} 
########MAPA INICIAL
      m = leafmap.Map(center=(lat,lon), zoom=9,draw_control=False,measure_control=False,fullscreen_control=False,attribution_control=True)
#######ADICIONAR O MERGE GDF
      m.add_data(data = data,column=ind,scheme=scheme,k=k,cmap=cmap,fields=fields,legend_title=title,legend_position='topright',layer_name=title,style_function = lambda feature: {'color': 'black','weight':1})
########VALORES DE MX E MN DAS VARIAVEIS
      max_value = data[ind].max()
      min_value = data[ind].min()
      max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
      min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]
#####ADICIONAR MX E MN NO MAPA
      folium.Marker([data.loc[data[ind] == max_value, "Y"].iloc[0],data.loc[data[ind] == max_value, "X"].iloc[0]],popup=f"Maior valor: {max_value}<br>{max_municipio}",icon=folium.Icon(color="darkpurple", icon="arrow-up")).add_to(m) 
      folium.Marker([data.loc[data[ind] == min_value, "Y"].iloc[0],data.loc[data[ind] == min_value, "X"].iloc[0]],popup=f"Menor valor: {min_value}<br>{min_municipio}",icon=folium.Icon(color="purple", icon="arrow-down"),).add_to(m)
#########ADICIONAR NO STREAMLIT
      m.to_streamlit()
      st.markdown("""**Ano-base:** 2010  
                  **Fonte(s):** IPARDES, 2023; IBGE, 2010  
                  **Fórmula:** Coeficiente de Gini da Renda Domiciliar per Capita   
                  **Observações:** Coeficiente de Gini da Renda Domiciliar per Capita do Censo Demográfico de 2010, obtido no banco de dados do IPARDES.
                  """)
    with d2:
      st.markdown("**Indica a distribuição de renda em uma população. Quanto mais próximo de 0, menor é a concentração de renda no município; portanto, quanto mais próximo de 1 maior é a concentração.**")    
      conta ('PR',renda,'Coeficiente de Gini',2010,'Coeficiente de Gini',0.54, None)
      grafico ('PR',renda,'Coeficiente de Gini',None)


  with t2:
    colored_header(label="Renda média da população",
                   description="Renda média da população no Paraná",
                   color_name="red-70",)
    
    d1,d2 = st.columns([2,1])
    with d1:
      arq = renda
      ind = 'Renda Média da População (R$ mil)'
      scheme = 'FisherJenks'
      k=5
      cmap='YlOrRd'
      fields=['Município','Renda Média da População (R$ mil)']
      title='Renda Média da População (R$ mil)'
      #######MERGE geojson e csv
      arq_csv = pd.read_csv(arq)
      arq_geojson = gpd.read_file(arq_g)
      data = arq_geojson.merge(arq_csv, on="Município")
#######LAT E LON CENTRAIS
      lon, lat = leafmap.gdf_centroid(data)
##########################MAPA
      style = {'Color': '#000000'} 
########MAPA INICIAL
      m = leafmap.Map(center=(lat,lon),draw_control=False,measure_control=False,fullscreen_control=False,attribution_control=True)
#######ADICIONAR O MERGE GDF
      m.add_data(data = data,column=ind,scheme=scheme,k=k,cmap=cmap,fields=fields,legend_title=title,legend_position='topright',layer_name=title)
########VALORES DE MX E MN DAS VARIAVEIS
      max_value = data[ind].max()
      min_value = data[ind].min()
      max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
      min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]
#####ADICIONAR MX E MN NO MAPA
      folium.Marker([data.loc[data[ind] == max_value, "Y"].iloc[0],data.loc[data[ind] == max_value, "X"].iloc[0]],popup=f"Maior valor: {max_value}<br>{max_municipio}",icon=folium.Icon(color="darkpurple", icon="arrow-up")).add_to(m) 
      folium.Marker([data.loc[data[ind] == min_value, "Y"].iloc[0],data.loc[data[ind] == min_value, "X"].iloc[0]],popup=f"Menor valor: {min_value}<br>{min_municipio}",icon=folium.Icon(color="purple", icon="arrow-down"),).add_to(m)
#########ADICIONAR NO STREAMLIT
      m.to_streamlit()
      st.markdown("""**Ano-base:** 2020
                  **Fonte(s):** Fundação Getúlio Vargas (FGV) 
                  **Fórmula:** (Renda Média da população R$/1000) 
                  **Observações:** Renda Média da População é disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV).
                  """)    
    with d2:
      st.markdown("**Indica a renda média da população (R$) para o ano de 2020**")  
      conta ('PR',renda,'Renda Média da População (R$ mil)',2020,'Renda Média da População','media','R$ mil')
      grafico('PR',renda,'Renda Média da População (R$ mil)','R$ mil')

  with t3:
    colored_header(label="Rendimento médio da população feminina",
                   description="Percentual do rendimento médio real mensal das mulheres em relação ao dos homens no Paraná",
                   color_name="red-70",)
    
    d1,d2 = st.columns([2,1])
    with d1:
      arq = renda
      ind = 'Rendimento médio da população feminina/masculina (%)'
      scheme = 'FisherJenks'
      k=5
      cmap='RdPu'
      fields=['Município','Rendimento médio da população feminina/masculina (%)']
      title='Rendimento médio da população feminina (%)'
      #######MERGE geojson e csv
      arq_csv = pd.read_csv(arq)
      arq_geojson = gpd.read_file(arq_g)
      data = arq_geojson.merge(arq_csv, on="Município")
#######LAT E LON CENTRAIS
      lon, lat = leafmap.gdf_centroid(data)
##########################MAPA
      style = {'Color': '#000000'} 
########MAPA INICIAL
      m = leafmap.Map(center=(lat,lon),zoom_max=16,zoom_min=11,draw_control=False,measure_control=False,fullscreen_control=False,attribution_control=True)
#######ADICIONAR O MERGE GDF
      m.add_data(data = data,column=ind,scheme=scheme,k=k,cmap=cmap,fields=fields,legend_title=title,legend_position='topright',layer_name=title)
########VALORES DE MX E MN DAS VARIAVEIS
      max_value = data[ind].max()
      min_value = data[ind].min()
      max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
      min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]
#####ADICIONAR MX E MN NO MAPA
      folium.Marker([data.loc[data[ind] == max_value, "Y"].iloc[0],data.loc[data[ind] == max_value, "X"].iloc[0]],popup=f"Maior valor: {max_value}<br>{max_municipio}",icon=folium.Icon(color="darkpurple", icon="arrow-up")).add_to(m) 
      folium.Marker([data.loc[data[ind] == min_value, "Y"].iloc[0],data.loc[data[ind] == min_value, "X"].iloc[0]],popup=f"Menor valor: {min_value}<br>{min_municipio}",icon=folium.Icon(color="purple", icon="arrow-down"),).add_to(m)
#########ADICIONAR NO STREAMLIT
      m.to_streamlit()
      st.markdown("""**Ano-base:** 2021
                  **Fonte(s):** IPARDES, RAIS  
                  **Fórmula:** (Rendimento médio da população feminina*100) /Rendimento média da população masculina   
                  **Observações:** Rendimento médio mensal é disponibilizado na RAIS (Relação Anual de Informações Sociais), obtido no banco de dados do IPARDES.
                  """)
    with d2:
      st.markdown("**Indica o percentual do rendimento médio real mensal das mulheres em relação ao dos homens celetistas e estatutários.**")  
      conta ('PR',renda,'Rendimento médio da população feminina/masculina (%)',2021,'Percentual do rendimento médio da população feminina em relação à masculina',None,None)
      grafico('PR',renda,'Rendimento médio da população feminina/masculina (%)',None)

else:
  att = st.radio("Selecione uma área:",("A","B","C","ESSE AQUI","DEF"))
  st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
  arq_g = PR
  if att == "A":
    #area,arq,ind,scheme,k,cmap,fields,title
    d1,d2 = st.columns([2,1])
    with d1:
      arq = renda
      ind = 'Coeficiente de Gini'
      scheme = 'FisherJenks'
      k=3
      cmap='PuBuGn'
      fields=['Município','Coeficiente de Gini']
      title='Coeficiente de Gini da Renda Domiciliar per Capita'
      #######MERGE geojson e csv
      arq_csv = pd.read_csv(arq)
      arq_geojson = gpd.read_file(arq_g)
      data = arq_geojson.merge(arq_csv, on="Município")
#######LAT E LON CENTRAIS
      lon, lat = leafmap.gdf_centroid(data)
##########################MAPA
      style = {'Color': '#000000'} 
########MAPA INICIAL
      m = leafmap.Map(center=(lat,lon),draw_control=False,measure_control=False,fullscreen_control=False,attribution_control=True)
#######ADICIONAR O MERGE GDF
      m.add_data(data = data,column=ind,scheme=scheme,k=k,cmap=cmap,fields=fields,legend_title=title,legend_position='TopRight',layer_name=title,style_function = lambda feature: {'color': 'black','weight':1})
########VALORES DE MX E MN DAS VARIAVEIS
      max_value = data[ind].max()
      min_value = data[ind].min()
      max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
      min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]
#####ADICIONAR MX E MN NO MAPA
      folium.Marker([data.loc[data[ind] == max_value, "Y"].iloc[0],data.loc[data[ind] == max_value, "X"].iloc[0]],popup=f"Maior valor: {max_value}<br>{max_municipio}",icon=folium.Icon(color="darkpurple", icon="arrow-up")).add_to(m) 
      folium.Marker([data.loc[data[ind] == min_value, "Y"].iloc[0],data.loc[data[ind] == min_value, "X"].iloc[0]],popup=f"Menor valor: {min_value}<br>{min_municipio}",icon=folium.Icon(color="purple", icon="arrow-down"),).add_to(m)
#########ADICIONAR NO STREAMLIT
      m.to_streamlit()
      st.markdown("""**Ano-base:** 2010  
                  **Fonte(s):** IPARDES, 2023; IBGE, 2010  
                  **Fórmula:** Coeficiente de Gini da Renda Domiciliar per Capita   
                  **Observações:** Coeficiente de Gini da Renda Domiciliar per Capita do Censo Demográfico de 2010, obtido no banco de dados do IPARDES.
                  """)
    with d2:
      st.markdown("**Indica a distribuição de renda em uma população. Quanto mais próximo de 0, menor é a concentração de renda no município; portanto, quanto mais próximo de 1 maior é a concentração.**")    
      conta ('PR',renda,'Coeficiente de Gini',2010,'Coeficiente de Gini',0.54, None)
      grafico ('PR',renda,'Coeficiente de Gini',None)

  elif att == "DEF":
    c1,c2,c3 = st.columns (3)
    br= './dados/geojson/1990.geojson'
    pr= './dados/geojson/PR.geojson'
    ntc= './dados/geojson/NTC.geojson'
          
      #estado (url,destaque,fields,layer)
      #local_2(url, url1, destaque,fields1,fields,layer,layer1)
      #local_3 (url, url1,url2, destaque,fields3,fields,fields2,layer,layer1)
    with c1:
      estado('br','Paraná','nome','Brasil')
    with c2:
      local_2('pr','br','Paraná','Município','nome','Paraná','Brasil')
    with c3: 
      local_3 ('ntc', 'br','pr', 'Paraná','Município','nome','Município','Núcleo Territorial Central','Brasil','Paraná')


###############################################################################################################################

  elif att == "ESSE AQUI":
    colored_header(label="Identificação da região",description="Identificação do Estado do Paraná",color_name="red-70",)
    c1,c2 = st.columns([1,2])


    style1 = lambda x: {'color': 'black', 'fillColor': '#fc8d62', "weight": 1} #destaque PR
    style2 = lambda x: {'color': 'black', 'fillColor': '#8da0cb', "weight": 1.5, 'fillOpacity':0.7} #destaque NTC

    def style_function(feature):
      if feature['properties']['nome'] == 'Paraná':
            return {'color': 'black', 'fillColor': '#fc8d62', 'weight': 1}
      else:
            return {'color': 'black', 'fillColor': '#66c2a5', 'weight': 1}


    with c1:
      url1= './dados/geojson/1990.geojson'
      gdf = gpd.read_file(url1)
      centroid = gdf.geometry.centroid
      lon, lat = centroid.x[0], centroid.y[0]
      m2 = leafmap.Map(center=(lat, lon), draw_control=False, measure_control=False, fullscreen_control=False, attribution_control=True)
      m2.add_geojson(url1, fields = ['nome'], layer_name= 'Brasil', style_function= style_function)
      legend_dict = {'Brasil': '#66c2a5','Paraná' : '#fc8d62'}
      m2.add_legend(title = 'Legenda', legend_dict= legend_dict, position='bottomleft')
      m2.to_streamlit()

    with c2:
      url1= './dados/geojson/1990.geojson'
      url= './dados/geojson/PR.geojson'
      gdf = gpd.read_file(url)
      centroid = gdf.geometry.centroid
      lon, lat = centroid.x[0], centroid.y[0]
      m = leafmap.Map(center=(lat, lon), zoom=10, draw_control=False, measure_control=False, fullscreen_control=False, attribution_control=True)
      m.add_geojson(url1, layer_name='Brasil', style_function=style_function)
      m.add_geojson(url, fields=['Município'], layer_name='Municípios do Paraná', style_function=style1)
      legend_dict = {'Brasil': '#66c2a5','Paraná' : '#fc8d62'}
      m.add_legend(title = 'Legenda', legend_dict= legend_dict, position='bottomleft')
      m.to_streamlit()

    url = './dados/geojson/NTC.geojson'
    url1= './dados/geojson/1990.geojson'
    pr= './dados/geojson/PR.geojson'
    a = gpd.read_file(url)
    centroid = a.geometry.centroid
    lon, lat = centroid.x[0], centroid.y[0]
    m = leafmap.Map(center=(lat, lon),draw_control=False, measure_control=False, fullscreen_control=False, attribution_control=True)
    m.add_geojson(url1, layer_name='Brasil', style_function=style_function)
    m.add_geojson(pr, fields=['Município'], layer_name='Municípios do Paraná', style_function=style1)
    m.add_geojson(url, fields=['Município'], layer_name='Núcleo Territorial Central', style_function = style2 )
    legend_dict = {'Brasil': '#66c2a5','Paraná' : '#fc8d62', 'Núcleo Territorial Central': '#8da0cb'}
    m.add_legend(title = 'Legenda', legend_dict= legend_dict, position='bottomleft')
    m.to_streamlit()
####################################################################################################################

  elif att == "B":
    colored_header(label="Renda média da população",
                   description="Renda média da população no Paraná",
                   color_name="red-70",)
    
    d1,d2 = st.columns([2,1])
    with d1:
      arq = renda
      ind = 'Renda Média da População (R$ mil)'
      scheme = 'FisherJenks'
      k=5
      cmap='YlOrRd'
      fields=['Município','Renda Média da População (R$ mil)']
      title='Renda Média da População (R$ mil)'
      #######MERGE geojson e csv
      arq_csv = pd.read_csv(arq)
      arq_geojson = gpd.read_file(arq_g)
      data = arq_geojson.merge(arq_csv, on="Município")
#######LAT E LON CENTRAIS
      lon, lat = leafmap.gdf_centroid(data)
##########################MAPA
      style = {'Color': '#000000'} 
########MAPA INICIAL
      m = leafmap.Map(center=(lat,lon),draw_control=False,measure_control=False,fullscreen_control=False,attribution_control=True)
#######ADICIONAR O MERGE GDF
      m.add_data(data = data,column=ind,scheme=scheme,k=k,cmap=cmap,fields=fields,legend_title=title,legend_position='topright',layer_name=title)
########VALORES DE MX E MN DAS VARIAVEIS
      max_value = data[ind].max()
      min_value = data[ind].min()
      max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
      min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]
#####ADICIONAR MX E MN NO MAPA
      folium.Marker([data.loc[data[ind] == max_value, "Y"].iloc[0],data.loc[data[ind] == max_value, "X"].iloc[0]],popup=f"Maior valor: {max_value}<br>{max_municipio}",icon=folium.Icon(color="darkpurple", icon="arrow-up")).add_to(m) 
      folium.Marker([data.loc[data[ind] == min_value, "Y"].iloc[0],data.loc[data[ind] == min_value, "X"].iloc[0]],popup=f"Menor valor: {min_value}<br>{min_municipio}",icon=folium.Icon(color="purple", icon="arrow-down"),).add_to(m)
#########ADICIONAR NO STREAMLIT
      m.to_streamlit()
      st.markdown("""**Ano-base:** 2020
                  **Fonte(s):** Fundação Getúlio Vargas (FGV) 
                  **Fórmula:** (Renda Média da população R$/1000) 
                  **Observações:** Renda Média da População é disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV).
                  """)    
    with d2:
      st.markdown("**Indica a renda média da população (R$) para o ano de 2020**")  
      conta ('PR',renda,'Renda Média da População (R$ mil)',2020,'Renda Média da População','media','R$ mil')
      grafico('PR',renda,'Renda Média da População (R$ mil)','R$ mil')

  else:
    colored_header(label="Rendimento médio da população feminina",
                   description="Percentual do rendimento médio real mensal das mulheres em relação ao dos homens no Paraná",
                   color_name="red-70",)
    
    d1,d2 = st.columns([2,1])
    with d1:
      arq = renda
      ind = 'Rendimento médio da população feminina/masculina (%)'
      scheme = 'FisherJenks'
      k=5
      cmap='RdPu'
      fields=['Município','Rendimento médio da população feminina/masculina (%)']
      title='Rendimento médio da população feminina (%)'
      #######MERGE geojson e csv
      arq_csv = pd.read_csv(arq)
      arq_geojson = gpd.read_file(arq_g)
      data = arq_geojson.merge(arq_csv, on="Município")
#######LAT E LON CENTRAIS
      lon, lat = leafmap.gdf_centroid(data)
##########################MAPA
      style = {'Color': '#000000'} 
########MAPA INICIAL
      m = leafmap.Map(center=(lat,lon),zoom_max=16,zoom_min=11,draw_control=False,measure_control=False,fullscreen_control=False,attribution_control=True)
#######ADICIONAR O MERGE GDF
      m.add_data(data = data,column=ind,scheme=scheme,k=k,cmap=cmap,fields=fields,legend_title=title,legend_position='topright',layer_name=title)
########VALORES DE MX E MN DAS VARIAVEIS
      max_value = data[ind].max()
      min_value = data[ind].min()
      max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
      min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]
#####ADICIONAR MX E MN NO MAPA
      folium.Marker([data.loc[data[ind] == max_value, "Y"].iloc[0],data.loc[data[ind] == max_value, "X"].iloc[0]],popup=f"Maior valor: {max_value}<br>{max_municipio}",icon=folium.Icon(color="darkpurple", icon="arrow-up")).add_to(m) 
      folium.Marker([data.loc[data[ind] == min_value, "Y"].iloc[0],data.loc[data[ind] == min_value, "X"].iloc[0]],popup=f"Menor valor: {min_value}<br>{min_municipio}",icon=folium.Icon(color="purple", icon="arrow-down"),).add_to(m)
#########ADICIONAR NO STREAMLIT
      m.to_streamlit()
      st.markdown("""**Ano-base:** 2021
                  **Fonte(s):** IPARDES, RAIS  
                  **Fórmula:** (Rendimento médio da população feminina*100) /Rendimento média da população masculina   
                  **Observações:** Rendimento médio mensal é disponibilizado na RAIS (Relação Anual de Informações Sociais), obtido no banco de dados do IPARDES.
                  """)
    with d2:
      st.markdown("**Indica o percentual do rendimento médio real mensal das mulheres em relação ao dos homens celetistas e estatutários.**")  
      conta ('PR',renda,'Rendimento médio da população feminina/masculina (%)',2021,'Percentual do rendimento médio da população feminina em relação à masculina',None,None)
      grafico('PR',renda,'Rendimento médio da população feminina/masculina (%)',None)
    
