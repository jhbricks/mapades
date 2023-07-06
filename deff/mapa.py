import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import leafmap.foliumap as leafmap
import pandas as pd
import numpy as np

######ARQUIVOS
contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"
renda = "./dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"


#area = 'PR' ou 'NTC'
#arq = arquivo csv, ex: contexto
#ind = indicador conforme está no arquivo csv, ex: 'População'
#scheme = classificação, lista no leafmap, ex: 'FisherJenks'
#k = número de classes
#cmap = paleta de cores, lista no leafmap, ex: 'Oranges'
#fields = variaveis que aparecem no popup, ex: ['Município','População']
#title = título do mapa e da legenda

def mapa (area, arq, ind, scheme, k, cmap, fields, title):

	if area == 'PR':
		arq_g= "./dados/geojson/PR.geojson"
	else:
		arq_g = "./dados/geojson/NTC.geojson"

  #####merge geojson com csv
	arq_csv = pd.read_csv(arq)
	arq_geojson = gpd.read_file(arq_g)
	data = arq_geojson.merge(arq_csv, on="Município")

  ### adicionar colunas com calculos para a categoria riqueza
	if ind == 'Renda Média da População (R$ mil)':
		data['Renda Média da População (R$ mil)'] = ((data['Renda Média da População (R$)']) / 1000).round(2).astype(float)
	elif ind == 'Renda Média dos Declarantes (R$ mil)':
		data['Renda Média dos declarantes (R$ mil)'] = ((data['Renda Média dos Declarantes (R$)']) / 1000).round(2).astype(float)
	elif ind == 'Patrimônio líquido médio da população (R$ milhões)':
		data['Patrimônio líquido médio da população (R$ milhões)'] = (data['Patrimônio liquido médio da população (R$)'] / 1000000).round(2).astype(float)
		data['Patrimônio líquido médio dos declarantes (R$ milhões)'] = (data['Patrimônio liquido médio dos declarantes (R$)'] / 1000000).round(2).astype(float)
	else:
		data = data 

  #Lat, Lon centrais
	ponto_central = arq_geojson.geometry.centroid
	lat = ponto_central.iloc[0].y
	lon = ponto_central.iloc[0].x
 
	if not isinstance(data, gpd.GeoDataFrame):
		print("O arquivo não é um GeoDataFrame")
		exit()
    
 ######################Mapa
	m = leafmap.Map(center=[lat, lon],
			zoom = zoom_to_layer,
		        draw_control=False,
		        measure_control=False,
		        fullscreen_control=False,
		        attribution_control=True)
  #zoom to layer
	if zoom == zoom_to_layer:
		bounds = data.to_crs(epsg="4326").bounds
		west = np.min(bounds["minx"])
		south = np.min(bounds["miny"])
		east = np.max(bounds["maxx"])
		north = np.max(bounds["maxy"])
		self.fit_bounds([[south, east], [north, west]]  
  
	m.add_data(data=data,
		   column=ind,
               	   scheme=scheme,
                   k=k,
                   cmap=cmap,
                   fields=fields,
                   legend_title=title,
                   legend_position= 'Bottomright',
                   layer_name=title,
                   style= lambda x: {"stroke": True,
				     "color": "#000000",
                		     "weight": 1,
                                     "fillOpacity": 1,})

  #VALORES MX E MN 
	max_value = data[ind].max()
	min_value = data[ind].min()
	max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
	min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]

	folium.Marker([data.loc[data[ind] == max_value, "Y"].iloc[0],
		       data.loc[data[ind] == max_value, "X"].iloc[0]],
                      popup=f"Maior valor: {max_value}<br>{max_municipio}",
                      icon=folium.Icon(color="darkblue", icon="arrow-up"),
		     ).add_to(m) 
	folium.Marker([data.loc[data[ind] == min_value, "Y"].iloc[0],
	               data.loc[data[ind] == min_value, "X"].iloc[0]],
                      popup=f"Menor valor: {min_value}<br>{min_municipio}",
                      icon=folium.Icon(color="lightblue", icon="arrow-down"),
                     ).add_to(m)

  #add_geojson(arq_g,area,style_function = lambda x: style_data)  
   
	m.to_streamlit()
  
		return m 


