import leafmap.leafmap as leafmap
import geopandas as gpd
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

a = "./dados/imagem/icon/renda.png"

img = Image.open(a)
#st.button(st.image(img))



#import streamlit as st

# Carregue a imagem que você deseja usar como botão
#imagem_botao = "./dados/imagem/icon/renda.png"

# Exiba a imagem como uma imagem normal
#st.image(imagem_botao, use_column_width=True)

# Adicione um link para outra página quando a imagem for clicada
link_para_outra_pagina = "https://mapadesigualdade.streamlit.app/Renda"
st.markdown(f'<a href="{link_para_outra_pagina}"><img src="{img}"></a>', unsafe_allow_html=True)
