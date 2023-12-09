import leafmap.leafmap as leafmap
import geopandas as gpd
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

a = "./dados/imagem/icon/renda.png"

#img = Image.open(a)
#st.button(st.image(img))



st.sidebar.markdown(
    """<a href="https://mapadesigualdade.streamlit.app/Renda">
    <img src="data:image/png;base64,{}" width="50">
    </a>""".format(
        base64.b64encode(open(a, "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)