import pandas as pd
import numpy as np
import libpysal
import mapclassify
#import matplotlib.pyplot as plt


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
def classes_data(gdf, ind, k, method):
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

        st.markdown(f"<h3><font style='font-weight: bold;'><font size='+5'> {GVF:.2f} </font> %</font></h3>",
                    unsafe_allow_html=True)

#valores das classes
def classify_data(gdf, ind, k, method):
    if method in methods:
        data = gdf[ind]
        q = methods[method](data, k=k) #classificação
        medias = [] #lista das médias das classes
        Z = [] #lista da soma dos quadrados Z
        intervalos= q.bins.tolist() #chama os intervalos das classes
        for i in range(len(intervalos)):
            if i == 0:
                dados_classe = data[data <= intervalos[i]]
            elif i == len(intervalos) - 1:
                dados_classe = data[(data > intervalos[i - 1]) & (data <= intervalos[i])]
            else: 
                dados_classe = data[(data > intervalos[i - 1]) & (data <= intervalos[i])]
            
            media_classe = np.mean(dados_classe) #media das classes
            medias.append(media_classe)

            sq = (dados_classe - media_classe) ** 2    #calculo o quadrado da diferença de cd classe

            Z.append(np.sum(sq))   #calcula e guarda a suma do quadrado da diferença por essa classe

        SDCM = np.sum    #Soma de xi - Z

        media_total = np.mean(data)  

        SDAM = np.sum((data - media_total)**2)    #Soma de xi-X

        GVF = 100 - ((SDCM/SDAM)*100)

        st.markdown(f"<h3><font style='font-weight: bold;><font size:'+5'> {GVF} </font> %</font></h3>", unsafe_allow_html=True)
          
