import streamlit as st
from streamlit_folium import folium_static
import folium
import leafmap
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
import numpy as np
import plotly.graph_objects as go



########################ARQUIVOS CSV E GEOJSON
#contexto = "./dados/csv/contexto.csv"
#pop = "./dados/csv/pop_2021.csv"
#renda = "./dados/csv/renda.csv"
#riqueza = "./dados/csv/riqueza.csv"

#######################DICIONÁRIO DEF MAPA
#area = 'PR' ou 'NTC'
#arq = arquivo csv, ex: contexto
#ind = indicador conforme está no arquivo csv, ex: 'População'
#scheme = classificação, lista no leafmap, ex: 'FisherJenks'
#k = número de classes
#cmap = paleta de cores, lista no leafmap, ex: 'Oranges'
#fields = variaveis que aparecem no popup, ex: ['Município','População']
#title = título do mapa e da legenda

@st.cache_data
def mapa (area,arq,ind,scheme,k,cmap,fields,title):
######encaminha o geojson da area
  if area == 'PR':
    arq_g = "./dados/geojson/PR.geojson"
  elif area == 'NTC':
    arq_g = "./dados/geojson/NTC.geojson"
  else:
    arq_g = area

#######MERGE geojson e csv
  arq_csv = pd.read_csv(arq)
  arq_geojson = gpd.read_file(arq_g)
  data = arq_geojson.merge(arq_csv, on="Município")

#######LAT E LON CENTRAIS
  ponto_central = arq_geojson.geometry.centroid
  abc = ponto_central.iloc[0].y
  lon = ponto_central.iloc[0].x
  lat = (abc + 55)
  st.markdown(f"<p><font size='+2' color='darkpurple'> lat ={lat} long = {lon}</font></p>", unsafe_allow_html=True)
    
  if not isinstance(data,gpd.GeoDataFrame):
    print("O arquivo não é um GeoDataFrame")
    exit()

  style = {"color":"#000000","weight":1, "fillOpacity":0}
##########################MAPA
########MAPA INICIAL
  m = leafmap.Map(center=[(lat+15),lon],
            		  draw_control=False,
                  measure_control=False,
                  fullscreen_control=False,
                  attribution_control=True)

  
  m.add_basemap("Esri.WorldGrayCanvas") 
  
#######ADICIONAR O MERGE GDF


  m.add_data(data = data,
             column=ind,
             scheme=scheme,
             k=k,
             cmap=cmap,
             fields=fields,
             legend_title=title,
             legend_position='topright',
             layer_name=title,
             )

  geojson_layer = folium.GeoJson(
    data,
    name = area,
    style_function=lambda feature: style,
    tooltip=folium.GeoJsonTooltip(fields=fields)).add_to(m)
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
	

#######################GRÁFICO

#arq = arquivo csv, ex: contexto
#ind = indicador conforme está no arquivo csv, ex: 'População'
#un = unidade, ex; 'Habitantes'

def grafico (area,arq,ind,un):
  if area == 'PR':
    arq_g = "./dados/geojson/PR.geojson"
  elif area == 'NTC':
    arq_g = "./dados/geojson/NTC.geojson"
  else:
    arq_g = area
    
#######MERGE geojson e csv
  arq_csv = pd.read_csv(arq)
  arq_geojson = gpd.read_file(arq_g)
  data = arq_geojson.merge(arq_csv, on="Município")


  highest = data.nlargest(3, ind)
  lowest = data.nsmallest(3, ind)

  fig = go.Figure()

#  colors = {'Maiores valores': '#A70005', 'Menores valores': '#FF858A'}
  colors = {'Maiores valores': '#563565', 'Menores valores': '#ab4397'}

  fig.add_trace(go.Bar(x=highest['Município'],
                       y=highest[ind],
                       name='Maiores valores',
                       marker=dict(color=colors['Maiores valores'])
                       ))
  fig.add_trace(go.Bar(x=lowest['Município'],
                        y=lowest[ind],
                        name='Menores valores',
                        marker=dict(color=colors['Menores valores']) 
                        ))
  
  fig.update_xaxes(title_text='Município')
  fig.update_yaxes(title_text=un)
  fig.update_layout(legend=dict(orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1))
  fig.update_layout(height=400,title_text='Top 3 dos maiores e menores valores do indicador')

  
  st.plotly_chart(fig, use_container_width=True)



#############Mapa localização

