from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import array, linspace
from numpy import dot
from numpy import set_printoptions


rcParams['toolbar'] = 'None'
rcParams['font.size'] = 14
rcParams['axes.titlesize'] = 18
set_printoptions(suppress=True)


N = 100

# первая случайная величина
X = array([60, 70, 80, 90, 100])
nx = array([8, 23, 35, 20, 14])
# выборочные численные характеристики
X_mean = dot(X, nx) / N
X_var = X.var(mean=X_mean, ddof=len(X)-N+1)
# ручное вычисление дисперсии:
# X_var = sum((xi - X_mean)**2 for xi in X) / (N - 1)

# вторая случайная величина
Y = array([25, 30, 35, 40, 45, 50])
my = array([3, 20, 42, 19, 14, 2])
# выборочные численные характеристики
Y_mean = dot(Y, my) / N
Y_var = Y.var(mean=Y_mean, ddof=len(Y)-N+1)

# проверка абсолютных частот распределений случайных величин
assert N == sum(nx) == sum(my)

# абсолютные частоты пар значений случайных величин
mxy = {
    (60,25): 3,
    (60,30): 5,
    (70,30): 12,
    (70,35): 11,
    (80,30): 3,
    (80,35): 28,
    (80,40): 4,
    (90,35): 3,
    (90,40): 13,
    (90,45): 4,
    (100,40): 2,
    (100,45): 10,
    (100,50): 2,
}

# точечный график пар значений случайных величин
plt.scatter([x for x, _ in mxy], [y for _, y in mxy])
plt.scatter(X_mean, Y_mean, s=45, c='#000')
plt.text(X_mean, Y_mean, ' A')

# условные законы распределения значений Y для каждого xi
Y_xi_mij = []
for xi in X:
    y, m = [], []
    for (xi_, yj_), mij in mxy.items():
        if xi == xi_:
            y.append(yj_)
            m.append(mij)
    Y_xi_mij.append([y, m])

# опытная линия регрессии
Y_xi_mij_mean = array([
    dot(y, m) / nx[i]
    for i, (y, m) in enumerate(Y_xi_mij)
])

# точечно-линейный график ломаной опытной линии регрессии
plt.plot(X, Y_xi_mij_mean, 's-m')

# нормирование случайных величин
X_norm = (X - X.mean()) / X.std()
Y_norm = (Y - Y.mean()) / Y.std()

# средние выборочные случайных величин
X_norm_mean = dot(X_norm, nx) / N
Y_norm_mean = dot(Y_norm, my) / N

# среднеквадратичные отклонения нормированных случайных величин
X_norm_std = (dot(X_norm**2, nx)/N - X_norm_mean**2)**0.5
Y_norm_std = (dot(Y_norm**2, my)/N - Y_norm_mean**2)**0.5

# 
XY_norm_prod = 0
for (x, y), m in mxy.items():
    i = X.tolist().index(x)
    j = Y.tolist().index(y)
    XY_norm_prod += X_norm[i] * Y_norm[j] * m

# корреляционный момент
XY_corr_moment = XY_norm_prod/N - X_norm_mean*Y_norm_mean
# коэффициент корреляции
XY_corr_coeff = XY_corr_moment / (X_norm_std * Y_norm_std)

# 
X_std_bias = X_norm_std * X.std()
Y_std_bias = Y_norm_std * Y.std()

# y = kx + b
k = XY_corr_coeff * Y_std_bias / X_std_bias
b = Y_mean - k * X_mean

# прямая теоретической линии регрессии
plt.axline((X_mean, Y_mean), slope=k, c='#f21', linewidth=3)

# запуск GUI matplotlib
plt.show()

