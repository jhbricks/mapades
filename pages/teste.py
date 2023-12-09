import leafmap.leafmap as leafmap
import geopandas as gpd
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

a = "./dados/imagem/icon/renda.png"

img = Image.open(a)
st.button(st.image(img))

html = f"<a href='{'https://mapadesigualdade.streamlit.app/Renda'}'><img src='data:image/png;base64,{a}'></a>"
st.markdown(html, unsafe_allow_html=True)