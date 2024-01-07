import streamlit as st
from streamlit_extras.colored_header import colored_header
from deff.mapa import mapa
from deff.mapa import grafico
from deff.calculos import conta


st.set_page_config(layout="wide", page_title="Riqueza - Mapa da Desigualdade", page_icon="💰")
st.markdown("""<style>.block-container {padding-top: 1rem;padding-left: 2rem;padding-right: 2rem;}</style>""", unsafe_allow_html=True)
st.markdown("<h3><font size='7'  color='red'>Riqueza</font></font></h3>", unsafe_allow_html=True)

#Selecionar a área 
#area = st.selectbox("Selecione uma área:", ("Paraná", "Núcleo Territorial Central de Curitiba"))

#Arquivos
PR = './dados/geojson/PR.geojson'
NTC = './dados/geojson/NTC.geojson'
riqueza = "./dados/csv/riqueza.csv"

#Selecionar a área [Radio horizontal]
area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central de Curitiba"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


if area == "Paraná":
  op = st.radio("Selecione um indicador:",
                  ("Domicílios com bens duráveis", "População declarante do IRPF", "Patrimônio Líquido Médio da População", "Patrimônio Líquido Médio dos declarantes do IRPF"))
#                ("Domicílios com bens duráveis", "Número de veículos por pessoas", "População declarante do IRPF", "Patrimônio Líquido Médio da População", "Patrimônio Líquido Médio dos declarantes do IRPF"))
  st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
  if op == "Domicílios com bens duráveis":
    colored_header(label="Domicílios com bens duráveis",
                   description="Percentual de domicílios com bens duráveis no Paraná",
                   color_name="red-70",)
    
    d1,d2 = st.columns([2,1])
    with d1:
      mapa('PR', riqueza, 'Domicílios com bens duráveis (%)',
           'FisherJenks', 5, 'OrRd', ['Município','Domicílios com bens duráveis (%)'],
           'Domicílios com bens duráveis (%)')
      st.markdown("""**Ano-base:** 2010  
                  **Fonte(s):** IPARDES, 2023; IBGE, 2010  
                  **Fórmula:** Percentual de domicílios com bens duráveis  
                  **Observações:** Dados do Censo Demográfico de 2010, obtido no banco de dados do IPARDES.
                  """)      

    with d2:
      st.markdown("**Indica o percentual de domicílios com bens duráveis¹ em relação ao total de domicílios disponibilizado no Censo Demográfico de 2010.**") 
      st.caption("¹ Rádio, TV, máquina de lavar, geladeira, celular, telefone fixo, computador, motocicleta e automóvel")
      conta ('PR',riqueza,'Domicílios com bens duráveis (%)',2010,
             'Percentual de domicílios com bens duráveis','media', '%')
      grafico ('PR',riqueza,'Domicílios com bens duráveis (%)','%')
 
#  elif op == "Número de veículos por pessoas":
#    colored_header(label="Número de veículos por pessoas",
#                   description="Número de veículos automotores por pessoa no Paraná",
#                   color_name="red-70",)

    
#    d1,d2 = st.columns([2,1])
#    with d1:
#      mapa('PR', riqueza, 'Veículos por pessoa',
#         'FisherJenks', 4, 'BuGn', ['Município','Veículos por pessoa'],
#         'Número de veículos por pessoas')
#      st.markdown("""**Ano-base:** 2021  
#                  **Fonte(s):** IPARDES, 2023  
#                  **Fórmula:** Número de veículos por pessoas  
#                  **Observações:** Dados disponibilizados pelo IPARDES
#                  """)

