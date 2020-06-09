from numpy import exp, array, random, dot
import sys

class NeuronLayer():
    def __init__(self, NNeurons, NInputsPerNeuron):
        self.synWeights = 2 * random.random((NInputsPerNeuron, NNeurons)) - 1

class NeuralNetwork():
    def __init__(self, FirstLayer, SecondLayer):
        self.FirstLayer = FirstLayer
        self.SecondLayer = SecondLayer

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def __sigmoidDerivative(self, x):
        return x * (1 - x)

    def train(self, tinputs, toutputs, tnuminterations):
        for cicle in range(tnuminterations):            
            FirstLayerOutput, SecondLayerOutput = self.Fit(tinputs)
            SecondLayerError = toutputs - SecondLayerOutput
            SecondLayerDelta = SecondLayerError * self.__sigmoidDerivative(SecondLayerOutput)
            FirstLayerError = SecondLayerDelta.dot(self.SecondLayer.synWeights.T)
            FirstLayerDelta = FirstLayerError * self.__sigmoidDerivative(FirstLayerOutput)
            FirstLayerAdjust = tinputs.T.dot(FirstLayerDelta)
            SecondLayerAdjust = FirstLayerOutput.T.dot(SecondLayerDelta)
            self.FirstLayer.synWeights += FirstLayerAdjust
            self.SecondLayer.synWeights += SecondLayerAdjust

    def Fit(self, inputs):
        output_from_FirstLayer = self.__sigmoid(dot(inputs, self.FirstLayer.synWeights))
        output_from_SecondLayer = self.__sigmoid(dot(output_from_FirstLayer, self.SecondLayer.synWeights))
        return output_from_FirstLayer, output_from_SecondLayer
        
    def weights(self):
        return f"First layer: {self.FirstLayer.synWeights}\n Second Layer: {self.SecondLayer.synWeights}\n"

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