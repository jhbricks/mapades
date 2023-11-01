import streamlit as st
from streamlit_folium import folium_static
import folium
import leafmap
import leafmap.foliumap as leafmap
import geopandas as gpd


br= './dados/geojson/1990.geojson'
pr= './dados/geojson/PR.geojson'
ntc= './dados/geojson/NTC.geojson'


#url = geojson da área, ex: 'br','pr'
#fields = coluna, ex: 'nome', 'Município'
#destaque = área de destaque, ex: 'Paraná'
#layer = título do layer, ex: 'Brasil'
#dict = dicionário da legenda, ex: 
def estado (url,destaque,fields,layer):
    style = lambda x: {'color': 'black', 'fillColor': '#66c2a5', 'weight': 1}  #Brasil (verde)
    style1 = lambda x: {'color': 'black', 'fillColor': '#fc8d62', "weight": 1} #destaque PR  (rosa)
    style2 = lambda x: {'color': 'black', 'fillColor': '#8da0cb', "weight": 1.5, 'fillOpacity':0.7} #destaque NTC  (azul)

    verde = '#66c2a5'
    rosa = '#fc8d62'
    azul = '#8da0cb'

    def style_function(feature):
      if feature['properties'][fields] == destaque:
            return style1
      else:
            return style
    
    gdf = gpd.read_file(url)
    centroid = gdf.geometry.centroid
    lon, lat = centroid.x[0], centroid.y[0]
    m = leafmap.Map(center=(lat, lon), draw_control=False, measure_control=False, fullscreen_control=False, attribution_control=True)
    m.add_geojson(url, fields = [fields], layer_name= layer, style_function= style_function)
    legend_dict = {layer: '#66c2a5',destaque: '#fc8d62'}
    m.add_legend(title = 'Legenda', legend_dict= legend_dict, position='bottomleft')
    m.to_streamlit()

#url: geojson de destaque, ex: 'pr'
#url1: geojson da área, ex: 'br'
#fields1: campo do url
def local_2 (url, url1, destaque,fields1,fields,layer,layer1):
    style = lambda x: {'color': 'black', 'fillColor': '#66c2a5', 'weight': 1}  #Brasil (verde)
    style1 = lambda x: {'color': 'black', 'fillColor': '#fc8d62', "weight": 1} #destaque PR  (rosa)
    style2 = lambda x: {'color': 'black', 'fillColor': '#8da0cb', "weight": 1.5, 'fillOpacity':0.7} #destaque NTC  (azul)

    verde = '#66c2a5'
    rosa = '#fc8d62'
    azul = '#8da0cb'

    def style_function(feature):
      if feature['properties'][fields] == destaque:
            return style1
      else:
            return style
          
    #url1= './dados/geojson/1990.geojson'
    #url= './dados/geojson/PR.geojson'
    
    gdf = gpd.read_file(url)
    centroid = gdf.geometry.centroid
    lon, lat = centroid.x[0], centroid.y[0]
    
    m = leafmap.Map(center=(lat, lon), zoom=10, draw_control=False, measure_control=False, fullscreen_control=False, attribution_control=True)
    m.add_geojson(url1, layer_name=layer1, style_function=style_function)
    m.add_geojson(url, fields=[fields1], layer_name=layer, style_function=style1)
    legend_dict = {layer1: '#66c2a5', layer : '#fc8d62'}
    m.add_legend(title = 'Legenda', legend_dict= legend_dict, position='bottomleft')
    m.to_streamlit()

#url: geojson de destaque, ex: 'ntc'
#url1: geojson da área, ex: 'br'
#url2: geojson da área, ex: 'pr'

style = lambda x: {'color': 'black', 'fillColor': '#66c2a5', 'weight': 1}  #Brasil (verde)
style1 = lambda x: {'color': 'black', 'fillColor': '#fc8d62', "weight": 1} #destaque PR  (rosa)
style2 = lambda x: {'color': 'black', 'fillColor': '#8da0cb', "weight": 1.5, 'fillOpacity':0.7} #destaque NTC  (azul)

def local_3 (url, url1,url2 destaque,fields,layer,layer1):
    def style_function(feature):
      if feature['properties'][fields] == destaque:
            return style1
      else:
            return style
    
   # url = './dados/geojson/NTC.geojson'
    #url1= './dados/geojson/1990.geojson'
    #url2= './dados/geojson/PR.geojson'
    a = gpd.read_file(url)
    centroid = a.geometry.centroid
    lon, lat = centroid.x[0], centroid.y[0]
    
    m = leafmap.Map(center=(lat, lon),draw_control=False, measure_control=False, fullscreen_control=False, attribution_control=True)
    
    m.add_geojson(url1, layer_name=layer1, style_function=style_function)
    m.add_geojson(url2, fields=[fields2], layer_name=layer2', style_function=style1)
    m.add_geojson(url, fields=[fields], layer_name='layer, style_function = style2 )
                  
    legend_dict = {layer1: '#66c2a5',layer2 : '#fc8d62', layer: '#8da0cb'}
    m.add_legend(title = 'Legenda', legend_dict= legend_dict, position='bottomleft')
    
    m.to_streamlit()



