import leafmap.leafmap as leafmap
import geopandas as gpd
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

a = "./dados/imagem/icon/renda.png"

#img = Image.open(a)
#st.button(st.image(img))


# Carregue a imagem que você deseja usar como botão
imagem_botao = "./dados/imagem/icon/renda.png"

# Adicione um link para outra página quando a imagem for clicada
link_para_outra_pagina = "https://mapadesigualdade.streamlit.app/Renda"

# Use st.image para exibir a imagem como um botão clicável
if st.button(""):
    # Redireciona para a outra página quando o botão é clicado
    st.markdown(f'[Clique aqui para acessar a outra página]({link_para_outra_pagina})')

# Exibe a imagem normalmente
st.image(imagem_botao, use_column_width=True)
