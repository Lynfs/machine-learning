import DistanciaEuclidiana
from operator import itemgetter

def KNN(conjuntoTreinamento, testInstance, k): 
    distancia = {}
    sort = {}
    comprimento = testInstance.shape[1]
    for x in range(len(conjuntoTreinamento)):       
        dist = DistanciaEuclidiana.DistanciaEuclidiana(testInstance, conjuntoTreinamento.iloc[x], comprimento)
        distancia[x] = dist[0]
       
    sortedD = sorted(distancia.items(), key=itemgetter(1))
    vizinhos = []
    for x in range(k):
        vizinhos.append(sortedD[x][0])
        counts = {"Iris-setosa":0,"Iris-versicolor":0,"Iris-virginica":0}
    for x in range(len(vizinhos)):
        response = conjuntoTreinamento.iloc[vizinhos[x]][-1]
        if response in counts:
            counts[response] += 1
        else:
            counts[response] = 1

    votos = sorted(counts.items(), key=itemgetter(1), reverse=True)
    return(votos[0][0], tuple(vizinhos))