import streamlit as st
from streamlit_extras.colored_header import colored_header

st.set_page_config(layout="wide")

#Selecionar a área [Radio horizontal]
st.markdown("<h3><font size='8'  color='red'>Renda</font></font></h3>", unsafe_allow_html=True)
area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#Arquivos


if area == "Paraná":
  t1, t2, t3, t4 = st.tabs(["Coeficiente de Gini", "Renda da população feminina", "Renda média da população", "Renda dos declarantes do IRPF"])
  with t1:
    colored_header(label="Coeficiente de Gini",
                   description="Coeficiente de Gini renda domiciliar per capita no Paraná",
                   color_name="red-70",)


    df_csv = pd.read_csv(ren)
    gdf_geojson = gpd.read_file(PR)
    merged_gdf = gdf_geojson.merge(df_csv, on="Município")
    if not isinstance(merged_gdf, gpd.GeoDataFrame):
      print("merged_gdf não é um GeoDataFrame")
      exit()
      
    max_value = merged_gdf["GINI"].max()
    min_value = merged_gdf["GINI"].min()
    max_municipio = merged_gdf.loc[merged_gdf["GINI"] == max_value, "Município"].iloc[0]
    min_municipio = merged_gdf.loc[merged_gdf["GINI"] == min_value, "Município"].iloc[0]
    m = leafmap.Map(center=[-24.7, -51.8],
                    zoom= 7,
                    draw_control=False,
                    measure_control=False,
                    fullscreen_control=False,
                    attribution_control=True)
    folium.Marker(
      [merged_gdf.loc[merged_gdf["GINI"] == max_value, "Y"].iloc[0],
       merged_gdf.loc[merged_gdf["GINI"] == max_value, "X"].iloc[0]],
      popup=f"Maior valor Gini: {max_value}<br>{max_municipio}",
      icon=folium.Icon(color="green", icon="arrow-up"),
    ).add_to(m)
    folium.Marker(
      [merged_gdf.loc[merged_gdf["GINI"] == min_value, "Y"].iloc[0],
       merged_gdf.loc[merged_gdf["GINI"] == min_value, "X"].iloc[0]],
      popup=f"Menor valor Gini: {min_value}<br>{min_municipio}",
      icon=folium.Icon(color="red", icon="arrow-down"),
    ).add_to(m)
    m.add_data(
      merged_gdf,
      column='GINI',
      scheme='FisherJenks',
      k = 3,
      cmap= 'RdPu',
      fields= ['Município','GINI'],
      legend_title='Índice de Gini da Renda Domiciliar per Capita (2010)',
      legend_position = "bottomright",
      layer_name = "'Índice de Gini da Renda Domiciliar per Capita (2010)",
      style={"stroke": True, "color": "#000000", "weight": 1, "fillOpacity": 1}
    )
    m.to_streamlit()

  
  with t2:
    colored_header(label="Rendimento médio da população feminina",
                   description="Percentual do rendimento médio real mensal das mulheres em relação ao dos homens no Paraná",
                   color_name="red-70",)


  
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