#    with d2:
#      st.markdown("**Indica o número de veículos automotores por pessoa disponibilizado pelo Instituto Paranaense de Desenvolvimento Econômico e Social (Ipardes) para o ano de 2021**") 
#      conta ('PR',riqueza,'Veículos por pessoa',2021,
#             'Número de veículos por pessoas','media', 'veículo/hab')
#      grafico ('PR',riqueza,'Veículos por pessoa','Veículo/hab')

    
  elif op == "População declarante do IRPF":
    colored_header(label="População declarante do IRPF",
                   description="Percentual de declarantes do Imposto de Renda Pessoa Física (IRPF) na população municipal no Paraná",
                   color_name="red-70",)

    
    d1,d2 = st.columns([2,1])
    with d1:
      mapa('PR', riqueza, 'Declarantes do IRPF (%)',
           'FisherJenks',5, 'BuPu', ['Município','Declarantes do IRPF (%)'],
           'População declarante do IRPF (%)')
      st.markdown("""**Ano-base:** 2020  
                  **Fonte(s):** FGV  
                  **Fórmula:** Declarantes na População  
                  **Observações:** Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)
                  """)

    with d2:
      st.markdown("**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)**") 
      conta ('PR',riqueza,'Declarantes do IRPF (%)',2020,
             'Percentual de declarantes do IRPF na população','18.05', '%')
      grafico ('PR',riqueza,'Declarantes do IRPF (%)','%')

  elif op == "Patrimônio Líquido Médio da População":
    colored_header(label="Patrimônio Líquido Médio da População",
                   description="Patrimônio Líquido Médio da população no Paraná",
                   color_name="red-70",)

    d1,d2 = st.columns([2,1])
    with d1:
      mapa('PR', riqueza,'Patrimônio líquido médio da população (R$ milhões)','FisherJenks',
           4,'YlOrBr',['Município','Patrimônio líquido médio da população (R$ milhões)'],'Patrimônio líquido médio da população (R$ milhões)')
      st.markdown("""**Ano-base:** 2020  
                  **Fonte(s):** FGV  
                  **Fórmula:** Patrimônio líquido médio da população/1000000  
                  **Observações:** Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)
                  """)

    with d2:
      st.markdown("**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)**") 
      conta ('PR',riqueza,'Patrimônio líquido médio da população (R$ milhões)',2020,
             'Patrimônio líquido médio da população','soma', 'R$ milhões')
      grafico ('PR',riqueza,'Patrimônio líquido médio da população (R$ milhões)','R$ milhões')

  elif op == "Patrimônio Líquido Médio dos declarantes do IRPF":
    colored_header(label="Patrimônio Líquido Médio dos declarantes do IRPF",
                   description="Patrimônio Líquido Médio dos declarantes do IRPF no Paraná",
                   color_name="red-70",)

    
    d1,d2 = st.columns([2,1])
    with d1:
      mapa('PR', riqueza, 'Patrimônio líquido médio dos declarantes (R$ milhões)',
           'FisherJenks', 5, 'GnBu', ['Município','Patrimônio líquido médio dos declarantes (R$ milhões)'],
           'Patrimônio líquido dos declarantes do IRPF (R$ milhões)')
      st.markdown("""**Ano-base:** 2020  
                  **Fonte(s):** FGV  
                  **Fórmula:** Patrimônio líquido médio dos declarantes do IRPF/1000000  
                  **Observações:** Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)
                  """)

    with d2:
      st.markdown("**Indica o Patrimônio Líquido Médio dos Declarantes (R$ milhões) para o ano de 2020**") 
      conta ('PR',riqueza,'Patrimônio líquido médio dos declarantes (R$ milhões)',2020,
             'Patrimônio líquido médio dos declarantes do IRPF','soma', 'R$ milhões')
      grafico ('PR',riqueza,'Patrimônio líquido médio dos declarantes (R$ milhões)','R$ milhões')


else:
  area == "Núcleo Territorial Central de Curitiba"
  op = st.radio("Selecione um indicador:",
                  ("Domicílios com bens duráveis", "População declarante do IRPF", "Patrimônio Líquido Médio da População", "Patrimônio Líquido Médio dos declarantes do IRPF"))
  #              ("Domicílios com bens duráveis", "Número de veículos por pessoas", "População declarante do IRPF", "Patrimônio Líquido Médio da População", "Patrimônio Líquido Médio dos declarantes do IRPF"))
  st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
  if op == "Domicílios com bens duráveis":
    colored_header(label="Domicílios com bens duráveis",
                   description="Percentual de domicílios com bens duráveis no Núcleo Territorial Central de Curitiba",
                   color_name="red-70",)
           
    d1,d2 = st.columns([2,1])
    with d1:
      mapa('NTC', riqueza, 'Domicílios com bens duráveis (%)',
           'FisherJenks', 3, 'OrRd', ['Município','Domicílios com bens duráveis (%)'],
           'Domicílios com bens duráveis (%)')
      st.markdown("""**Ano-base:** 2010  
                  **Fonte(s):** IPARDES, 2023; IBGE, 2010  
                  **Fórmula:** Percentual de domicílios com bens duráveis  
                  **Observações:** Dados do Censo Demográfico de 2010, obtido no banco de dados do IPARDES.
                  """)

    with d2:
      st.markdown("**Indica o percentual de domicílios com bens duráveis¹ em relação ao total de domicílios disponibilizado no Censo Demográfico de 2010.**") 
      st.caption("¹ Rádio, TV, máquina de lavar, geladeira, celular, telefone fixo, computador, motocicleta e automóvel")
      conta ('NTC',riqueza,'Domicílios com bens duráveis (%)',2010,
             'Percentual de domicílios com bens duráveis','media', '%')
      grafico ('NTC',riqueza,'Domicílios com bens duráveis (%)','%')
  
 # elif op == "Número de veículos por pessoas":
  #  colored_header(label="Número de veículos por pessoas",
