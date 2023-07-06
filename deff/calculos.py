import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import leafmap.foliumap as leafmap
import pandas as pd

contexto = "./dados/csv/contexto.csv"
pop = "./dados/csv/pop_2021.csv"
renda = "./dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"

##### VALORES MAX E MIN E SEUS MUNICÍPIOS
#area = 'PR' ou 'NTC'
#arq = arquivo csv, ex: contexto
#ind = indicador conforme está no arquivo csv
#unidade = unidade de medida do indicador, se tiver

def mx_mn (area,arq,ind,unidade=None):

    if area == 'PR':
       arq_g= "./dados/geojson/PR.geojson"
    else:
       arq_g = "./dados/geojson/NTC.geojson"

    arq_csv = pd.read_csv(arq)
    arq_geojson = gpd.read_file(arq_g)
    data = arq_geojson.merge(arq_csv, on="Município")
  
    max_value = data[ind].max()
    min_value = data[ind].min()
    max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
    min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]

    arrow_d = '\U0001F82B'  
    arrow_u = '\U0001F829'  
    min_str = f"{min_municipio}"
    max_str = f"{max_municipio}"
    ind_mn = f"{min_value}"
    ind_mx = f"{max_value}"


    st.markdown("<h3><font size='+5'> Municípios com o <font color='#6612b8'>maior</font> e <font color='#ba2db4'>menor</font> valor:</font></h3>", unsafe_allow_html=True)
    if unidade:
        st.markdown(f"""<p><font size='+7' color='#6612b8'>{arrow_u}</font> <font size='+5'>{max_str} = {ind_mx} {unidade}</font>  
        <font size='+7' color='#ba2db4'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn} {unidade}</font></p>""", unsafe_allow_html=True)
      
      #st.markdown(f"<p><font size='+5' color='#ba2db4'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn} {unidade}</font></p>", unsafe_allow_html=True)
    else:
        st.markdown(f"<p><font size='+7' color='#6612b8'>{arrow_u}</font> <font size='+5'>{max_str} = {ind_mx} </font></p>", unsafe_allow_html=True)
      #st.markdown(f"<p><font size='+5' color='#ba2db4'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn} </font></p>", unsafe_allow_html=True)
      #st.markdown(f"<p style='line-height: 0.7;'><font size='+10' color='#6612b8'>{arrow_u}</font> <font size='+5'>{max_str} = {ind_mx}</font></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='line-height: 0.5;'><font size='+7' color='#ba2db4'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn}</font></p>", unsafe_allow_html=True)

####CALCULOS PARA OS INDICADORES

#area = 'PR' ou 'NTC'
#arq = arquivo csv
#ind = indicador, como está na tabela ('População')
#ano = ano dos dados
#calc = texto antes do cálculo (soma, média), ex: 'População total'
#tipo = 'media_int' = média com número inteiro, 'soma' = somatório, 'media' = média com precisão de 2 casas. Se não especificar vai resultar em média com 2 casas
#unidade = unidade de medida do indicador, ex: 'habitantes', '%', 'hab/km²'. Se não especificar não exibirá nada.

