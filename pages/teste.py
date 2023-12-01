import leafmap.leafmap as leafmap
import geopandas as gpd
import pandas as pd

arq_g = "./dados/geojson/PR.geojson"
arq = "./dados/csv/contexto.csv"

arq_csv = pd.read_csv(arq)
arq_geojson = gpd.read_file(arq_g)
data = arq_geojson.merge(arq_csv, on="Município")

m = leafmap.Map()
m.add_heatmap(
    data,
    latitude="Y",
    longitude='X',
    value="Densidade Demográfica (hab/km²)",
    name="Heat map",
    radius=20,)

m.to_streamlit()