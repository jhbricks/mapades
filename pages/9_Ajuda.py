import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_option_menu import option_menu

selected3 = option_menu(None, ["Início", "Contextualização",  "Renda", 'Riqueza'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)
colored_header(
    label="Como ler mapas",
    description="   ",
    color_name="light-blue-70",
)
st.markdown("""texto texto""")