def mx_mn (area,arq,ind,unidade=None) :

    if area == 'PR':
       arq_g= "./dados/geojson/PR.geojson"
    else:
       arq_g = "./dados/geojson/NTC.geojson"

    arq_csv = pd.read_csv(arq)
    arq_geojson = gpd.read_file(arq_g)
    data = arq_geojson.merge(arq_csv, on="Município")
  
    max_value = data[ind].max()
    min_value = data[ind].min()
    max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
    min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]

    arrow_d = '\U0001F82B'  
    arrow_u = '\U0001F829'  
    min_str = f"{min_municipio}"
    max_str = f"{max_municipio}"
    ind_mn = f"{min_value}"
    ind_mx = f"{max_value}"


    st.markdown("<h3><font size='+5'> Municípios com o <font color='darkblue'>maior</font> e <font color='lightblue'>menor</font> valor:</font></h3>", unsafe_allow_html=True)
    if unidade:
      st.markdown(f"""<p><font size='+7' color='#6612b8'>{arrow_u}</font> <font size='+5'>{max_str} = {ind_mx} {unidade}</font>  
      <font size='+7' color='#ba2db4'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn} {unidade}</font></p>""", unsafe_allow_html=True)
      
      #st.markdown(f"<p><font size='+5' color='#ba2db4'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn} {unidade}</font></p>", unsafe_allow_html=True)
    else:
      st.markdown(f"<p><font size='+7' color='#6612b8'>{arrow_u}</font> <font size='+5'>{max_str} = {ind_mx} </font></p>", unsafe_allow_html=True)
      #st.markdown(f"<p><font size='+5' color='#ba2db4'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn} </font></p>", unsafe_allow_html=True)
      #st.markdown(f"<p style='line-height: 0.7;'><font size='+10' color='#6612b8'>{arrow_u}</font> <font size='+5'>{max_str} = {ind_mx}</font></p>", unsafe_allow_html=True)
      st.markdown(f"<p style='line-height: 0.5;'><font size='+7' color='#ba2db4'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn}</font></p>", unsafe_allow_html=True)


def conta (area,arq,ind,ano,calc=None,tipo=None,unidade=None):
    
    if area == 'PR':
       arq_g= "./dados/geojson/PR.geojson"
       nome = 'Paraná'
    else:
       arq_g = "./dados/geojson/NTC.geojson"
       nome = 'Núcleo Territorial Central'

    arq_csv = pd.read_csv(arq)
    arq_geojson = gpd.read_file(arq_g)
    data = arq_geojson.merge(arq_csv, on="Município")
    somaT = data['PCT'].sum()
  
    if ind == "Densidade Demográfica (hab/km²)":
      somapop = data['População'].sum()
      somaarea = data['Areakm2'].sum()
      DEM = (somapop / somaarea).round().astype(int)
      st.markdown(f"<h3><font size='+5'> Densidade demográfica no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
      st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {DEM} </font> habitantes por km²</font></h3>", unsafe_allow_html=True)
    elif ind == 'Grau de Urbanização (%)':
      somaU = data['PCU'].sum()
      TU = (somaU*100)/somaT
      st.markdown(f"<h3><font size='+5'> Grau de Urbanização no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
      st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {TU} </font> %</font></h3>", unsafe_allow_html=True)
    elif ind == 'População feminina (%)':
      somaF = data['PCF'].sum()
      TF = (somaF*100)/somaT
      st.markdown(f"<h3><font size='+5'> População feminina total no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
      st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {TF} </font> %</font></h3>", unsafe_allow_html=True)
    elif ind == 'População preta ou parda (%)':
      somaPR=data['PCPR'].sum()
      somaPA=data['PCPA'].sum()
      TPP= ((somaPR + somaPA)*100)/somaT
      st.markdown(f"<h3><font size='+5'> População preta ou parda total no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
      st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {TPP} </font> %</font></h3>", unsafe_allow_html=True)
    elif ind == 'Razão de Dependência (%)':
      soma65 = data['PP65'].sum()
      soma14 = data['PP14'].sum()
      somaPT = data['PPT'].sum()
      RD = ((soma65 + soma14)*100)/somaPT
      st.markdown(f"<h3><font size='+5'> Razão de dependência no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
      st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {RD} </font> %</font></h3>", unsafe_allow_html=True)
    else:
      if tipo == "md_int":
        media = int(data[ind].mean())
      elif tipo == "soma":
        media = data[ind].sum()
      else:
        media = data[ind].mean().round(2)
      st.markdown(f"<h3><font size='+5'> {calc} em {ano}:</font></h3>", unsafe_allow_html=True)
      st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {media} {unidade}</font></h3>", unsafe_allow_html=True)
      #st.markdown(f"<h3><font size='+5'> {calc}:</font></h3>", unsafe_allow_html=True)  
      #st.markdown(f"<p style='font-weight: bold;'> <font size: '+5'>{media} {unidade}</font></p>", unsafe_allow_html=True)
