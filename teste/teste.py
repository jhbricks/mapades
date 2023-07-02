def mapa (area, arq, ind, scheme, k, cmap, fields, title, tipo= None, unidade=None, fonte=None):
  
  if area == 'PR':
       arq_g= "./dados/geojson/PR.geojson"
  else:
       arq_g = "./dados/geojson/NTC.geojson"

  arq_csv = pd.read_csv(arq)
  arq_geojson = gpd.read_file(arq_g)
  data = arq_geojson.merge(arq_csv, on="Município")

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
