import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(layout="wide",page_title="Mapa da Desigualdade")

#Remove os espaços em branco no topo
st.markdown("""<style> .block-container {padding-top: 1rem;}</style> """, unsafe_allow_html=True)

st.write("# Mapa da Desigualdade")

#st.sidebar.success("Selecione uma das páginas acima")

st.markdown("**Selecione um dos temas abaixo ou abra o menu ao lado** ")

#####Estilo dos botões
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #fad3ac;
    color: black;
    height: 3em;
    width: 10em;
    border-radius:10px;
    border:3px solid #fad3ac;
    font-size:20px;
    font-weight: bold;
    margin: auto;
    display: block;
}

div.stButton > button:hover {
	background:linear-gradient(to bottom, #fad3ac 5%, #ffe8d1 100%);
	background-color:#fad3ac;
}
</style>""", unsafe_allow_html=True)        

#####Botões
c1, c2, c3 = st.columns(3)

with c1:
    cont = st.button("Contextualização")
    if cont:
        switch_page("Contextualização")

    renda = st.button("Renda")
    if renda:
        switch_page("Renda")

    riqz = st.button("Riqueza")
    if riqz:
        switch_page("Riqueza")

with c2:
    seg = st.button("Segurança")
    if seg:
        switch_page("Segurança")

    amb = st.button("Meio ambiente")
    if amb:
        switch_page("Meio ambiente")

    edu = st.button("Educação")
    if edu:
        switch_page("Educação")

with c3:
    mais = st.button("Mais temas")
    if mais:
        switch_page("Mais temas")

    sob = st.button("Sobre")
    if sob:
        switch_page("Sobre")

    aju = st.button("Ajuda")
    if aju:
        switch_page("Ajuda")


#sidebar
logos = "./dados/imagem/3.png"

st.markdown("""<style>[data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 70%;}</style>""", unsafe_allow_html=True)

with st.sidebar:
    #st.sidebar.markdown("**Realização**")
    #st.write("[Kurytiba Metropole] (http://https://www.kurytibametropole.org/)e [Gemaeco] (https://gemaeco.ufpr.br/)")
    st.sidebar.image(logos)
    g1 = "https://gemaeco.ufpr.br/"
    k1 = "http://www.kurytibametropole.org"
    st.markdown ("[Kurytiba Metropole] (%s)" % k1) 
    #st.write("[Gemaeco] (%s)" %g1)
    st.sidebar.info(
        """🌐 Setor de [Ciência da Terra](http://www.terra.ufpr.br/) 
        \n 💠 Departamento de [Geomática](http://www.geomatica.ufpr.br/)
        \n 🌍 [Eng. Cartográfica e de Agrimensura](http://www.cartografica.ufpr.br/)""")

    st.sidebar.write("[![UFPR](http://www.ufpr.br/portalufpr/wp-content/uploads/2015/11/ufpr_logo.jpg)](https://www.ufpr.br/portalufpr/)")




    #st.sidebar.info("""[Kurytiba Metropole] (http://https://www.kurytibametropole.o   rg/)e [Gemaeco] (https://gemaeco.ufpr.br/)
     #               Mais informações [clique aqui]. (https://mapadesigualdade.streamlit.app/Sobre)""")