import pandas as pd
import numpy as np
import libpysal
import mapclassify
import matplotlib.pyplot as plt

data = popgdf['Densidade Demográfica (hab/km²)']
k=4
#q10 = mapclassify.Percentiles(data,[45,65])
#q10 = mapclassify.EqualInterval(data, k=k)
#q10 = mapclassify.HeadTailBreaks(data)

#Converte a lista em numpy array
data = np.array(data)
q10 = mapclassify.FisherJenks(data, k=k)
print(q10)

#Chama os intervalos das classes
class_intervals = q10.bins.tolist()

#Lista das médias das classes
class_means = []

#Lista da soma dos quadrados Z
Z = []

for i in range(len(class_intervals)):
    if i == 0:
        class_data = data[data <= class_intervals[i]]
    elif i == len(class_intervals) - 1:
        class_data = data[(data > class_intervals[i - 1]) & (data <= class_intervals[i])]
    else:
        class_data = data[(data > class_intervals[i - 1]) & (data <= class_intervals[i])]

    class_mean = np.mean(class_data)
    class_means.append(class_mean)

    # Calculate squared differences within each class
    squared_diffs = (class_data - class_mean) ** 2

    # Calculate and store the sum of squared differences for this class
    Z.append(np.sum(squared_diffs))

#Soma de xi-Z
SDCM = np.sum(Z)
print(f"SDCM: {SDCM}")

#Média total
total_mean = np.mean(data)

#Soma de xi-X
SDAM = np.sum((data - total_mean)**2)
print('SDAM=', SDAM)

GVF = 100 - ((SDCM/SDAM) *100)
print('GVF', GVF.round(2))

