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


@st.cache_data

#Valores máximo e mínimo do indicador
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

#Icone de flecha/Município/Valor
    arrow_d = '\U0001F82B'  
    arrow_u = '\U0001F829'  
    min_str = f"{min_municipio}"
    max_str = f"{max_municipio}"
    ind_mn = f"{min_value}"
    ind_mx = f"{max_value}"

#Texto que vai aparecer
    st.markdown("<h3><font size='+5'> Municípios com o <font color='#563666'>maior</font> e <font color='#CC4FB4'>menor</font> valor:</font></h3>", unsafe_allow_html=True)
    if ind == 'Renda Média da População (R$ mil)': 
        st.markdown(f"<p><font size='+6' color='#563666'>{arrow_u}</font> <font size='+5'>{max_str} = {unidade} {ind_mx} mil </font></p>", unsafe_allow_html=True)
        st.markdown(f"<p><font size='+6' color='#563666'>{arrow_u}</font> <font size='+5'>{min_str} = {unidade} {ind_mn} mil </font></p>", unsafe_allow_html=True)
    elif ind == 'Patrimônio líquido médio da população (R$ milhões)' or ind == 'Patrimônio líquido médio dos declarantes (R$ milhões)':
      st.markdown(f"<p><font size='+6' color='#563666'>{arrow_u}</font> <font size='+5'>{max_str} = {unidade} {ind_mx} milhões </font></p>", unsafe_allow_html=True)
      st.markdown(f"<p><font size='+6' color='#563666'>{arrow_u}</font> <font size='+5'>{min_str} = {unidade} {ind_mn} milhões </font></p>", unsafe_allow_html=True)   
    elif unidade is not None:
        st.markdown(f"""<p><font size='+7' color='#563666'>{arrow_u}</font> <font size='+5'>{max_str} = {ind_mx} {unidade}</font>  
        <font size='+7' color='#CC4FB4'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn} {unidade}</font></p>""", unsafe_allow_html=True)
    else:
        st.markdown(f"<p><font size='+7' color='#563666'>{arrow_u}</font> <font size='+5'>{max_str} = {ind_mx} </font></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='line-height: 0.5;'><font size='+7' color='#CC4FB4'>{arrow_d}</font> <font size='+5'>{min_str} = {ind_mn}</font></p>", unsafe_allow_html=True)


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
  
 ###########GERAL
    if tipo == "md_int":
        media = int(data[ind].mean())
    elif tipo == "soma":
        media = data[ind].sum()
    elif tipo == "media":
        media = data[ind].mean().round(2)
    elif tipo is not None and unidade is not None:
        st.markdown(f"<h3><font size='+5'> {calc} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;'><font size='+5'> {tipo} {unidade}</font></h3>", unsafe_allow_html=True)
    elif tipo is not None and unidade is None:
        st.markdown(f"""<h3><font size='+5'> {calc} em {ano}:</font>  
        <font style='font-weight: bold;><font size:'+5'>     {tipo} </font></h3>""", unsafe_allow_html=True)
###########CONTEXTO 
    elif ind == "Densidade Demográfica (hab/km²)":
        somapop = data['População'].sum()
        somaarea = data['Areakm2'].sum()
        DEM = (somapop / somaarea).round().astype(int)
        st.markdown(f"<h3><font size='+5'> Densidade demográfica no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {DEM} </font> habitantes por km²</font></h3>", unsafe_allow_html=True)
    elif ind == 'Grau de Urbanização (%)':
        somaT = data['PCT'].sum()
        somaU = data['PCU'].sum()
        TU = ((somaU*100)/somaT).round(2)
        st.markdown(f"<h3><font size='+5'> Grau de Urbanização no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {TU} </font> %</font></h3>", unsafe_allow_html=True)
    elif ind == 'População feminina (%)':
        somaT = data['PCT'].sum()
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
 #################################################RENDA
    elif ind == "Rendimento médio da população feminina/masculina (%)":
        somaF = data['RMF'].sum()
        somaM = data['RMM'].sum()
        RFM = ((somaF*100)/somaM).round(2)
        st.markdown(f"<h3><font size='+5'> Percentual do Rendimento médio mensal da população feminina em relação a masculina no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {RFM} % </font> %</font></h3>", unsafe_allow_html=True)
    elif ind == 'Renda Média da População (R$ mil)':
        st.markdown(f"<h3><font size='+5'> {calc} no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {unidade} {tipo} mil </font></h3>", unsafe_allow_html=True)
    elif ind == 'Renda Média dos Declarantes (R$ mil)':
        st.markdown(f"<h3><font size='+5'> {calc} no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {unidade} {tipo} mil </font></h3>", unsafe_allow_html=True)
 ###################################################RIQUEZA   
    elif ind == 'Declarantes do IRPF (%)':
        st.markdown(f"<h3><font size='+5'> {calc} no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {tipo} {unidade} </font></h3>", unsafe_allow_html=True)
    elif ind == 'Patrimônio líquido médio da população (R$ milhões)':
        st.markdown(f"<h3><font size='+5'> {calc} no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {unidade} {tipo} milhões </font></h3>", unsafe_allow_html=True)
    elif ind == 'Patrimônio líquido médio dos declarantes (R$ milhões)':
        st.markdown(f"<h3><font size='+5'> {calc} no {nome} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {unidade} {tipo} milhões </font></h3>", unsafe_allow_html=True)
 ###################################################   
    else:
        st.markdown(f"<h3><font size='+5'> {calc} em {ano}:</font></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {tipo} {unidade}</font></h3>", unsafe_allow_html=True)