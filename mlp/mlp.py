from numpy import exp, array, random, dot

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
            FirstLayerError = SecondLayerDelta.dot(self.SecondLayer.synWeights.T)
            SecondLayerError = toutputs - SecondLayerOutput
            SecondLayerDelta = SecondLayerError * self.__sigmoidDerivative(SecondLayerOutput)
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