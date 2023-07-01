import streamlit as st
from streamlit_extras.colored_header import colored_header
#st.markdown("<h3><font size='8'  color='red'>Contextualização</font></font></h3>", unsafe_allow_html=True)
import streamlit as st

# Define o estilo com CSS personalizado para diminuir a distância entre as linhas
st.markdown("<style>.custom-heading {line-height: 0.1;}</style>", unsafe_allow_html=True)

# Cria a linha com estilo personalizado
st.markdown("<h3 class='custom-heading'><font size='8' color='red'>Contextualização</font></h3>", unsafe_allow_html=True)

# Resto do seu código


#area = st.selectbox("Selecione uma área:", ("Paraná", "Núcleo Territorial Central
area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

if area == "Paraná":
  t1, t2, t3, t4, t5, t6 = st.tabs(["População residente", "População feminina", "População preta/parda", "Densidade demográfica", "Grau de urbanização", "Razão de dependência"])
  with t1:
    st.subheader(":red[População residente]")
    st.caption("População total do Paraná")
  with t2:
    st.subheader(":red[População feminina]")
    st.caption("Percentagem da população feminina no Paraná")
  with t3:
    colored_header(label="My New Pretty Colored Header",
                   description="This is a description",
                   color_name="violet-70",)
    
    



