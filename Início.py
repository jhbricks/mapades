import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(layout="wide",page_title="Mapa da Desigualdade")

#Remove os espaços em branco no topo
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.write("# Mapa da Desigualdade")

st.sidebar.success("Selecione uma das páginas acima")

st.markdown(
    """
    Mapa da Desigualdade é uma ferramenta para indicar a situação do local e blablablabalabal
    **Selecione um dos temas abaixo ou abra o menu ao lado** 
    """)

#####Estilo dos botões
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #faecca;
    color: black;
    height: 3em;
    width: 12em;
    border-radius:10px;
    border:3px solid #faecca;
    font-size:20px;
    font-weight: bold;
    margin: auto;
    display: block;
}

div.stButton > button:hover {
	background:linear-gradient(to bottom, #faecca 5%, #f0ede6 100%);
	background-color:##faecca;
}
</style>""", unsafe_allow_html=True)        

#####Botões
c1, c2, c3 = st.columns(3)

with c1:
    cont = st.button("Contextualização")
    if cont:
        switch_page("Contextualização")

    seg = st.button("Segurança")
    if seg:
        switch_page("Segurança")

    out = st.button("Mais temas")
    if out:
        switch_page("Mais temas")

with c2:
    renda = st.button("Renda")
    if renda:
        switch_page("Renda")

    amb = st.button("Meio ambiente")
    if amb:
        switch_page("Meio ambiente")

    sob = st.button("Sobre")
    if sob:
        switch_page("Sobre")

with c3:
    riqz = st.button("Riqueza")
    if riqz:
        switch_page("Riqueza")

    edu = st.button("Educação")
    if edu:
        switch_page("Educação")

    aju = st.button("Ajuda")
    if aju:
        switch_page("Ajuda")
