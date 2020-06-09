from numpy import exp, array, random, dot

class NeuronLayer():
    def __init__(self, NNeurons, NInputsPerNeuron):
        self.synaptic_weights = 2 * random.random((NInputsPerNeuron, NNeurons)) - 1

class NeuralNetwork():
    def __init__(self, FirstLayer, SecondLayer):
        self.FirstLayer = FirstLayer
        self.SecondLayer = SecondLayer

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def weights(self):
        return self.FirstLayer.synaptic_weights, self.SecondLayer.synaptic_weights