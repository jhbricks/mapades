import leafmap.leafmap as leafmap
import geopandas as gpd
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

a = "./dados/imagem/icon/renda.png"

#img = Image.open(a)
#st.button(st.image(img))



import streamlit as st
import base64

# Carregue a imagem que você deseja usar como botão
caminho_imagem = "./dados/imagem/icon/renda.png"
imagem_base64 = base64.b64encode(open(caminho_imagem, "rb").read()).decode()

# Adicione um link para outra página quando a imagem for clicada
link_para_outra_pagina = "https://mapadesigualdade.streamlit.app/Renda"

# Use st.markdown para exibir a imagem como um link clicável
st.markdown(
    f"""<a href="{link_para_outra_pagina}">
    <img src="data:image/png;base64,{imagem_base64}" width="30">
    </a>""",
    unsafe_allow_html=True,
)


