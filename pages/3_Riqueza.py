import streamlit as st
from streamlit_extras.colored_header import colored_header

st.set_page_config(layout="wide")

#Selecionar a área [Radio horizontal]
st.markdown("<h3><font size='8'  color='red'>Renda</font></font></h3>", unsafe_allow_html=True)
area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


if area == "Paraná":
  t1, t2, t3, t4, t5 = st.tabs(["Domicílios com bens duráveis", "Número de veículos por pessoas", "População declarante do IRPF", "Patrimônio Líquido Médio da População", "Patrimônio Líquido Médio dos declarantes do IRPF"])
  
  with t1:
    colored_header(label="Domicílios com bens duráveis",
                   description="Percentual de domicílios com bens duráveis no Paraná",
                   color_name="red-70",)

  
  with t2:
    colored_header(label="Número de veículos por pessoas",
                   description="Número de veículos automotores por pessoa no Paraná",
                   color_name="red-70",)


  
  with t3:
    colored_header(label="População declarante do IRPF",
                   description="Percentual de declarantes do Imposto de Renda Pessoa Física (IRPF) na população municipal no Paraná",
                   color_name="red-70",)


  with t4:
    colored_header(label="Patrimônio Líquido Médio da População",
                   description="Patrimônio Líquido Médio da população no Paraná",
                   color_name="red-70",)


  with t5:
    colored_header(label="Patrimônio Líquido Médio dos declarantes do IRPF",
                   description="Patrimônio Líquido Médio dos declarantes do IRPF no Paraná",
                   color_name="red-70",)


if area == "Núcleo Territorial Central":
  t1, t2, t3, t4, t5 = st.tabs(["Domicílios com bens duráveis", "Número de veículos por pessoas", "População declarante do IRPF", "Patrimônio Líquido Médio da População", "Patrimônio Líquido Médio dos declarantes do IRPF"])
  
  with t1:
    colored_header(label="Domicílios com bens duráveis",
                   description="Percentual de domicílios com bens duráveis no Núcleo Territorial Central",
                   color_name="red-70",)

  
  with t2:
    colored_header(label="Número de veículos por pessoas",
                   description="Número de veículos automotores por pessoa no Núcleo Territorial Central",
                   color_name="red-70",)


  
  with t3:
    colored_header(label="População declarante do IRPF",
                   description="Percentual de declarantes do Imposto de Renda Pessoa Física (IRPF) na população municipal no Núcleo Territorial Central",
                   color_name="red-70",)


  with t4:
    colored_header(label="Patrimônio Líquido Médio da População",
                   description="Patrimônio Líquido Médio da população no Núcleo Territorial Central",
                   color_name="red-70",)


  with t5:
    colored_header(label="Patrimônio Líquido Médio dos declarantes do IRPF",
                   description="Patrimônio Líquido Médio dos declarantes do IRPF no Núcleo Territorial Central",
                   color_name="red-70",)
