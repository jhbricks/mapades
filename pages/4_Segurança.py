import streamlit as st
from streamlit_extras.colored_header import colored_header

colored_header(label="Indicadores de Segurança: em breve ⌛", description="   ", color_name="orange-70",)


label = "Nice title"
color_name = "red-70"
st.subheader(label)
st.write(f'<hr style="background-color: {color(color_name)}; margin-top: 0;''margin-bottom: 0; height: 3px; border: none; border-radius: 3px;">',
        unsafe_allow_html=True,)
