"""
Пользовательские реализации различных функций активации.
"""

from matplotlib import pyplot as plt
from numpy import exp, linspace, array
from pandas import DataFrame

from re import compile


def step(x, cutoff=0):
    """Функция Хэвисайда (ступенчатая).
    
    cutoff — порог."""
    if x <= cutoff:
        return 0
    else:
        return 1


# выход — 5 классов
#   класс 1: [1, 0, 0, 0, 0]
#   класс 2: [0, 1, 0, 0, 0]
#   класс 3: [0, 0, 1, 0, 0]
#   класс 4: [0, 0, 0, 1, 0]
#   класс 5: [0, 0, 0, 0, 1]


def linear(x, k=1, b=0):
    """Линейная функция.
    
    k — угол наклона, b — смещение."""
    return k*x + b


def relu(x, k=1, cutoff=0):
    """Усечённая линейная функция.
    
    k — угол наклона, cutoff — порог."""
    if x <= cutoff:
        return 0
    else:
        return k * x - cutoff


def lrelu(x, k1=1, k2=0.1, cutoff=0):
    """Усечённая линейная функция c "утечкой".
    
    :param k1: угол наклона выше порога
    :param k2: угол наклона ниже порога
    :param cutoff: порог
    """
    if x <= cutoff:
        return k2 * x
    else:
        return k1*x - cutoff*(1 - k2)
    

def prelu(x, k=1, left=-1, right=1, normalization=True):
    """Параметризованная линейная функция с нормализацией.
    
    :param k: угол наклона
    :param left: нижний порог
    :param right: верхний порог
    :param normalization: приведение значений к диапазону [0;1]
    """
    if x <= left:
        return 0
    elif right <= x:
        return 1 if normalization else right
    else:
        # k = k * right / (right - left)
        if normalization:
            return (k * x - left) / (k * right)
        else:
            return k * x - left
            


def sigmoid(x, a=1, b=0):
    """Сигмоидальная логистическая функция. 
    
    :param a: угол наклона
    :param b: смещение
    """
    return 1 / (1 + exp(-a*x + b))


def tanh(x, a=1, b=0):
    """Функция гиперболического тангенса."""
    return 2*a / (1 + exp(-2*a*x + b)) - 1



if __name__ == '__main__':
    
    x = linspace(10, 100, 100)
    
    y_step = array([step(x_i, cutoff=35) for x_i in x])
    y_linear = array([linear(x_i) for x_i in x])
    y_relu = array([relu(x_i, cutoff=35) for x_i in x])
    y_lrelu = array([lrelu(x_i, k2=0.2, cutoff=35) for x_i in x])
    y_prelu = array([prelu(x_i, left=35, right=80, normalization=False) for x_i in x])
    y_sigmoid = array([sigmoid(x_i, a=0.25) for x_i in x-x.mean()])
    y_tanh = array([tanh(x_i, a=0.25) for x_i in x-x.mean()])
    
    test = DataFrame({
        'x': x,
        'step': y_step,
        'linear': y_linear,
        'relu': y_relu,
        'lrelu': y_lrelu,
        'prelu': y_prelu,
        'sigmoid': y_sigmoid,
        'tanh': y_tanh,
    })
    
    pat_ws = compile(r'\s{2,}')
    
    fig = plt.figure(figsize=(16, 7), layout='constrained')
    axs = fig.subplots(2, 4)
    
    axs[0][0].plot(x, y_step)
    axs[0][0].set(title=pat_ws.split(step.__doc__)[0])
    
    axs[0][1].plot(x, y_linear)
    axs[0][1].set(title=pat_ws.split(linear.__doc__)[0])
    
    axs[0][2].plot(x, y_relu)
    axs[0][2].set(title=pat_ws.split(relu.__doc__)[0])
    
    axs[0][3].plot(x, y_lrelu)
    axs[0][3].set(title=pat_ws.split(lrelu.__doc__)[0])
    
    axs[1][0].plot(x, y_prelu)
    axs[1][0].set(title=pat_ws.split(prelu.__doc__)[0])
    
    axs[1][1].plot(x, y_sigmoid)
    axs[1][1].set(title=pat_ws.split(sigmoid.__doc__)[0])
    
    axs[1][2].plot(x, y_tanh)
    axs[1][2].set(title=pat_ws.split(tanh.__doc__)[0])
    
    plt.show()