#                   description="Número de veículos automotores por pessoa no Núcleo Territorial Central de Curitiba",
#                   color_name="red-70",)
#
#    d1,d2 = st.columns([2,1])
#    with d1:
#      mapa('NTC', riqueza, 'Veículos por pessoa',
#           'FisherJenks', 4, 'BuGn', ['Município','Veículos por pessoa'],
#           'Número de veículos por pessoas')
#      st.markdown("""**Ano-base:** 2021  
#                  **Fonte(s):** IPARDES, 2023    
#                  **Fórmula:** Número de veículos por pessoas  
#                  **Observações:** Dados disponibilizados pelo IPARDES
#                  """)
#
#    with d2:
#      st.markdown("**Indica o número de veículos automotores por pessoa disponibilizado pelo Instituto Paranaense de Desenvolvimento Econômico e Social (Ipardes) para o ano de 2021**") 
#      conta ('NTC',riqueza,'Veículos por pessoa',2021,
#             'Número de veículos por pessoas','media', 'veículo/hab')
#      grafico ('NTC',riqueza,'Veículos por pessoa','Veículo/hab')

  elif op == "População declarante do IRPF":
    colored_header(label="População declarante do IRPF",
                   description="Percentual de declarantes do Imposto de Renda Pessoa Física (IRPF) na população municipal no Núcleo Territorial Central de Curitiba",
                   color_name="red-70",)

    d1,d2 = st.columns([2,1])
    with d1:
      mapa('NTC', riqueza, 'Declarantes do IRPF (%)',
           'FisherJenks',3, 'BuPu', ['Município','Declarantes do IRPF (%)'],
           'População declarante do IRPF (%)')
      st.markdown("""**Ano-base:** 2020  
                  **Fonte(s):** FGV  
                  **Fórmula:** Declarantes na População  
                  **Observações:** Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)
                  """)

    with d2:
      st.markdown("**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)**") 
      conta ('NTC',riqueza,'Declarantes do IRPF (%)',2020,
             'Percentual de declarantes do IRPF na população','17', '%')
      grafico ('NTC',riqueza,'Declarantes do IRPF (%)','%')

  elif op == "Patrimônio Líquido Médio da População":
    colored_header(label="Patrimônio Líquido Médio da População",
                   description="Patrimônio Líquido Médio da população no Núcleo Territorial Central de Curitiba",
                   color_name="red-70",)

    d1,d2 = st.columns([2,1])
    with d1:
      mapa('NTC', riqueza, 'Patrimônio líquido médio da população (R$ milhões)',
           'FisherJenks', 3, 'YlOrBr', ['Município','Patrimônio líquido médio da população (R$ milhões)'],
           'Patrimônio líquido médio da população (R$ milhões)')
      st.markdown("""**Ano-base:** 2020 
                  **Fonte(s):** FGV  
                  **Fórmula:** Patrimônio líquido médio da população/1000000 
                  **Observações:** Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)
                  """)

    with d2:
      st.markdown("**Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)**") 
      conta ('NTC',riqueza,'Patrimônio líquido médio da população (R$ milhões)',2020,
             'Patrimônio líquido médio da população','soma', 'R$ milhões')
      grafico ('NTC',riqueza,'Patrimônio líquido médio da população (R$ milhões)','R$ milhões')

  elif op == "Patrimônio Líquido Médio dos declarantes do IRPF":
    colored_header(label="Patrimônio Líquido Médio dos declarantes do IRPF",
                   description="Patrimônio Líquido Médio dos declarantes do IRPF no Núcleo Territorial Central de Curitiba",
                   color_name="red-70",)

    d1,d2 = st.columns([2,1])
    with d1:
      mapa('NTC', riqueza, 'Patrimônio líquido médio dos declarantes (R$ milhões)',
           'FisherJenks', 3, 'GnBu', ['Município','Patrimônio líquido médio dos declarantes (R$ milhões)'],
           'Patrimônio líquido médio dos declarantes do IRPF (R$ milhões)')
      st.markdown("""**Ano-base:** 2020  
                  **Fonte(s):** FGV  
                  **Fórmula:** Patrimônio líquido médio dos declarantes do IRPF/1000000   
                  **Observações:** Disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV)
                  """)

    with d2:
      st.markdown("**Indica o Patrimônio Líquido Médio dos Declarantes (R$ milhões) para o ano de 2020**") 
      conta ('NTC',riqueza,'Patrimônio líquido médio dos declarantes (R$ milhões)',2020,
             'Patrimônio líquido médio dos declarantes do IRPF','soma', 'R$ milhões')
      grafico ('NTC',riqueza,'Patrimônio líquido médio dos declarantes (R$ milhões)','R$ milhões')
