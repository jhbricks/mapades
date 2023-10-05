import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np
import libpysal
import mapclassify
import leafmap
import leafmap.foliumap as leafmap
from streamlit_extras.colored_header import colored_header


st.set_page_config(layout="wide",page_title='Classificação dos dados')
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.markdown("<h3><font size='8'  color='gray'>Classificação dos dados</font></font></h3>", unsafe_allow_html=True)
st.markdown(""" **Classificação de dados** explicação  
            explicação texto texto texto  
            texto texto texto  
            texto texto texto.
""")

#inserir os arquivos csv e geojson
st.markdown("Digite as variáveis:")
c1,c2 = st.columns(2)
with c1:
    area = st.text_input('Link do dado geográfico:', placeholder = "Cole o link do arquivo geojson.")
    arq = st.text_input('Link do indicador:', placeholder = "Cole o link do arquivo csv.")
    comum = st.text_input('Coluna em comum:', placeholder = 'Digite o nome da coluna que os aquivos tem em comum.')
    ind = st.text_input('Indicador:', placeholder = "Digite o indicador igual está no arquivo csv enviado.")
    scheme = st.text_input('Método de classificação:', placeholder = "Digite o método de classificação.")
    k = int(st.number_input("Número de classes", placeholder="Digite o número de classes que os dados serão divididos."))
    cmap = st.text_input('Paleta de cores:', placeholder = "Digite o nome da paleta de cores.")

    st.markdown("Deseja comparar diferentes classificações produzindo dois mapas?")
    on = st.toggle('Comparar duas classificações')

fields = [comum,ind]
method = scheme

with c2:
    st.write("Instruções")
    with st.expander("Instrução: Dado geográfico"):
        st.markdown("""Colar o link do arquivo do dado geográfico.  
                    O link deve contém o arquivo do tipo geojson, terminado com ".geojson", por exemplo: *link.com/area.geojson*  
                    O arquivo deverá conter uma coluna com itens e nome exatamente iguais ao do arquivo CSV, por exemplo, uma coluna denominada Município, contendo os nomes dos municípios.
                     """)
    with st.expander("Instrução: Indicador"):
        st.markdown("""Colar o link do arquivo dos indicadores.  
                    O link deve contém o arquivo como CSV, terminado com ".csv", por exemplo: *link.com/indicador.csv*   
                    O arquivo deverá conter uma coluna com itens e nome exatamente iguais ao do arquivo geojson, por exemplo, uma coluna denominada Município, contendo os nomes dos municípios.  
                    Verifique se o arquivo está usando vírgula (,) como separador.
                    """)
    with st.expander("Instrução: Coluna em comum"):
        st.markdown("""Digite o nome da columa que o arquivo do dado geográfico (geojson) e do indicador (csv) tem em comum.  
                    Por exemplo: *Município*
                    """)
    with st.expander("Instrução: Método de classificação"):
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
    with st.expander("Instrução: Número de classes"):
        st.markdown("""Digite o número de classes em que os dados serão divididos.""")
    with st.expander("Instrução: Paleta de cores"):
        st.markdown("""Digite o nome da paleta de cores escolhida exatamente como consta na página do Leafmap.
                    Link: https://leafmap.org/notebooks/23_colormaps/  
                    Sugerimos  escolher a paleta de cores com base na ferramenta Color Brewer: https://colorbrewer2.org/
                    """)
    
    if on:
        scheme1 = st.text_input('Método de classificação 1:', placeholder = "Digite o método de classificação.")
        k1 = int(st.number_input("Número de classes 1", placeholder="Digite o número de classes que os dados serão divididos."))
        cmap1 = st.text_input('Paleta de cores 1:', placeholder = "Digite o nome da paleta de cores.")


#merge
arq_csv = pd.read_csv(arq)
arq_geojson = gpd.read_file(area)
gdf = arq_geojson.merge(arq_csv, on="Município")

#métodos de classificação
methods = {
    'FisherJenks': mapclassify.FisherJenks,
    'Quantiles': mapclassify.Quantiles,
    'EqualInterval': mapclassify.EqualInterval,
    'BoxPlot': mapclassify.BoxPlot,
    'FisherJenksSampled': mapclassify.FisherJenksSampled,
    'HeadTailBreaks': mapclassify.HeadTailBreaks,
    'JenksCaspall': mapclassify.JenksCaspall,
    'JenksCaspallForced': mapclassify.JenksCaspallForced,
    'JenksCaspallSampled': mapclassify.JenksCaspallSampled,
    'MaxP': mapclassify.MaxP,
    'MaximumBreaks': mapclassify.MaximumBreaks,
    'NaturalBreaks': mapclassify.NaturalBreaks,
    'Percentiles': lambda data, bins: mapclassify.Percentiles(data, bins=[]),
    'StdMean': mapclassify.StdMean,
    'UserDefined': lambda data, bins: mapclassify.UserDefined(data, bins=[]),
}

# valores das classes
if method in methods:
    data = gdf[ind]
    q = methods[method](data, k=k)  # classificação
    medias = []  # lista das médias das classes
    Z = []  # lista da soma dos quadrados Z
    intervalos = q.bins.tolist()  # chama os intervalos das classes
    for i in range(len(intervalos)):
        if i == 0:
            dados_classe = data[data <= intervalos[i]]
        elif i == len(intervalos) - 1:
            dados_classe = data[(data > intervalos[i - 1]) & (data <= intervalos[i])]
        else:
            dados_classe = data[(data > intervalos[i - 1]) & (data <= intervalos[i])]

        media_classe = np.mean(dados_classe)  # média das classes
        medias.append(media_classe)

        sq = (dados_classe - media_classe) ** 2  # cálculo o quadrado da diferença de cada classe

        Z.append(np.sum(sq))  # calcula e guarda a soma do quadrado da diferença por essa classe

    SDCM = np.sum(Z)  # Soma de Z

    media_total = np.mean(data)

    SDAM = np.sum((data - media_total) ** 2)  # Soma de xi-X

    GVF = 100 - ((SDCM / SDAM) * 100)

    st.markdown(f"<h3><font style='font-weight: bold;'><font size='+5'> {GVF:.2f} </font> %</font></h3>",unsafe_allow_html=True)

#####LAT E LON CENTRAIS
ponto_central = arq_geojson.geometry.centroid
lat = ponto_central.iloc[0].y
lon = ponto_central.iloc[0].x
    
if not isinstance(gdf,gpd.GeoDataFrame):
    print("O arquivo não é um GeoDataFrame")
    exit()

##########################MAPA
########MAPA INICIAL
m = leafmap.Map(
    center=[lat,lon],
	#zoom = z,
	#zoom_min = zmn,
	#zoom_max = zmx,
	draw_control=False,
    measure_control=False,
    fullscreen_control=False,
    attribution_control=True)
  
#######ADICIONAR O MERGE GDF


m.add_data(data = gdf,
           column=ind,
           scheme=scheme,
           k=k,
           cmap=cmap,
           fields=fields,
           legend_position='topright',
           )

#########ADICIONAR NO STREAMLIT
m.to_streamlit()