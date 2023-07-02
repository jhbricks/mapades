import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import leafmap.foliumap as leafmap
import pandas as pd

st.set_page_config(layout="wide")

#Selecionar a área [Radio horizontal]
st.markdown("<h3><font size='8'  color='red'>Renda</font></font></h3>", unsafe_allow_html=True)
area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#Arquivos
PR = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/PR.geojson'
NTC = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson'
ren = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/csv/renda.csv'

#Unir o csv e o geojson
ren_csv = pd.read_csv(ren)
PR_geojson = gpd.read_file(PR)
ren_PR = PR_geojson.merge(ren_csv, on="Município")
if not isinstance(ren_PR, gpd.GeoDataFrame):
  print("merged_gdf não é um GeoDataFrame")
  exit()

if area == "Paraná":
  t1, t2, t3, t4 = st.tabs(["Coeficiente de Gini", "Renda da população feminina", "Renda média da população", "Renda dos declarantes do IRPF"])
  m = leafmap.Map(center=[-24.7, -51.8],
                  min_zoom= 7,
                  max_zoom = 13,
                  width = 800,
                  height = 600,
                  draw_control=False,
                  measure_control=False,
                  fullscreen_control=False,
                  attribution_control=True)
  
  with t1:
    colored_header(label="Coeficiente de Gini",
                   description="Coeficiente de Gini renda domiciliar per capita no Paraná",
                   color_name="red-70",)

     
    max_value = ren_PR["Coeficiente de Gini"].max()
    min_value = ren_PR["Coeficiente de Gini"].min()
    max_municipio = ren_PR.loc[ren_PR["Coeficiente de Gini"] == max_value, "Município"].iloc[0]
    min_municipio = ren_PR.loc[ren_PR["Coeficiente de Gini"] == min_value, "Município"].iloc[0]

    folium.Marker(
      [ren_PR.loc[ren_PR["Coeficiente de Gini"] == max_value, "Y"].iloc[0],
       ren_PR.loc[ren_PR["Coeficiente de Gini"] == max_value, "X"].iloc[0]],
      popup=f"Maior valor: {max_value}<br>{max_municipio}",
      icon=folium.Icon(color="green", icon="arrow-up"),
    ).add_to(m)
    folium.Marker(
      [ren_PR.loc[ren_PR["Coeficiente de Gini"] == min_value, "Y"].iloc[0],
       ren_PR.loc[ren_PR["Coeficiente de Gini"] == min_value, "X"].iloc[0]],
      popup=f"Menor valor: {min_value}<br>{min_municipio}",
      icon=folium.Icon(color="red", icon="arrow-down"),
    ).add_to(m)
    m.add_data(
      ren_PR,
      column='Coeficiente de Gini',
      scheme='FisherJenks',
      k = 3,
      cmap= 'RdPu',
      fields= ['Município','Coeficiente de Gini'],
      legend_title='Coeficiente de Gini da renda domiciliar per capita',
      legend_position = "bottomright",
      layer_name = "'Coeficiente de Gini da Renda Domiciliar per Capita",
      style={"stroke": True, "color": "#000000", "weight": 1, "fillOpacity": 1}
    )
    
    m.to_streamlit()

  
  with t2:
    colored_header(label="Rendimento médio da população feminina",
                   description="Percentual do rendimento médio real mensal das mulheres em relação ao dos homens no Paraná",
                   color_name="red-70",)

    c1, c2 = st.columns(2)

    with c1:
      max_value = ren_PR["Coeficiente de Gini"].max()
      min_value = ren_PR["Coeficiente de Gini"].min()
      max_municipio = ren_PR.loc[ren_PR["Coeficiente de Gini"] == max_value, "Município"].iloc[0]
      min_municipio = ren_PR.loc[ren_PR["Coeficiente de Gini"] == min_value, "Município"].iloc[0]

      folium.Marker(
        [ren_PR.loc[ren_PR["Coeficiente de Gini"] == max_value, "Y"].iloc[0],
         ren_PR.loc[ren_PR["Coeficiente de Gini"] == max_value, "X"].iloc[0]],
        popup=f"Maior valor: {max_value}<br>{max_municipio}",
        icon=folium.Icon(color="green", icon="arrow-up"),
      ).add_to(m)
      folium.Marker(
        [ren_PR.loc[ren_PR["Coeficiente de Gini"] == min_value, "Y"].iloc[0],
         ren_PR.loc[ren_PR["Coeficiente de Gini"] == min_value, "X"].iloc[0]],
        popup=f"Menor valor: {min_value}<br>{min_municipio}",
        icon=folium.Icon(color="red", icon="arrow-down"),
      ).add_to(m)
      m.add_data(
        ren_PR,
        column='Coeficiente de Gini',
        scheme='FisherJenks',
        k = 3,
        cmap= 'RdPu',
        fields= ['Município','Coeficiente de Gini'],
        legend_title='Coeficiente de Gini da renda domiciliar per capita',
        legend_position = "bottomright",
        layer_name = "'Coeficiente de Gini da Renda Domiciliar per Capita",
        style={"stroke": True, "color": "#000000", "weight": 1, "fillOpacity": 1}
      )
      m.to_streamlit()

    with c2:
      st.markdown("<h3><font color='black'>Municípios com o </font> <font color='green'>maior</font>  <font color='black'>e</font> <font color='red'>menor</font> <font color='black'>valor:</font></h3>",
                  unsafe_allow_html=True)
      arrow_d = '\U0001F82B'  
      arrow_u = '\U0001F829'  
      min_str = f"{min_municipio}"
      max_str = f"{max_municipio}"
      ind_mn = f"{min_value}"
      ind_mx = f"{max_value}"
      st.markdown(f"<p style='line-height: 0.7;'><font size='+14' color='green'>{arrow_u}</font> <font color='black'>{max_str} = {ind_mx}</font></p>",
                    unsafe_allow_html=True)
      st.markdown(f"<p style='line-height: 0.5;'><font size='+14' color='red'>{arrow_d}</font> <font color='black'>{min_str} = {ind_mn}</font></p>",
                    unsafe_allow_html=True)
      media = merged_gdf["Índice de Gini da Renda Domiciliar per Capita (2010)"].mean().round(2)
      st.markdown(f" Média: {media}")
  
  with t3:
    colored_header(label="Renda média da população",
                   description="Renda média da população no Paraná",
                   color_name="red-70",)


  with t4:
    colored_header(label="Renda dos declarantes do IRPF",
                   description="Renda média dos declarentes do IRPF no Paraná",
                   color_name="red-70",)




if area == "Núcleo Territorial Central":
  
  t1, t2, t3, t4 = st.tabs(["Coeficiente de Gini", "Renda da população feminina", "Renda média da população", "Renda dos declarantes do IRPF"])
  with t1:
    colored_header(label="Coeficiente de Gini",
                   description="Coeficiente de Gini renda domiciliar per capita no Núcleo Territorial Central",
                   color_name="red-70",)

  
  with t2:
    colored_header(label="Rendimento médio da população feminina",
                   description="Percentual do rendimento médio real mensal das mulheres em relação ao dos homens no Núcleo Territorial Central",
                   color_name="red-70",)


  
  with t3:
    colored_header(label="Renda média da população",
                   description="Renda média da população no Núcleo Territorial Central",
                   color_name="red-70",)


  with t4:
    colored_header(label="Renda dos declarantes do IRPF",
                   description="Renda média dos declarentes do IRPF no Núcleo Territorial Central",
                   color_name="red-70",)
