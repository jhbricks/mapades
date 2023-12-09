import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(layout="wide",page_title="Mapa da Desigualdade")

#Remove os espaços em branco no topo
st.markdown("""<style> .block-container {padding-top: 1rem;}</style> """, unsafe_allow_html=True)

st.write("# Mapa da Desigualdade")

#st.sidebar.success("Selecione uma das páginas acima")

st.markdown("""*Mapa da Desigualdade é uma ferramenta que apresenta indicadores relacionados à
            diversos fatores que influenciam a qualidade de vida da população, destacando as
            diferenças entre as regiões do Estado do Paraná e do Núcleo Territorial Central de Curitiba.*""")   
st.markdown("**Selecione um dos temas abaixo ou abra o menu ao lado**")


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
c = 'st.sidebar.image(logos)'

with c1:
    aju = st.button("Ajuda")
    if aju:
        switch_page("Ajuda")
        
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

    mais = st.button("Mais temas")
    if mais:
        switch_page("Mais temas")

with c3:
    comp = st.button("Comparar")
    if comp:
        switch_page("Comparação")

    mun = st.button("Município")
    if mun:
        switch_page("Município")

    cla = st.button("Classificar")
    if cla:
        switch_page("Classificar")

    sob = st.button("Sobre")
    if sob:
        switch_page("Sobre")




#sidebar
logos = "./dados/imagem/3.png"

st.markdown("""<style>[data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 80%;}</style>""", unsafe_allow_html=True)

st.sidebar.info(
            """**Realização**
            \n [Kurytiba Metropole](https://www.kurytibametropole.org/) 
            \n [Gemaeco](https://gemaeco.ufpr.br/)
            \n [PPGCG](https://cienciasgeodesicas.ufpr.br/)
            \n [Mais informações](https://mapadesigualdade.streamlit.app/Sobre)""")
with st.sidebar:
    st.sidebar.image(logos)

       