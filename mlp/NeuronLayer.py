from numpy import random

class NeuronLayer():
    def __init__(self, NNeurons, NInputsPerNeuron):
        self.synWeights = 2 * random.random((NInputsPerNeuron, NNeurons)) - 1
