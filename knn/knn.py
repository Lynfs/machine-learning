import pandas as pd
import knnfunc, DistanciaEuclidiana

def main():
    col=['slength','swidth','plength','pwidth','tipo']
    iris=pd.read_csv("iris.csv",names=col)
    testSet = [[6.3, 2.7, 4.9, 1.8]]
    test = pd.DataFrame(testSet)
    k = int(input("K: "))
    result,neigh = knnfunc.KNN(iris, test, k)
    print(f"""
    tipos:
    	Iris-setosa
    	Iris-versicolor
    	Iris-virginica
    Tamanho Da base: {iris.shape[0]}
    	\n
    	""")
    print(f"Classe: {result}")
    print(f"NN para indivíduo {testSet} ====>  {neigh}\n")

main()