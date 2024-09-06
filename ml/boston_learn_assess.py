from pandas import DataFrame
from pandas import read_csv
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error as skl_rmse, r2_score as skl_r2

from pathlib import Path
from sys import path


data_path = Path(path[0]) / 'boston.csv'
boston = read_csv(data_path, comment='#')


# отбор признаков
x = boston.loc[:, ['RM', 'LSTAT']]
y = boston['MEDV']

# разделение набора данных на обучающий и тестовый
x_train, x_test, y_train, y_test = train_test_split(
    x, y, 
    test_size=1/3, 
    random_state=2
)

# проверка корректности разделения
assert len(x_train) + len(x_test) == len(x)
assert len(y_train) + len(y_test) == len(y)

# обучение модели
model = LinearRegression()
model.fit(x_train, y_train)

# тестирование модели
y_predicted = model.predict(x_test)

assert len(y_test) == len(y_predicted)

# сооздание DataFrame для сравнения известных и предсказанных моделью значений целевой переменной
compare = x_test.copy()
compare['MEDV'] = y_test
compare['MEDV_PRED'] = y_predicted.round(1)

# метрика 1
# среднекадратичное отклонение между известными и предсказанными моделью значениями целевой переменной
rmse = (sum((y_test - y_predicted)**2) / len(y_test))**0.5
rmse_ = skl_rmse(y_test, y_predicted)

# метрика 2
# коэффициент детерминации — доля значений зависимых переменных, для которых успешно (с минимальным отклонением) предсказаны значения целевой переменной
r2 = 1 - rmse**2 * len(y_test) / sum((y_test - y_test.mean())**2)
r2_ = skl_r2(y_test, y_predicted)

print(
    f'(man) RMSE = {rmse:.3f}',
    f'(skl) RMSE = {rmse_:.3f}',
    f'(man) R2 = {r2:.3f}',
    f'(skl) R2 = {r2_:.3f}',
    sep='\n'
)

