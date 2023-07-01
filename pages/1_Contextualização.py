import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.header(":red[Contextualização]") 
st.markdown(
  """
  ### Escolha uma das áreas 
  """)

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
    label= "Nice title"
    description="Cool description"
    color_name = "red"
    st.subheader(label)
    st.write(
        f'<hr style="background-color: {color(color_name)}; margin-top: 0;'
        ' margin-bottom: 0; height: 3px; border: none; border-radius: 3px;">',
        unsafe_allow_html=True,
    )
    if description:
        st.caption(description)
    
    



