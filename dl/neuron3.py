from numpy import ndarray, array, dot

from typing import Callable


class Neuron:
    """
    Модель нейрона с динамическим количеством входов.
    """
    default_weight = 1
    
    def __init__(
            self, 
            activation_function: Callable, 
            **activation_function_params
    ):
        self._activation = activation_function
        self._af_params = activation_function_params
        self.weights = None
    
    def _create_inputs(self, n: int):
        self.weights = array([self.default_weight]*n)
    
    def _linear(self, x: ndarray):
        if self.weights is None:
            self._create_inputs(len(x))
        return dot(self.weights, x)
    
    def out(self, x: ndarray):
        return self._activation(self._linear(x), **self._af_params)


class DenseLayer(list):
    """
    Модель полносвязного слоя нейронов.
    """
    def __init__(
            self, 
            n: int, 
            activation_function: Callable, 
            **activation_function_params
    ):
        for _ in range(n):
            self.append(Neuron(activation_function, **activation_function_params))
    
    def out(self, x: ndarray):
        return array([
            neuron.out(x)
            for neuron in self
        ])



if __name__ == '__main__':
    
    import activations as af
    
    net = (
        DenseLayer(5, af.relu, cutoff=5),
        DenseLayer(2, af.step, cutoff=5),
    )
    
    x = array([2, 4, 6, 8])
    
    # breakpoint()
    
    res = x
    for layer in net:
        res = layer.out(res)
    
    print(res)

