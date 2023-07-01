import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.header(":red[Contextualização]") 
st.markdown(
  """
  ### Escolha uma das áreas 
  """)

area = st.selectbox("Selecione uma área:", ("Paraná", "Núcleo Territorial Central"))

if area == "Paraná":
  t1, t2, t3, t4, t5 = st.tabs(["População residente", "População feminina", "População preta/parda", "Densidade demográfica", "Grau de urbanização", "Razão de dependência"])
  with t1:
    st.subheader(":red[População residente]")
    st.caption("População total do Paraná")
  with t2:
    st.subheader(":red[População feminina]")
    st.caption("Percentagem da população feminina no Paraná")
    
    



