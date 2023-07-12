import streamlit as st
from streamlit_extras.colored_header import colored_header

colored_header(
    label="Ajuda",
    description="   ",
    color_name="light-blue-70",
)

t1, t2 = st.tabs(["Como ler mapas", "Glossário"])

with T1:
   colored_header(label="Como ler mapas",
                   description="  ",
                   color_name="light-blue-70",)
    st.markdown("""**Desig**""")
with t2:
    colored_header(label="Glossário",
                   description="  ",
                   color_name="light-blue-70",)
    st.markdown("""**Desigualdade:**atributo de elementos distintos; dessemelhança;
    diferença; disparidade. No contexto de uma sociedade, a desigualdade social é a relação
    de diferença de distribuição de bens, status e oportunidades entre pessoas ou grupos.""")
    st.markdown("""**Equidade:**  adaptação da norma geral de igualdade a situações
    específicas em busca de um resultado mais justo e inclusivo. Por exemplo, ao invés de
    distribuir o orçamento público de uma cidade de forma igualitária para cada bairro, investir
    mais do orçamento em regiões mais vulneráveis e/ou com maior número populacional.""")
    st.markdown("""**Igualdade:**valor ou importância equivalente. No entanto, quando
    essa igualdade não leva em consideração as diferenças entre pessoas, grupos e sistemas,
    ela pode perpetuar injustiças.""")
    st.markdown("""**Renda:**Fluxo anual de ganhos de um indivíduo proveniente de todos os recursos disponíveis,
    incluindo salários, lucros empresariais, rendimentos de propriedades, transferências do
    governo e outros rendimentos. (World Inequality Lab)
    ou  
    Segundo o dicionário Michaelis, valor monetário que uma pessoa ou uma instituição
    recebe, regular ou não, como pagamento por trabalho ou serviços prestados, incluindo
    juros.""")
    st.markdown("""**Riqueza:**A soma dos ativos que um indivíduo possui, incluindo bens imóveis, títulos financeiros,
    ações, negócios, contas bancárias, propriedades intelectuais e outros bens valiosos, menos
    as dívidas que o indivíduo deve. (World Inequality Lab)
    ou  
    Estoque de recursos econômicos tangíveis (imóveis, carros e outros bens duráveis) e
    intangíveis (recursos monetários e financeiros, como dinheiro na caderneta de poupança,
    ações de empresas e títulos diversos) que tenham valor monetário.""")
    st.markdown("""**Índice de Gini:** Utilizado como medida de desigualdade. O índice varia de 0 (perfeita igualdade) a 1
    índice de gini (extrema desigualdade), portanto, quanto mais próximo de 1, maior é a desigualdade""")
    
