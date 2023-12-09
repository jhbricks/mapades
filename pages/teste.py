import leafmap.leafmap as leafmap
import geopandas as gpd
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

a = "./dados/imagem/icon/renda.png"

img = Image.open(a)
st.button(st.image(img))