def local (area):
  style = lambda x: {'color': 'black', 'fillColor': '#66c2a5', 'weight': 1}  #Brasil (verde)
  style1 = lambda x: {'color': 'black', 'fillColor': '#fc8d62', "weight": 1} #destaque PR  (rosa)
  style2 = lambda x: {'color': 'black', 'fillColor': '#8da0cb', "weight": 1.5, 'fillOpacity':0.7} #destaque NTC  (azul)
  def style_function(feature):
    if feature['properties']['Estado'] == 'Paraná':
        return {'color': 'black', 'fillColor': '#fc8d62', 'weight': 1}
    else:
        return {'color': 'black', 'fillColor': '#66c2a5', 'weight': 1}
  if area == 'BR - PR':
    url1= './dados/geojson/BR.geojson'
    gdf = gpd.read_file(url1)
    centroid = gdf.geometry.centroid
    lon, lat = centroid.x[0], centroid.y[0]
    m2 = leafmap.Map(center=(lat, lon), draw_control=False, measure_control=False, fullscreen_control=False, attribution_control=True)
    m2.add_basemap("Google Terrain")
    m2.add_geojson(url1, fields = ['Estado'], layer_name= 'Brasil', style_function= style_function)
    legend_dict = {'Brasil': '#66c2a5','Paraná' : '#fc8d62'}
    m2.add_legend(title = 'Legenda', legend_dict= legend_dict, position='bottomleft')
    m2.to_streamlit()
  
  elif area == 'PR':
    url1= './dados/geojson/BR.geojson'
    url= './dados/geojson/PR.geojson'
    gdf = gpd.read_file(url)
    centroid = gdf.geometry.centroid
    lon, lat = centroid.x[0], centroid.y[0]
    m = leafmap.Map(center=(lat, lon), zoom=10, draw_control=False, measure_control=False, fullscreen_control=False, attribution_control=True)
    m.add_basemap("Google Terrain")
    m.add_geojson(url1, layer_name='Brasil', style_function=style_function)
    m.add_geojson(url, fields=['Município'], layer_name='Paraná', style_function=style1)
    legend_dict = {'Brasil': '#66c2a5','Paraná' : '#fc8d62'}
    m.add_legend(title = 'Legenda', legend_dict= legend_dict, position='bottomleft')
    m.to_streamlit()
  
  elif area == 'BR - NTC':
    url1= './dados/geojson/BR.geojson'
    url = './dados/geojson/NTC.geojson'
    gdf = gpd.read_file(url1)
    centroid = gdf.geometry.centroid
    lon, lat = centroid.x[0], centroid.y[0]
    m2 = leafmap.Map(center=(lat, lon), draw_control=False, measure_control=False, fullscreen_control=False, attribution_control=True)
    m2.add_basemap("Google Terrain")
    m2.add_geojson(url1, fields = ['Estado'], layer_name= 'Brasil', style_function= style_function)
    m2.add_geojson(url, fields=['Município'], layer_name='Núcleo Territorial Central de Curitiba', style_function = lambda x: {'color': '#8da0cb', 'fillColor': '#8da0cb', "weight": 1.5, 'fillOpacity':0.7} )
    legend_dict = {'Brasil': '#66c2a5','Paraná' : '#fc8d62','Núcleo Territorial Central de Curitiba': '#8da0cb'}
    m2.add_legend(title = 'Legenda', legend_dict= legend_dict, position='bottomleft')
    m2.to_streamlit()

  elif area == 'NTC':
    url = './dados/geojson/NTC.geojson'
    url1= './dados/geojson/BR.geojson'
    pr= './dados/geojson/PR.geojson'
    a = gpd.read_file(url)
    centroid = a.geometry.centroid
    lon, lat = centroid.x[0], centroid.y[0]
    m = leafmap.Map(center=(lat, lon),draw_control=False, measure_control=False, fullscreen_control=False, attribution_control=True)
    m.add_basemap("Google Terrain")
    m.add_geojson(url1, layer_name='Brasil', style_function=style_function)
    m.add_geojson(pr, fields=['Município'], layer_name='Paraná', style_function=style1)
    m.add_geojson(url, fields=['Município'], layer_name='Núcleo Territorial Central de Curitiba', style_function = style2)
    legend_dict = {'Brasil': '#66c2a5','Paraná' : '#fc8d62', 'Núcleo Territorial Central de Curitiba': '#8da0cb'}
    m.add_legend(title = 'Legenda', legend_dict= legend_dict, position='bottomleft')
    m.to_streamlit()
