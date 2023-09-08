import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import pandas_ods_reader as ods
from scipy.signal import find_peaks


# Todas as medidas no automatico foram feitas com um delay de 0.2s  

lif135 = pd.read_csv('LIF135.TXT', sep='\t', encoding='latin-1').replace(',', '.', regex=True)
lif164 = pd.read_csv('LIF164.TXT', sep='\t', encoding='latin-1').replace(',', '.', regex=True)
lif182 = pd.read_csv('LIF182.TXT', sep='\t', encoding='latin-1').replace(',', '.', regex=True)
lif194 = pd.read_csv('LIF194.TXT', sep='\t', encoding='latin-1').replace(',', '.', regex=True)
lif212 = pd.read_csv('LIF212.TXT', sep='\t', encoding='latin-1').replace(',', '.', regex=True)
lif228 = pd.read_csv('LIF228.TXT', sep='\t', encoding='latin-1').replace(',', '.', regex=True)
lif246 = pd.read_csv('LIF246.TXT', sep='\t', encoding='latin-1').replace(',', '.', regex=True)
lifalph = pd.read_csv('LIFKALPH.TXT', sep='\t', encoding='latin-1').replace(',', '.', regex=True)
lifcni = pd.read_csv('LIFCNI.TXT', sep='\t', encoding='latin-1').replace(',', '.', regex=True)
Dados = ods.read_ods('Dados.ods', 1)

#                                                               #


# Definindo arrays, caso queira ver o data frame, basta mudar o nome.

lif135 = lif135.values[1:].astype(float)
lif164 = lif164.values[1:].astype(float)
lif182 = lif182.values[1:].astype(float)
lif194 = lif194.values[1:].astype(float)
lif212 = lif212.values[1:].astype(float)
lif228 = lif228.values[1:].astype(float)
lif246 = lif246.values[1:].astype(float)
lifalph = lifalph.values[1:].astype(float)
lifcni = lifcni.values[1:].astype(float)

#                                                               #


# Funções

def get_name(data):

    for name, value in globals().items():
        if value is data:
            return name


def get_alpha_beta(data): # Esta função da a posição de alpha e beta, 
                          # mas na verdade apenas ganhamos os dois maiores
                          # picos a uma distancia de 10 medidas de angulo

    peaks, _ = find_peaks(data[:, 1], height = 100, distance = 10)
    alpha_beta = peaks[np.argsort(data[peaks, 1])[-2:]]
    return alpha_beta


def get_graph(data):

    fig, ax = plt.subplots()
    ax.set_title(get_name(data))  
    ax.set_xlabel('Theta')  
    ax.set_ylabel('Z/#/0.2s')
    ax.plot(data[:, 0], data[:, 1], c='#bb21bb')
    peaks = get_alpha_beta(data)
    ax.scatter(data[peaks, 0], data[peaks, 1], c='red', s=10)

    for i, peak in enumerate(peaks):
        label = 'beta' if i == 0 else 'alpha'  
        ax.annotate(label, (data[peak, 0], data[peak, 1]), textcoords="offset points", xytext=(-20,-10), ha='center')

    plt.show()


# Lista com nome dos dados                                  #

#lif135 
#lif164 
#lif182 
#lif194 
#lif212 
#lif228 
#lif246 
#lifalph
#lifcni 

#                                                           #

plt.style.use('dark_background')
get_graph(lif194)
#print(lif194[get_alpha_beta(lif194)])









