import streamlit as st
from streamlit_extras.colored_header import colored_header

st.set_page_config(layout="wide")
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

t1, t2 = st.tabs(["Como ler mapas", "Glossário"])

with t1:
    colored_header(label="Como ler mapas",description="  ",color_name="light-blue-70",)
    zoom = "./dados/imagem/zoom (1).gif"
    drag = "./dados/imagem/arrastar (1).gif"
    valor = "./dados/imagem/maior menor (1).gif"
    nomes = "./dados/imagem/nomes e valores.gif"
    st.markdown("""**Funções**""")
    c1,c2,c3,c4=st.columns([1,2,1,2])
    with c1:
        st.markdown("Ao passar o cursor em cima dos municípios irá mostrar o nome do município e o valor do indicador.")
    with c2:
        st.image(nomes)
    with c3:
        st.markdown("Os marcadores com setas indica os municípios com o menor (↓) e o maior (↑) valor do indicador.")
    with c4:
        st.image(valor)

with t2:
    colored_header(label="Glossário",description="  ",color_name="light-blue-70",)
    st.markdown("""**:blue[Desigualdade]:** atributo de elementos distintos; dessemelhança; diferença; disparidade. No contexto de uma sociedade, a desigualdade social é a relação
    de diferença de distribuição de bens, status e oportunidades entre pessoas ou grupos.""")
    st.markdown("""**:blue[Igualdade]:** valor ou importância equivalente. No entanto, quando
    essa igualdade não leva em consideração as diferenças entre pessoas, grupos e sistemas,
    ela pode perpetuar injustiças.""")
    st.markdown("""**:blue[Equidade]:**  adaptação da norma geral de igualdade a situações
    específicas em busca de um resultado mais justo e inclusivo. Por exemplo, ao invés de
    distribuir o orçamento público de uma cidade de forma igualitária para cada bairro, investir
    mais do orçamento em regiões mais vulneráveis e/ou com maior número populacional.""")
    st.markdown("""**:blue[Renda]:** Fluxo anual de ganhos de um indivíduo proveniente de todos os recursos disponíveis,
    incluindo salários, lucros empresariais, rendimentos de propriedades, transferências do
    governo e outros rendimentos. (World Inequality Lab)
    ou  
    Segundo o dicionário Michaelis, valor monetário que uma pessoa ou uma instituição
    recebe, regular ou não, como pagamento por trabalho ou serviços prestados, incluindo
    juros.""")
    st.markdown("""**:blue[Riqueza]:** A soma dos ativos que um indivíduo possui, incluindo bens imóveis, títulos financeiros,
    ações, negócios, contas bancárias, propriedades intelectuais e outros bens valiosos, menos
    as dívidas que o indivíduo deve. (World Inequality Lab)
    ou  
    Estoque de recursos econômicos tangíveis (imóveis, carros e outros bens duráveis) e
    intangíveis (recursos monetários e financeiros, como dinheiro na caderneta de poupança,
    ações de empresas e títulos diversos) que tenham valor monetário.""")
    st.markdown("""**:blue[Índice de Gini]:** Utilizado como medida de desigualdade. O índice varia de 0 (perfeita igualdade) a 1
    índice de gini (extrema desigualdade), portanto, quanto mais próximo de 1, maior é a desigualdade""")
    
