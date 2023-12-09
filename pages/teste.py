import leafmap.leafmap as leafmap
import geopandas as gpd
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

a = "./dados/imagem/icon/renda.png"



html = f"<a href='{'https://mapadesigualdade.streamlit.app/Renda'}'><img src='data:./dados/imagem/icon/renda.png;base64,{image_base64}'></a>"
st.markdown(html, unsafe_allow_html=True)