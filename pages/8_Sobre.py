import streamlit as st
from streamlit_extras.colored_header import colored_header
from PIL import Image

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
st.set_page_config(layout="wide", page_title="Sobre")

colored_header(
    label="Sobre",
    description="   ",
    color_name="blue-green-70",
)
st.markdown("""O **Mapeamento das Desigualdades** na Região de
Curitiba é uma iniciativa da Kurytiba Metropole, em
parceria com o Grupo de Estudos em
Macroeconomia Ecológica (GEMAECO), vinculado
à Universidade Federal do Paraná (UFPR),
registrada como Projeto de Extensão.  
A iniciativa tem por objetivo realizar o
mapeamento multidimensional da desigualdade na
região de Curitiba, especificamente nos municípios
do Núcleo Urbano Central da Região
Metropolitana, além de explorar as suas causas,
consequências e possíveis ações públicas e
privadas para reduzi-las.
""")

colored_header(
    label="Realizadores",
    description="   ",
    color_name="blue-green-70",
)
km = "./dados/imagem/km.png"
ge = "./dados/imagem/ufprge.png"
i1 = Image.open(km)
i2 = Image.open(ge)
a1 = i1.resize((600, 400))
a2 = i2.resize((600,400))
c1, c2 = st.columns(2)

with c1:
    st.image(a1)
    st.markdown("""A **Kurytiba Metropole** é uma associação sem fins
    lucrativos e apartidária que tem como objetivo
    transformar Curitiba em uma metrópole
    sustentável, democrática, justa e com um alto
    índice de qualidade de vida para todos que nela
    habitam através de projetos de impacto social e
    construção de políticas públicas.
    """)

with c2:
    st.image(a2)
    st.markdown("""O **Grupo de Estudos em MacroEconomia Ecológica
    (GEMAECO)** é um grupo de pesquisa vinculado à
    Universidade Federal do Paraná (UFPR),
    registrado no Conselho Nacional de
    Desenvolvimento Científico e Tecnológico (CNPq),
    que tem por objetivo integrar à visão analítica da
    Economia Ecológica à Teoria Macroeconômica,
    incluindo a proposição de políticas públicas.
    """)
