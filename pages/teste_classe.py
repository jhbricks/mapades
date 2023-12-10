import streamlit as st
import base64

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

espacamento_colunas = 10  # Ajuste conforme necessário

# Criar a estrutura em HTML com os botões
html_colunas = ""
for linha in range(num_linhas):
    html_colunas += '<div style="display: flex; flex-direction: row; gap: 20px; justify-content: center;">'
    html_colunas += " ".join([criar_botao(*botoes[linha * num_colunas + i]) for i in range(num_colunas)])
    html_colunas += '</div>'
    html_colunas += '<hr style="margin: 20px;">'  # Adicionar espaçamento entre linhas

# Exibir a estrutura HTML
st.write(html_colunas, unsafe_allow_html=True)