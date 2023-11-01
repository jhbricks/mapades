import streamlit as st
from streamlit_folium import folium_static
import folium
import leafmap
import leafmap.foliumap as leafmap
import geopandas as gpd

#url = geojson de destaque

def local (url,local,fields,layer,url):
    style1 = lambda x: {'color': 'black', 'fillColor': '#fc8d62', "weight": 1} #destaque
    style2 = lambda x: {'color': 'black', 'fillColor': '#66c2a5', "weight": 1}

    def style_function(feature):
    if feature['properties']['nome'] == local:
        return {'color': 'black', 'fillColor': '#fc8d62', 'weight': 1}
    else:
        return {'color': 'black', 'fillColor': '#66c2a5', 'weight': 1}

    gdf = gpd.read_file(url)
    centroid = gdf.geometry.centroid
    lon, lat = centroid.x[0], centroid.y[0]
    m = leafmap.Map(center=(lat, lon), zoom=10, draw_control=False, measure_control=False, fullscreen_control=False, attribution_control=True)
    m.add_geojson(url1, style_function=style_function)
    m.add_geojson(url, fields=fields, layer_name=layer, style_function=style1)