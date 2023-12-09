import streamlit as st
from streamlit_extras.colored_header import colored_header
from PIL import Image

st.set_page_config(layout="wide", page_title="Sobre")
st.markdown("""<style>.block-container {padding-top: 1rem;padding-left: 2rem;padding-right: 2rem;}</style>""", unsafe_allow_html=True)

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
cg = "https://cienciasgeodesicas.ufpr.br/wp-content/uploads/2021/03/PPGCG-assinatura-horizontal-colorida-1-priorit%C3%A1ria.png"
i1 = Image.open(km)
i2 = Image.open(ge)
i3 = Image.open(cg)
a1 = i1.resize((210, 100))
a2 = i2.resize((200,100))
a3 = i3.resize((210,100))
c1, c2, c3 = st.columns(3)

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
    st.markdown("""**Contato:**
                \n email: contato@kurytibametropole.org
                \n Site: [Kurytiba Metropole](https://www.kurytibametropole.org/) 
                \n Instagram: [@kurytibametropole](https://www.instagram.com/kurytibametropole/)
                \n Facebook: [Kurytiba Metropole](https://www.facebook.com/kurytibametropole)""",unsafe_allow_html=True)

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
    st.markdown("""**Contato:**
                \n CNPq Lattes: [Grupo de pesquisa](https://dgp.cnpq.br/dgp/espelhogrupo/6395737613746571) 
                \n Site: [GAMAECO](https://gemaeco.ufpr.br/) 
                \n Instagram: [@ufpr_oficial](https://www.instagram.com/ufpr_oficial/)
                \n Facebook: [UFPR](https://www.facebook.com/UFPRoficial)""",unsafe_allow_html=True)

with c3:
    st.image(a3)
    st.markdown("""O Programa de Pós Graduação em Ciências Geodésicas (PPGCG)   
                da Universidade Federal do Paraná (UFPR)   
                está inserido na área das Ciências Geodésicas, que se   
                constitui de um ramo das geociências incumbido da medição,   
                representação e modelagem da superfície da Terra, incluindo   
                o campo gravitacional e suas variações espaço-temporais.   
                As áreas de concentração do PPGCG são:   
                • Cartografia e SIG   
                • Geodésia e Levantamentos   
                • Sensoriamento Remoto e Fotogrametria
                """)
    st.markdown("""**Contato:**
                \n Site: [PPGCG](https://cienciasgeodesicas.ufpr.br/) 
                \n Instagram: [@ppgcg_ufpr](https://www.instagram.com/ppgcg_ufpr)""",unsafe_allow_html=True)