def conta (area,arq,ind,ano,calc=None,tipo=None,unidade=None):
    
    if area == 'PR':
       arq_g= "./dados/geojson/PR.geojson"
       nome = 'Paraná'
    else:
       arq_g = "./dados/geojson/NTC.geojson"
       nome = 'Núcleo Territorial Central'

    arq_csv = pd.read_csv(arq)
    arq_geojson = gpd.read_file(arq_g)
    data = arq_geojson.merge(arq_csv, on="Município")
  
    somaT = data['PCT'].sum()
  
    if ind == "Densidade Demográfica (hab/km²)":
        somapop = data['População'].sum()
        somaarea = data['Areakm2'].sum()
        DEM = (somapop / somaarea).round().astype(int)
        st.markdown(f"<h3><font size='+5'> Densidade demográfica no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {DEM} </font> habitantes por km²</font></h3>", unsafe_allow_html=True)
    elif ind == 'Grau de Urbanização (%)':
        somaU = data['PCU'].sum()
        TU = ((somaU*100)/somaT).round(2)
        st.markdown(f"<h3><font size='+5'> Grau de Urbanização no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {TU} </font> %</font></h3>", unsafe_allow_html=True)
    elif ind == 'População feminina (%)':
        somaF = data['PCF'].sum()
        TF = ((somaF*100)/somaT).round(2)
        st.markdown(f"<h3><font size='+5'> População feminina total no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {TF} </font> %</font></h3>", unsafe_allow_html=True)
    elif ind == 'População preta ou parda (%)':
        somaPR=data['PCPR'].sum()
        somaPA=data['PCPA'].sum()
        TPP= (((somaPR + somaPA)*100)/somaT).round(2)
        st.markdown(f"<h3><font size='+5'> População preta ou parda total no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {TPP} </font> %</font></h3>", unsafe_allow_html=True)
    elif ind == 'Razão de Dependência (%)':
        soma65 = data['PP65'].sum()
        soma14 = data['PP14'].sum()
        somaPT = data['PPT'].sum()
        RD = (((soma65 + soma14)*100)/somaPT).round(2)
        st.markdown(f"<h3><font size='+5'> Razão de dependência no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {RD} </font> %</font></h3>", unsafe_allow_html=True)
    else:
        if tipo == "md_int":
            media = int(data[ind].mean())
        elif tipo == "soma":
            media = data[ind].sum()
        else:
            media = data[ind].mean().round(2)
        st.markdown(f"<h3><font size='+5'> {calc} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {media} {unidade}</font></h3>", unsafe_allow_html=True)
      #st.markdown(f"<h3><font size='+5'> {calc}:</font></h3>", unsafe_allow_html=True)  
      #st.markdown(f"<p style='font-weight: bold;'> <font size: '+5'>{media} {unidade}</font></p>", unsafe_allow_html=True)



#################################RENDA
def conta_renda (area,arq,ind,ano,calc=None,tipo=None,unidade=None):
     
    if area == 'PR':
       arq_g= "./dados/geojson/PR.geojson"
       nome = 'Paraná'
    else:
       arq_g = "./dados/geojson/NTC.geojson"
       nome = 'Núcleo Territorial Central'

    arq_csv = pd.read_csv(arq)
    arq_geojson = gpd.read_file(arq_g)
    data = arq_geojson.merge(arq_csv, on="Município")
  
    if ind == "Rendimento médio da população feminina/masculina (%)":
        somaF = data['RMF'].sum()
        somaM = data['RMM'].sum()
        RFM = ((somaF*100)/somaM).round(2)
        st.markdown(f"<h3><font size='+5'> Percentual do Rendimento médio mensal da população feminina em relação a masculina no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {RFM} % </font> %</font></h3>", unsafe_allow_html=True)
    elif ind == 'Renda Média da População (R$ mil)':
        st.markdown(f"<h3><font size='+5'> {calc} no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {unidade} {tipo} </font></h3>", unsafe_allow_html=True)
    elif ind == 'Renda Média dos Declarantes (R$ mil)':
        st.markdown(f"<h3><font size='+5'> {calc} no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {unidade} {tipo} </font></h3>", unsafe_allow_html=True)
    elif ind == 'Declarantes do IRPF (%)':
        st.markdown(f"<h3><font size='+5'> {calc} no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {tipo} {unidade} </font></h3>", unsafe_allow_html=True)
    elif ind == 'Patrimônio líquido médio da população (R$ milhões)':
        st.markdown(f"<h3><font size='+5'> {calc} no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {unidade} {tipo} </font></h3>", unsafe_allow_html=True)
    elif ind == 'Patrimônio líquido médio dos declarantes (R$ milhões)':
        st.markdown(f"<h3><font size='+5'> {calc} no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {unidade} {tipo} </font></h3>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h3><font size='+5'> {calc} no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {tipo} {unidade}</font></h3>", unsafe_allow_html=True)
