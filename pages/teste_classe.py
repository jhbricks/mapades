import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np
import libpysal
import mapclassify
import leafmap
import leafmap.foliumap as leafmap
from streamlit_extras.colored_header import colored_header
from deff.classe import gvf

st.set_page_config(layout="wide",page_title='Classificação dos dados')
st.markdown("""<style>.block-container {padding-top: 1rem;}</style>""", unsafe_allow_html=True)

st.markdown("<h3><font size='8'  color='gray'>Classificação dos dados</font></font></h3>", unsafe_allow_html=True)
st.markdown(""" **Classificação de dados**   
            Demonstração da classificação de dados em um Mapa Coroplético utilizando a biblioteca python Leafmap.""")


c1,c2 = st.columns(2)
with c1:
    form = st.form(key="form_settings")
    form.markdown("Digite as variáveis:")

    area = form.text_input('Link do dado geográfico:', placeholder = "Cole o link do arquivo geojson.")
    arq = form.text_input('Link do indicador:', placeholder = "Cole o link do arquivo csv.")
    comum = form.text_input('Coluna em comum:', placeholder = 'Digite o nome da coluna que os aquivos tem em comum.')
    ind = form.text_input('Indicador:', placeholder = "Digite o indicador igual está no arquivo csv enviado.")
    scheme = form.text_input('Método de classificação:', placeholder = "Digite o método de classificação.")
    k = int(form.number_input("Número de classes", placeholder="Digite o número de classes que os dados serão divididos."))
    cmap = form.text_input('Paleta de cores:', placeholder = "Digite o nome da paleta de cores.")

    form.markdown("Deseja comparar diferentes classificações produzindo dois mapas?")
    on = form.toggle('Comparar duas classificações')

    if on:
        scheme1 = form.text_input('Método de classificação 2:', placeholder = "Digite o método de classificação.")
        k1 = int(form.number_input("Número de classes 2", placeholder="Digite o número de classes que os dados serão divididos."))
        cmap1 = form.text_input('Paleta de cores 2:', placeholder = "Digite o nome da paleta de cores.")

    teste = form.form_submit_button(label="Submit")

fields = [comum,ind]
method = scheme

with c2:
    st.write("Instruções")
    with st.expander("Dado geográfico"):
        st.markdown("""Colar o link do arquivo do dado geográfico.  
                    O link deve contém o arquivo do tipo geojson, terminado com ".geojson", por exemplo: *link.com/area.geojson*  
                    O arquivo deverá conter uma coluna com itens e nome exatamente iguais ao do arquivo CSV, por exemplo, uma coluna denominada Município, contendo os nomes dos municípios.
                     """)
    with st.expander("Link do Indicador"):
        st.markdown("""Colar o link do arquivo dos indicadores.  
                    O link deve contém o arquivo como CSV, terminado com ".csv", por exemplo: *link.com/indicador.csv*   
                    O arquivo deverá conter uma coluna com itens e nome exatamente iguais ao do arquivo geojson, por exemplo, uma coluna denominada Município, contendo os nomes dos municípios.  
                    Verifique se o arquivo está usando vírgula (,) como separador.
                    """)
    with st.expander("Coluna em comum"):
        st.markdown("""Digite o nome da columa que o arquivo do dado geográfico (geojson) e do indicador (csv) tem em comum.  
                    Por exemplo: *Município*
                    """)
    with st.expander("Indicador"):
        st.markdown("""Digite o nome da coluna que contem os dados do indicador que deseja mostrar. O nome deve ser digitado exatamente como está no arquivo csv.   
                    Por exemplo: *População*
                    """)
    with st.expander("Método de classificação"):
        st.markdown("Digite o Método de classificação dos dados escolhido. Os métodos disponíveis são:")
        m1,m2 = st.columns(2)
        with m1:
            st.markdown("""BoxPlot  
                        EqualInterval  
                        FisherJenks  
                        FisherJenksSampled  
                        HeadTailBreaks  
                        JenksCaspall  
                        JenksCaspallForced  
                        JenksCaspallSampled""")
        with m2:
              st.markdown("""MaxP  
                          MaximumBreaks  
                          NaturalBreaks  
                          Quantiles  
                          Percentiles  
                          StdMean  
                          UserDefined""")
        st.markdown("Mais informações acessar a página do Leafmap: https://leafmap.org/notebooks/53_choropleth/")
    with st.expander("Número de classes"):
        st.markdown("""Digite o número de classes em que os dados serão divididos.""")
    with st.expander("Paleta de cores"):
        st.markdown("""Digite o nome da paleta de cores escolhida exatamente como consta na página do Leafmap.
                    Link: https://leafmap.org/notebooks/23_colormaps/  
                    Sugerimos  escolher a paleta de cores com base na ferramenta Color Brewer: https://colorbrewer2.org/
                    """)
    with st.expander("Comparação de classificações"):
        st.markdown("""Ao escolher comparar duas classificações o usuário poderá escolher entre dois métodos de classificações, dois números de classes e/ou duas paleta de cores
                    para o mesmo dado (indicador), preenchendo os novos campos que apareceram.""")

if teste:
    if on:
        g1,g2 = st.columns(2)
        with g1:
            gvf(area,arq,comum,ind,scheme,k,cmap) 
        with g2:
            gvf(area,arq,comum,ind,scheme1,k1,cmap1)
    else:
        gvf(area,arq,comum,ind,scheme,k,cmap)


