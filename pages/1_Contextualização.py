import streamlit as st
from streamlit_extras.colored_header import colored_header
st.markdown("<h3><font size='8'  color='red'>Contextualização</font></font></h3>", unsafe_allow_html=True)

#area = st.selectbox("Selecione uma área:", ("Paraná", "Núcleo Territorial Central

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)

area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central")

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
    
    



