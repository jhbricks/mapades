import streamlit as st
from streamlit_extras.colored_header import colored_header
from deff.mapa import mapa
from deff.mapa import grafico
from deff.calculos import conta


st.set_page_config(layout="wide", page_title="Renda - Mapa da Desigualdade")
st.markdown("""<style>.block-container {padding-top: 1rem;}</style>""", unsafe_allow_html=True)

#Selecionar a área 
st.markdown("<h3><font size='7'  color='red'>Renda</font></font></h3>", unsafe_allow_html=True)
#Selecionar a área [Radio horizontal]
area = st.radio("Selecione uma área:",("Paraná","Núcleo Territorial Central de Curitiba"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#Arquivos
renda = "./dados/csv/renda.csv"

if area == "Paraná":
  op = st.radio("Selecione um indicador:",
                ("Índice de Gini", "Renda média da população", "Renda da população feminina", "Renda dos declarantes do IRPF"))
  st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
  if op == "Índice de Gini":
    colored_header(label="Índice de Gini",
                   description="Índice de Gini renda domiciliar per capita no Paraná",
                   color_name="red-70",)
    
    d1,d2 = st.columns([2,1])
    with d1:
      mapa('PR',renda,'Índice de Gini','FisherJenks',3,'PuBuGn', ['Município','Índice de Gini'],'Índice de Gini da Renda Domiciliar per Capita')
      st.markdown("""**Ano-base:** 2010  
                  **Fonte(s):** IPARDES, 2023; IBGE, 2010  
                  **Fórmula:** Índice de Gini da Renda Domiciliar per Capita  
                  **Observações:** Índice de Gini da Renda Domiciliar per Capita do Censo Demográfico de 2010, obtido no banco de dados do IPARDES.
                  """)
    with d2:
      st.markdown("**Indica a distribuição de renda em uma população. Quanto mais próximo de 0, menor é a concentração de renda no município, portanto, quanto mais próximo de 1 maior é a concentração.**")    
      conta ('PR',renda,'Índice de Gini',2010,'Índice de Gini',0.54, None)
      grafico ('PR',renda,'Índice de Gini',None)


  elif op == "Renda média da população":
    colored_header(label="Renda média da população",
                   description="Renda média da população no Paraná",
                   color_name="red-70",)
    
    d1,d2 = st.columns([2,1])
    with d1:
      mapa('PR',renda,'Renda Média da População (R$ mil)','FisherJenks',5,'YlOrRd', ['Município','Renda Média da População (R$ mil)'],'Renda Média da População (R$ mil)')
      st.markdown("""**Ano-base:** 2020  
                  **Fonte(s):** Fundação Getúlio Vargas (FGV)  
                  **Fórmula:** (Renda Média da população R$/1000)  
                  **Observações:** Renda Média da População é disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV).
                  """)    
    with d2:
      st.markdown("**Indica a renda média da população (R$) para o ano de 2020**")  
      conta ('PR',renda,'Renda Média da População (R$ mil)',2020,'Renda Média da População','media','R$ mil')
      grafico('PR',renda,'Renda Média da População (R$ mil)','R$ mil')

  elif op == "Rendimento médio da população feminina":
    colored_header(label="Rendimento médio da população feminina",
                   description="Percentual do rendimento médio real mensal das mulheres em relação ao dos homens no Paraná",
                   color_name="red-70",)
    
    d1,d2 = st.columns([2,1])
    with d1:
      mapa('PR',renda,'Rendimento médio da população feminina/masculina (%)','FisherJenks',5,'RdPu', ['Município','Rendimento médio da população feminina/masculina (%)'],'Rendimento médio da população feminina (%)')
      st.markdown("""**Ano-base:** 2021  
                  **Fonte(s):** IPARDES, RAIS  
                  **Fórmula:** (Rendimento médio da população feminina*100) /Rendimento média da população masculina   
                  **Observações:** Rendimento médio mensal é disponibilizado na RAIS (Relação Anual de Informações Sociais), obtido no banco de dados do IPARDES.
                  """)
    with d2:
      st.markdown("**Indica o percentual do rendimento médio real mensal das mulheres em relação ao dos homens celetistas e estatutários.**")  
      conta ('PR',renda,'Rendimento médio da população feminina/masculina (%)',2021,'Percentual do rendimento médio da população feminina em relação à masculina',None,None)
      grafico('PR',renda,'Rendimento médio da população feminina/masculina (%)','%')

  elif op == "Renda dos declarantes":
    colored_header(label="Renda dos declarantes do IRPF",
                   description="Renda média dos declarentes do IRPF no Paraná",
                   color_name="red-70",)
    
    d1,d2 = st.columns([2,1])
    with d1:
      mapa('PR',renda,'Renda Média dos Declarantes (R$ mil)','FisherJenks',5,'YlGn', ['Município','Renda Média dos Declarantes (R$ mil)'],'Renda Média dos Declarantes (R$ mil)')
      st.markdown("""**Ano-base:** 2020  
                  **Fonte(s):** Fundação Getúlio Vargas (FGV)  
                  **Fórmula:** (Renda Média dos declarantes R$/1000)  
                  **Observações:** Renda Média dos declarantes do IRPF é disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV).
                  """)      
    with d2:
      st.markdown("**Indica a renda média (R$) dos declarantes do Imposto de Renda Pessoa Física (IRPF) para o ano de 2020.**")  
      conta ('PR',renda,'Renda Média dos Declarantes (R$ mil)',2020,'Renda Média dos Declarantes','media','R$ mil')
      grafico('PR',renda,'Renda Média dos Declarantes (R$ mil)','R$ mil')

   
else:
  area == "Núcleo Territorial Central de Curitiba"
  op = st.radio("Selecione um indicador:",
                ("Índice de Gini", "Renda média da população", "Renda da população feminina", "Renda dos declarantes do IRPF"))
  st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
  if op == "Índice de Gini":
    colored_header(label="Índice de Gini",
                   description="Índice de Gini renda domiciliar per capita no Núcleo Territorial Central de Curitiba",
                   color_name="red-70",)
    
    c1,c2 = st.columns([2,1])
    with c1:
      mapa('NTC',renda,'Índice de Gini','FisherJenks',4,'PuBuGn', ['Município','Índice de Gini'],'Índice de Gini da Renda Domiciliar per Capita')
      st.markdown("""**Ano-base:** 2010  
                  **Fonte(s):** IPARDES, IBGE  
                  **Fórmula:** Índice de Gini da Renda Domiciliar per Capita  
                  **Observações:** Índice de Gini da Renda Domiciliar per Capita do Censo Demográfico de 2010, obtido no banco de dados do IPARDES.
                  """)

    with c2:
      st.markdown("**Indica a distribuição de renda em uma população. Quanto mais próximo de 0, menor é a concentração de renda no município; portanto, quanto mais próximo de 1 maior é a concentração.**")  
      conta ('NTC',renda,'Índice de Gini',2010,'Índice de Gini',0.47, unidade = None)
      grafico ('NTC',renda,'Índice de Gini',None)

  elif op == "Renda média da população":
    colored_header(label="Renda média da população",
                   description="Renda média da população no Núcleo Territorial Central de Curitiba",
                   color_name="red-70",)
    
    c1,c2 = st.columns([2,1])
    with c1:
      mapa('NTC',renda,'Renda Média da População (R$ mil)','FisherJenks',4,'YlOrRd', ['Município','Renda Média da População (R$ mil)'],'Renda Média da População (R$ mil)')
      st.markdown("""**Ano-base:** 2020  
                  **Fonte(s):** Fundação Getúlio Vargas (FGV)  
                  **Fórmula:** (Renda Média da população R$/1000)  
                  **Observações:** Renda Média da População é disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV).
                  """) 
    with c2:
      st.markdown("**Indica a renda média da população (R$ mil) para o ano de 2020.**")  
      conta ('NTC',renda,'Renda Média da População (R$ mil)',2020,'Renda Média da População','media','R$ mil')
      grafico ('NTC',renda,'Renda Média da População (R$ mil)','R$ mil')

  elif op == "Rendimento médio da população feminina":
    colored_header(label="Rendimento médio da população feminina",
                   description="Percentual do rendimento médio real mensal das mulheres em relação ao dos homens no Núcleo Territorial Central de Curitiba",
                   color_name="red-70",)
    
    c1,c2 = st.columns([2,1])
    with c1:
      mapa('NTC',renda,'Rendimento médio da população feminina/masculina (%)','FisherJenks',4,'RdPu', ['Município','Rendimento médio da população feminina/masculina (%)'],'Rendimento médio da população feminina (%)')
      st.markdown("""**Ano-base:** 2021
                  **Fonte(s):** IPARDES, RAIS  
                  **Fórmula:** (Rendimento médio da população feminina*100) /Rendimento média da população masculina   
                  **Observações:** Rendimento médio mensal é disponibilizado na RAIS (Relação Anual de Informações Sociais), obtido no banco de dados do IPARDES.
                  """)

    with c2:
      st.markdown("**Indica o percentual do rendimento médio real mensal das mulheres em relação ao dos homens celetistas e estatutários.**")  
      conta ('NTC',renda,'Rendimento médio da população feminina/masculina (%)',2021,'Percentual do rendimento médio da população feminina em relação à masculina',None,None)
      grafico('NTC',renda,'Rendimento médio da população feminina/masculina (%)','%')

  elif op == "Renda dos declarantes do IRPF":
    colored_header(label="Renda dos declarantes do IRPF",
                   description="Renda média dos declarentes do IRPF no Núcleo Territorial Central de Curitiba",
                   color_name="red-70",)
    
    c1,c2 = st.columns([2,1])
    with c1:
      mapa('NTC',renda,'Renda Média dos Declarantes (R$ mil)','FisherJenks',4,'YlGn', ['Município','Renda Média dos Declarantes (R$ mil)'],'Renda Média dos Declarantes (R$ mil)')
      st.markdown("""**Ano-base:** 2020  
                  **Fonte(s):** Fundação Getúlio Vargas (FGV)  
                  **Fórmula:** (Renda Média dos declarantes R$/1000)  
                  **Observações:** Renda Média dos declarantes do IRPF é disponibilizado no Mapa da Riqueza elaborado pela Fundação Getúlio Vargas (FGV).
                  """)

    with c2:
      st.markdown("**Indica a renda média (R$) dos declarantes do Imposto de Renda Pessoa Física (IRPF) para o ano de 2020.**")  
      conta ('NTC',renda,'Renda Média dos Declarantes (R$ mil)',2020,'Renda Média dos Declarantes','media','R$ mil')
      grafico ('NTC',renda,'Renda Média dos Declarantes (R$ mil)','R$ mil')

