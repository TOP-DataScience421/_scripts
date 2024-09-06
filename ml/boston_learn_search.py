from numpy import float64
from pandas import DataFrame
from pandas import read_csv
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error as skl_rmse, r2_score as skl_r2

from pathlib import Path
from random import randrange
from sys import path


ScoredModel = LinearRegression, float64, float64


def mlr_learn_score(
        data: DataFrame, 
        target_var: str, 
        *dep_var_labels: str
) -> ScoredModel:
    """Обучает модель множественной линейной регрессии с использованием указанных метками целевой и зависимых переменных. Вычисляет среднеквадратичное отклонение предсказанных результатов модели и коэффициент детерминации."""
    x = data.loc[:, dep_var_labels]
    y = boston[target_var]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, 
        test_size=1/3, 
        random_state=2
    )
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_predicted = model.predict(x_test)
    r2 = skl_r2(y_test, y_predicted)
    n, k = x_test.shape[0], x_test.shape[1]
    r2_adj = 1 - (1 - r2) * ((n - 1)/(n - k - 1))
    return model, skl_rmse(y_test, y_predicted), r2_adj


data_path = Path(path[0]) / 'boston.csv'
boston = read_csv(data_path, comment='#')


dep_vars = 'RM', 'LSTAT'
_, rmse_1, r2_1 = mlr_learn_score(boston, 'MEDV', *dep_vars)
print(*dep_vars, f'— RMSE = {rmse_1:.1f}, R2 = {r2_1:.2f}')

dep_vars = 'RM', 'LSTAT', 'PTRATIO', 'INDUS', 'TAX'
_, rmse_2, r2_2 = mlr_learn_score(boston, 'MEDV', *dep_vars)
print(*dep_vars, f'— RMSE = {rmse_2:.1f}, R2 = {r2_2:.2f}')

dep_vars = 'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'
_, rmse_3, r2_3 = mlr_learn_score(boston, 'MEDV', *dep_vars)
print('all', f'— RMSE = {rmse_3:.1f}, R2 = {r2_3:.2f}')

