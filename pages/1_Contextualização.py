import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import leafmap.foliumap as leafmap
import pandas as pd

st.set_page_config(layout="wide")

#Selecionar a área [Radio horizontal]
st.markdown("<h3><font size='8'  color='red'>Contextualização</font></font></h3>", unsafe_allow_html=True)
#area = st.selectbox("Selecione uma área:", ("Paraná", "Núcleo Territorial Central
area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#####Arquivos
PR = "./dados/geojson/PR.geojson"
NTC = "./dados/geojson/NTC.geojson"
cont = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"


if area == "Paraná":
  def mapa_PR (arq, ind, scheme, k, cmap, fields, title, fonte, tipo= None, unidade=None, texto=None):
                #Merge
               arq_csv = pd.read_csv(arq)
               PR_geojson = gpd.read_file(PR)
               data = PR_geojson.merge(arq_csv, on="Município")
               if not isinstance(data, gpd.GeoDataFrame):
                  print("O arquivo não é um GeoDataFrame")
                  exit()
                #Mapa
               m = leafmap.Map(center=[-24.7, -51.8],
                               min_zoom=7,
                               max_zoom=13,
                               width=800,
                               height=500,
                               draw_control=False,
                               measure_control=False,
                               fullscreen_control=False,
                               attribution_control=True)
                
               m.add_data(data=data,
                          column=ind,
                          scheme=scheme,
                          k=k,
                          cmap=cmap,
                          fields=fields,
                          legend_title=title,
                          legend_position= 'Bottomright',
                          layer_name=title,
                          style={"stroke": True, "color": "#000000", "weight": 1, "fillOpacity": 1})
    
               max_value = data[ind].max()
               min_value = data[ind].min()
               max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
               min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]

               folium.Marker([data.loc[data[ind] == max_value, "Y"].iloc[0],
                              data.loc[data[ind] == max_value, "X"].iloc[0]],
                             popup=f"Maior valor: {max_value}<br>{max_municipio}",
                             icon=folium.Icon(color="green", icon="arrow-up"),
                            ).add_to(m) 
               folium.Marker([data.loc[data[ind] == min_value, "Y"].iloc[0],
                              data.loc[data[ind] == min_value, "X"].iloc[0]],
                             popup=f"Menor valor: {min_value}<br>{min_municipio}",
                             icon=folium.Icon(color="red", icon="arrow-down"),
                            ).add_to(m)

               m.to_streamlit()

               c1,c2 = st.columns([1.5,0.5])
               with c1:
                  arrow_d = '\U0001F82B'  
                  arrow_u = '\U0001F829'  
                  min_str = f"{min_municipio}"
                  max_str = f"{max_municipio}"
                  ind_mn = f"{min_value}"
                  ind_mx = f"{max_value}"
                  column_name = ind
                  if tipo == "inteiro":
                    #media = data[ind].mean().int
                    media = int(data[ind].mean())
                  else:
                    media = data[ind].mean().round(2)
            
                  st.markdown("<h3><font size='+5'> Municípios com o <font size='+5' color='green'>maior</font> e <font size='+5' color='red'>menor</font> <font size='+5'> valor:</font></h3>", unsafe_allow_html=True)
                  st.markdown(f"<p style='line-height: 0.7;'><font size='+10' color='green'>{arrow_u}</font> <font size='+5'>{max_str} = {ind_mx}</font></p>", unsafe_allow_html=True)
                  st.markdown(f"<p style='line-height: 0.5;'><font size='+10' color='red'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn}</font></p>", unsafe_allow_html=True)
                  st.markdown(f"<h3><font size='+5'> Média do {column_name} no Paraná:</font></h3>", unsafe_allow_html=True)
                  if unidade:
                     st.markdown(f"<p style='line-height: 0.2; font-weight: bold; font-size: 1.7em;'>{media} {unidade}</p>", 
                                 unsafe_allow_html=True)
                  else:
                     st.markdown(f"<p style='line-height: 0.2; font-weight: bold; font-size: 1.7em;'>{media}</p>",
                                 unsafe_allow_html=True)
               with c2:
                  texto = texto
                  fonte = fonte

  t1, t2, t3, t4, t5, t6 = st.tabs(["População residente", "Densidade demográfica", "População feminina", "População preta/parda", "Grau de urbanização", "Razão de dependência"])
  with t1:
    colored_header(label="População residente",
                   description="População residente do Paraná",
                   color_name="red-70",)
    
    Ateste = st.subheader("teste nlablanakjan")
    AAA = st.write("FONTE")
    #arq, ind, scheme, k, cmap, fields, title, fonte, tipo= None, unidade=None, texto=None
    mapa_PR(pop,'População','FisherJenks',7,'YlGnBu', ['Município','População'],'População residente do Paraná',AAA, 'inteiro', 'hab',Ateste)

  with t2:
    colored_header(label="Densidade demográfica",
                   description="Número de pessoas por km² no Paraná",
                   color_name="red-70",)
  with t3:
    colored_header(label="Grau de urbanização",
                   description="Percentual da população residente em áreas urbanas no Paraná",
                   color_name="red-70",)
  
  with t4:
    colored_header(label="População feminina",
                   description="Percentual da população feminina no Paraná",
                   color_name="red-70",)
    
  with t5:
    colored_header(label="População preta ou parda",
                   description="Percentual da população preta ou parda no Paraná",
                   color_name="red-70",)
    
  with t6:
    colored_header(label="Razão de dependência",
                   description="Percentual da população fora da idade de trabalhar em relação a população em idade de trabalhar no Paraná",
                   color_name="red-70",)
    
    

if area == "Núcleo Territorial Central":
  t1, t2, t3, t4, t5, t6 = st.tabs(["População residente", "Densidade demográfica", "População feminina", "População preta/parda", "Taxa de urbanização", "Razão de dependência"])
  with t1:
    colored_header(label="População residente",
                   description="População residente do Núcleo Territorial Central",
                   color_name="red-70",)

  with t2:
    colored_header(label="Densidade demográfica",
                   description="Número de pessoas por km² no Núcleo Territorial Central",
                   color_name="red-70",)
  with t3:
    colored_header(label="Taxa de urbanização",
                   description="Percentual da população residente em áreas urbanas no Núcleo Territorial Central",
                   color_name="red-70",)
  
  with t4:
    colored_header(label="População feminina",
                   description="Percentual da população feminina no Núcleo Territorial Central",
                   color_name="red-70",)
    
  with t5:
    colored_header(label="População preta ou parda",
                   description="Percentual da população preta ou parda no Núcleo Territorial Central",
                   color_name="red-70",)
    
  with t6:
    colored_header(label="Razão de dependência",
                   description="Percentual da população fora da idade de trabalhar em relação a população em idade de trabalhar no Núcleo Territorial Central",
                   color_name="red-70",)
    
    


