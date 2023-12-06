import leafmap.leafmap as leafmap
import geopandas as gpd
import pandas as pd
import plotly.express as px

arq_g = "./dados/geojson/PR.geojson"
arq = "./dados/csv/contexto.csv"

arq_csv = pd.read_csv(arq)
arq_geojson = gpd.read_file(arq_g)
data = arq_geojson.merge(arq_csv, on="Município")

ind = "População"

max_value = data[ind].max()
min_value = data[ind].min()
max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]

media = data[ind].mean().round(2)

data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')
fig.show()