import streamlit as st
import base64
from PIL import Image


st.set_page_config(layout="wide",page_title="Mapa da Desigualdade")

#Remove os espaços em branco no topo
st.markdown("""<style> .block-container {padding-top: 3rem;}</style> """, unsafe_allow_html=True)
# Exibir o título centralizado
texto_centralizado = """<div style="display: flex; justify-content: center; align-items: center"><h1>Mapa da Desigualdade</h1></div>"""
st.write(texto_centralizado, unsafe_allow_html=True)

#st.sidebar.success("Selecione uma das páginas acima")

st.markdown("""*Mapa da Desigualdade é uma ferramenta que apresenta indicadores relacionados à
            diversos fatores que influenciam a qualidade de vida da população, destacando as
            diferenças entre as regiões do Estado do Paraná e do Núcleo Territorial Central de Curitiba.    
            O Mapa da Desigualdade está em construção, por enquanto apenas as categorias Contextualização,
            Renda e Riqueza estão com indicadores.*""")   


texto = """<div style="display: flex; justify-content: center; align-items: center"><h1 style="font-size: 20px;"><b>Selecione um dos temas abaixo ou abra o menu ao lado</b></h1></div>"""
st.write(texto, unsafe_allow_html=True)


def criar_botao(link, imagem, texto, largura=150):
    img_base64 = base64.b64encode(open(imagem, "rb").read()).decode()
    return f'<a href="{link}" target="_self"><img src="data:image/png;base64,{img_base64}" width="{largura}" alt="{texto}"></a>'

botoes = [
    ("https://mapadesigualdade.streamlit.app/Contextualização", "./dados/imagem/icon/contx.png", "Contextualização"),
    ("https://mapadesigualdade.streamlit.app/Segurança", "./dados/imagem/icon/seg.png", "Segurança"),
    ("https://mapadesigualdade.streamlit.app/Mobilidade", "./dados/imagem/icon/mob.png", "Mobilidade"),
    ("https://mapadesigualdade.streamlit.app/Mais_temas", "./dados/imagem/icon/mais.png", "Mais Temas"),
    ("https://mapadesigualdade.streamlit.app/Ajuda", "./dados/imagem/icon/aju.png", "Ajuda"),
    ("https://mapadesigualdade.streamlit.app/Renda", "./dados/imagem/icon/renda.png", "Renda"),
    ("https://mapadesigualdade.streamlit.app/Meio_Ambiente", "./dados/imagem/icon/amb.png", "Meio Ambiente"),
    ("https://mapadesigualdade.streamlit.app/Educação", "./dados/imagem/icon/edu.png", "Educação"),
    ("https://mapadesigualdade.streamlit.app/Comparar", "./dados/imagem/icon/comp.png", "Comparar"),
    ("https://mapadesigualdade.streamlit.app/Classificar", "./dados/imagem/icon/class.png", "Classificar"),
    ("https://mapadesigualdade.streamlit.app/Riqueza", "./dados/imagem/icon/riq.png", "Riqueza"),
    ("https://mapadesigualdade.streamlit.app/Saúde", "./dados/imagem/icon/saude.png", "Saúde"),
    ("https://mapadesigualdade.streamlit.app/Cultura", "./dados/imagem/icon/cult.png", "Cultura"),
    ("https://mapadesigualdade.streamlit.app/Município", "./dados/imagem/icon/mun.png", "Comparar"),
    ("https://mapadesigualdade.streamlit.app/Sobre", "./dados/imagem/icon/sobre.png", "Sobre"),
]

num_colunas = 5
num_linhas = 3

espacamento_colunas = 10  # Espaço entre colunas

# Criar a estrutura em HTML com os botões
html_colunas = ""
for linha in range(num_linhas):
    html_colunas += f'<div style="display: flex; flex-direction: row; gap: 10px; justify-content: center; margin-bottom: {espacamento_colunas}px;">'
    html_colunas += " ".join([criar_botao(*botoes[linha * num_colunas + i]) for i in range(num_colunas)])
    html_colunas += '</div>'

# Exibir a estrutura HTML
st.write(html_colunas, unsafe_allow_html=True)


#sidebar
logos = "./dados/imagem/3.png"

st.markdown("""<style>[data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 80%;}</style>""", unsafe_allow_html=True)

with st.sidebar:
    st.sidebar.image(logos)


r = "./dados/imagem/realiz.png"
#i1 = Image.open(r)
#st.image(i1, width=600)
st.markdown("""<style> [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 80%;}</style>""", unsafe_allow_html=True)
st.image(r)




