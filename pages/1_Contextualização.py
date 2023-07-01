import streamlit as st
from streamlit_extras.colored_header import colored_header

#st.markdown(f"<p style='line-height: 0.2;'><font size='+16' color='red'>Contextualização</font></p>, unsafe_allow_html=True)
st.markdown("<h3><font size='10'  color='red'>Contextualização</font></font></h3>", unsafe_allow_html=True)

st.header(":red[Contextualização]") 
area = st.selectbox("Selecione uma área:", ("Paraná", "Núcleo Territorial Central"))

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
    
    



