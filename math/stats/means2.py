from numpy import array, unique, dot

# выборка случайной величины X
x_sample = array([ 80,  80,  90,  80,  80,  80,  70,  60,  70,  70,  80,  70, 100,
                   80,  80,  90,  80,  60,  80,  80,  80,  80,  90,  80, 100,  70,
                  100,  70,  90,  60,  60,  70,  70,  80,  70,  70,  60,  70,  90,
                   90,  60,  70,  80,  90,  90, 100, 100,  90,  80,  90,  90,  60,
                   80,  70,  80, 100,  80, 100,  70,  90,  90,  70,  70,  70,  80,
                   90,  80, 100, 100,  80,  80, 100, 100,  80,  80,  80,  80,  80,
                   70,  80,  90,  70,  60,  80,  90,  80,  70,  80, 100,  90,  80,
                   70,  70,  90,  90, 100,  80, 100,  70,  90])
n = len(x_sample)

# численные характеристики случайной величины X из выборки:
x_mean = x_sample.mean()
x_var = x_sample.var()
x_std = x_sample.std()


# закон распределения случайной величины X
x, nx = unique(x_sample, return_counts=True)

# численные характеристики случайной величины X из закона распределения:
x_mean = dot(x, nx) / n
x_var = dot(x**2, nx) / n - x_mean**2
x_std = x_var**0.5


