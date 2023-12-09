import leafmap.leafmap as leafmap
import geopandas as gpd
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

a = "./dados/imagem/icon/renda.png"

img = Image.open(a)
st.button(st.image(img))

button_style = f"""
                        <style>
                        div.stButton > button {{
                            background: url(data:a;base64,{encoded_image}) no-repeat;
                            background-size: cover;
                            background-position: center;
                            height: 16em;
                            width: 24em;
                            box-shadow: 10px 10px 5px grey;
                            margin: 15px;
                        }}
                        </style>
                        """
st.markdown(button_style, unsafe_allow_html=True)