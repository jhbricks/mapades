import leafmap.leafmap as leafmap
import geopandas as gpd
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

a = "./dados/imagem/icon/renda.png"

img = Image.open(a)
#st.button(st.image(img))


# Carregue a imagem que você deseja usar como botão
imagem_botao = "./dados/imagem/icon/renda.png"

# Adicione um link para outra página quando a imagem for clicada
link_para_outra_pagina = "https://mapadesigualdade.streamlit.app/Renda"

# Use st.markdown para exibir a imagem como um link
st.markdown(f'[![Botão]({imagem_botao})]({link_para_outra_pagina})')

# Carregue a imagem usando a biblioteca PIL
imagem = Image.open(imagem_botao)

# Exiba a imagem usando st.image
st.image(imagem, use_column_width=True)
