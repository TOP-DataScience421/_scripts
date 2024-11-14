from numpy import array

import neuron1


class NeuronLayer(list):
    """
    Модель слоя нейронов.
    """
    def __init__(self, weights):
        """weights — ndarray(2, n) — каждый столбец матрицы представляет собой вектор весов для отдельно взятого нейрона в слое"""
        weights = array(weights)
        for weight_vector in weights.T:
            self.append(neuron1.Neuron(*weight_vector))
    
    def out(self, input_data):
        """x — ndarray(2, n) — каждый столбец матрицы представляет собой вектор входных значений для отдельно взятого нейрона в слое"""
        input_data = array(input_data)
        res = []
        for i, neuron in enumerate(self):
            res.append(neuron.out(*input_data.T[i]))
        return array(res)


nl1 = NeuronLayer([
    [-1, 0, 1],
    [1, 0, -1],
])

x = array([
    [6, 7, 9],
    [7, 9, 8],
])

# >>> nl1.out(x)
# array([1, 0, 1])

