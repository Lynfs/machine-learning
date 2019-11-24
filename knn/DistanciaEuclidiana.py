import numpy as np

def DistanciaEuclidiana(data1, data2, length):
    distancia = 0
    for x in range(length):
        distancia += np.square(data1[x] - data2[x])
    return np.sqrt(distancia)