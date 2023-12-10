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
img = "./dados/imagem/icon/renda.png"
img_b1 = base64.b64encode(open(img, "rb").read()).decode()
link = "https://mapadesigualdade.streamlit.app/Renda"

s,d,f,g,h = st.columns(5)

with s:
    img1 = "./dados/imagem/icon/contx.png"
    img_b1 = base64.b64encode(open(img1, "rb").read()).decode()
    link1 = "https://mapadesigualdade.streamlit.app/Contextualização"
    st.markdown(f"""<a href="{link1}" target="_self"><img src="data:image/png;base64,{img_b1}" width="150"></a>""",unsafe_allow_html=True)
    
    img2 = "./dados/imagem/icon/renda.png"
    img_b2 = base64.b64encode(open(img2, "rb").read()).decode()
    link2 = "https://mapadesigualdade.streamlit.app/Renda"
    st.markdown(f"""<a href="{link2}" target="_self"><img src="data:image/png;base64,{img_b2}" width="150"></a>""",unsafe_allow_html=True)
    
    img3 = "./dados/imagem/icon/riq.png"
    img_b3 = base64.b64encode(open(img3, "rb").read()).decode()
    link3 = "https://mapadesigualdade.streamlit.app/Riqueza"
    st.markdown(f"""<a href="{link3}" target="_self"><img src="data:image/png;base64,{img_b3}" width="150"></a>""",unsafe_allow_html=True)

with d:
    img4 = "./dados/imagem/icon/seg.png"
    img_b4 = base64.b64encode(open(img4, "rb").read()).decode()
    link4 = "https://mapadesigualdade.streamlit.app/Segurança"
    st.markdown(f"""<a href="{link4}" target="_self"><img src="data:image/png;base64,{img_b4}" width="150"></a>""",unsafe_allow_html=True)
    
    img5 = "./dados/imagem/icon/amb.png"
    img_b5 = base64.b64encode(open(img5, "rb").read()).decode()
    link5 = "https://mapadesigualdade.streamlit.app/Meio_Ambiente"
    st.markdown(f"""<a href="{link5}" target="_self"><img src="data:image/png;base64,{img_b5}" width="150"></a>""",unsafe_allow_html=True)
    
    img6 = "./dados/imagem/icon/edu.png"
    img_b6 = base64.b64encode(open(img6, "rb").read()).decode()
    link6 = "https://mapadesigualdade.streamlit.app/Educação"
    st.markdown(f"""<a href="{link6}" target="_self"><img src="data:image/png;base64,{img_b6}" width="150"></a>""",unsafe_allow_html=True)
    
with f:
# Use st.markdown para exibir a imagem como um link clicável
    img8 = "./dados/imagem/icon/seg.png"
    img_b8 = base64.b64encode(open(img1, "rb").read()).decode()
    link4 = "https://mapadesigualdade.streamlit.app/Segurança"
    st.markdown(f"""<a href="{link4}" target="_self"><img src="data:image/png;base64,{img_b4}" width="150"></a>""",unsafe_allow_html=True)
    
    img5 = "./dados/imagem/icon/amb.png"
    img_b5 = base64.b64encode(open(img5, "rb").read()).decode()
    link5 = "https://mapadesigualdade.streamlit.app/Meio_Ambiente"
    st.markdown(f"""<a href="{link5}" target="_self"><img src="data:image/png;base64,{img_b5}" width="150"></a>""",unsafe_allow_html=True)
    
    img7 = "./dados/imagem/icon/mais.png"
    img_b7 = base64.b64encode(open(img7, "rb").read()).decode()
    link7 = "https://mapadesigualdade.streamlit.app/Riqueza"
    st.markdown(f"""<a href="{link7}" target="_self"><img src="data:image/png;base64,{img_b7}" width="150"></a>""",unsafe_allow_html=True)

with g:
    img0 = "./dados/imagem/icon/aju.png"
    img_b0 = base64.b64encode(open(img0, "rb").read()).decode()
    link0 = "https://mapadesigualdade.streamlit.app/Ajuda"
    st.markdown(f"""<a href="{link0}" target="_self"><img src="data:image/png;base64,{img_b0}" width="150"></a>""",unsafe_allow_html=True)

    img7 = "./dados/imagem/icon/mais.png"
    img_b7 = base64.b64encode(open(img7, "rb").read()).decode()
    link7 = "https://mapadesigualdade.streamlit.app/Mais_temas"
    st.markdown(f"""<a href="{link7}" target="_self"><img src="data:image/png;base64,{img_b7}" width="150"></a>""",unsafe_allow_html=True)

    img6 = "./dados/imagem/icon/edu.png"
    img_b6 = base64.b64encode(open(img1, "rb").read()).decode()
    link6 = "https://mapadesigualdade.streamlit.app/Educação"
    st.markdown(f"""<a href="{link6}" target="_self"><img src="data:image/png;base64,{img_b6}" width="150"></a>""",unsafe_allow_html=True)

with h:
    img0 = "./dados/imagem/icon/aju.png"
    img_b0 = base64.b64encode(open(img0, "rb").read()).decode()
    link0 = "https://mapadesigualdade.streamlit.app/Ajuda"
    st.markdown(f"""<a href="{link0}" target="_self"><img src="data:image/png;base64,{img_b0}" width="150"></a>""",unsafe_allow_html=True)

    img7 = "./dados/imagem/icon/mais.png"
    img_b7 = base64.b64encode(open(img7, "rb").read()).decode()
    link7 = "https://mapadesigualdade.streamlit.app/Mais_temas"
    st.markdown(f"""<a href="{link7}" target="_self"><img src="data:image/png;base64,{img_b7}" width="150"></a>""",unsafe_allow_html=True)

    img6 = "./dados/imagem/icon/edu.png"
    img_b6 = base64.b64encode(open(img1, "rb").read()).decode()
    link6 = "https://mapadesigualdade.streamlit.app/Educação"
    st.markdown(f"""<a href="{link6}" target="_self"><img src="data:image/png;base64,{img_b6}" width="150"></a>""",unsafe_allow_html=True)