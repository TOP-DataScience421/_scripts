from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import array, linspace
from numpy import set_printoptions
from sklearn.linear_model import LinearRegression

from random import shuffle


rcParams['toolbar'] = 'None'
rcParams['font.size'] = 14
rcParams['axes.titlesize'] = 18
set_printoptions(suppress=True)


N = 100

X = array([100,  90,  80, 100,  80,  80, 100,  90,  80,  60, 100,  80,  90,
            80,  60,  90,  70, 100,  80,  80,  70, 100, 100,  60,  60,  80,
            90,  90,  80,  70,  90,  90,  90,  80,  60,  80,  70,  70,  90,
           100,  90,  80,  90,  80,  90,  80,  80,  80,  70,  90,  70,  70,
           100,  80, 100,  70,  70,  80,  80,  80,  60, 100,  80,  70,  70,
            80,  70,  80,  80,  90,  90,  80,  70,  70,  70, 100,  90,  70,
            70,  80,  70,  80,  80,  80,  60,  80,  80,  70,  90,  70,  80,
            80,  90,  80,  90, 100,  70,  60, 100,  70])

Y = array([40, 45, 30, 45, 35, 35, 40, 35, 35, 30, 45, 35, 40, 35, 30, 35, 30,
           50, 35, 35, 30, 45, 45, 30, 30, 35, 40, 40, 30, 35, 45, 40, 40, 40,
           25, 40, 30, 35, 40, 45, 40, 35, 40, 35, 45, 35, 35, 35, 35, 35, 30,
           30, 45, 35, 50, 30, 30, 35, 35, 35, 25, 45, 35, 30, 30, 35, 30, 35,
           40, 40, 40, 35, 35, 35, 35, 45, 45, 35, 35, 35, 30, 30, 35, 35, 30,
           35, 40, 35, 40, 35, 35, 35, 40, 35, 40, 45, 35, 25, 45, 30])

X_mean = X.mean()
Y_mean = Y.mean()

# точечный график пар значений случайных величин
plt.scatter(X, Y)
plt.scatter(X_mean, Y_mean, s=45, c='#000')
plt.text(X_mean, Y_mean, ' A')

model = LinearRegression()
model.fit(X.reshape(-1, 1), Y.reshape(-1, 1))

k, b = model.coef_[0][0], model.intercept_[0]

print(f'функция линейной модели: y = {k:.2f}*x + {b:.2f}')

# прямая теоретической линии регрессии
plt.axline((X_mean, Y_mean), slope=k, c='#f21', linewidth=3)

# запуск GUI matplotlib
plt.show()

