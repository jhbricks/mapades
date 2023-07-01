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
    label = "População residente"
    description = "População total do estado do Paraná"
    color_name  = "red-70"
    st.subheader(label)
    st.markdown(f'<hr style="background-color: {color(color_name)}; margin-top: 0; margin-bottom: 0; height: 3px; border: none; border-radius: 3px;">',
    unsafe_allow_html=True,)
    if description:
        st.caption(description)



