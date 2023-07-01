import streamlit as st
from streamlit_extras.colored_header import colored_header

st.set_page_config(layout="wide")

#Selecionar a área [Radio horizontal]
st.markdown("<h3><font size='8'  color='red'>Contextualização</font></font></h3>", unsafe_allow_html=True)
#area = st.selectbox("Selecione uma área:", ("Paraná", "Núcleo Territorial Central
area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


if area == "Paraná":
  t1, t2, t3, t4, t5, t6 = st.tabs(["População residente", "População feminina", "População preta/parda", "Densidade demográfica", "Grau de urbanização", "Razão de dependência"])
  with t1:
    colored_header(label="População residente",
                   description="População total do Paraná",
                   color_name="red-70",)
    
  with t2:
    colored_header(label="População feminina",
                   description="Percentagem da população feminina no Paraná",
                   color_name="red-70",)
    
  with t3:
    colored_header(label="My New Pretty Colored Header",
                   description="This is a description",
                   color_name="red-70",)
    
    



