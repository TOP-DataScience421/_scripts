from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import (
    array, 
    arange, 
    average,
    linspace,
    var as np_var
)
from scipy.stats import describe

rcParams['toolbar'] = 'None'
rcParams['font.size'] = 14
rcParams['axes.titlesize'] = 18


N = 10000

x = linspace(0, 2, N)
y = array(list(map(lambda x: x - 0.25*x**3, x)))

# plt.plot(x, y)
# plt.show()

# аналитическое вычисление определённых интегралов
mx = 16/15
dx = 44/225
stdx = dx**0.5

# вычисление численными методами
mx_ = average(x, weights=y)
dx_ = average(x**2, weights=y) - mx_**2
stdx_ = dx_**0.5

