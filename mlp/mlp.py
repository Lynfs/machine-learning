from numpy import array, random 
import sys
from NeuralNetwork import NeuralNetwork
from NeuronLayer import NeuronLayer

if __name__ == "__main__":
    FirstLayer = NeuronLayer(N, I)#primeira camada(N neuronios, I entradas)
    SecondLayer = NeuronLayer(N, I)#segunda camada(N neuronio, I entradas)
    neural_network = NeuralNetwork(FirstLayer, SecondLayer)
    ArrIn, ArrOut = [[]], [[]]
    for i in range(len(ArrIn)):
        sys.stdout.write(str(neural_network.weights())+'\n')
        tinputs = array(ArrIn) #array de entradas
        toutputs = array(ArrOut).T #array de saída
        neural_network.train(tinputs, toutputs, n)#substitir n para treinar a rede, usando o conjunto de treinamento, n vezes.
        sys.stdout.write(str(neural_network.weights()))
        hidden_state, output = neural_network.Fit(array())#array de teste de rede
        sys.stdout.write('\n'+str(output))